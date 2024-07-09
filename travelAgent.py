import os
from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import initialize_agent

load_dotenv()

llm = ChatOpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
    model="gpt-3.5-turbo",
)

tools = load_tools(['ddg-search', 'wikipedia'], llm)

agent = initialize_agent(
    tools,
    llm,
    agent='zero-shot-react-description',
    verbose=True
)

query = "Vou viajar para Londres em agosto de 2024. Quero que faça um roteiro de viagem para mim com eventos que irão ocorrer na data da viagem da cidade e com o preço de passagem de São Paulo para Londres."

agent.run(query)