import os, bs4
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_text_splitters.character import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence

load_dotenv()

llm = ChatOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    model="gpt-3.5-turbo",
)

query = """
Vou viajar para Londres em agosto de 2024. Quero que faça um roteiro de viagem para mim com eventos que irão ocorrer na data da viagem da cidade e com o preço de passagem de São Paulo para Londres.
"""

def researchAgent(query, llm):
    tools = load_tools(["ddg-search", "wikipedia"], llm)
    prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, prompt=prompt, verbose=True)
    webContext = agent_executor.invoke({ "input": query })
    return webContext["output"]

def loadData():
    loader = WebBaseLoader(
        web_paths=("https://www.dicasdeviagem.com/inglaterra/",),
        bs_kwargs=dict(parse_only=bs4.SoupStrainer(class_=("postcontentwrap", "slidecaption")))
    )
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)
    vector_store = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())
    retriever = vector_store.as_retriever()
    return retriever

def getRelevantDocs(query):
    retriever = loadData()
    relevant_documents = retriever.invoke(query)
    print(relevant_documents)
    return relevant_documents

def supervisorAgent(query, llm, webContext, relevant_documents):
    prompt_template = """
    Você é um gerente de uma agência de viagens. Sua resposta final deverá ser um roteiro de viagem completo de detalhado.
    Utilize o contexto de eventos e preços de passagens, o input do usuário e também os doucmentos relevantes para elaborar o roteiro.
    Contexto: {webContext}
    Documentos relevantes: {relevant_documents}
    Input do usuário: {query}
    Assistente:
    """

    prompt = PromptTemplate(
        input_variables=("webContext", "relevant_documents", "query"),
        template=prompt_template
    )

    sequence = RunnableSequence(prompt | llm)
    response = sequence.invoke({
        "webContext": webContext,
        "relevant_documents": relevant_documents,
        "query": query
    })
    return response

def getResponse(query, llm):
    webContext = researchAgent(query, llm)
    relevant_documents = getRelevantDocs(query)
    response = supervisorAgent(query, llm, webContext, relevant_documents)
    return response

print(getResponse(query, llm).content)