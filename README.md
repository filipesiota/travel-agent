# NWL Journey - Agente de Viagens com IA

## Aula 1 - LLMs e os agentes de IA

### Conceitos

- **IA Generativa:** Uma das capacidades da IA, que gera textos, imagens e outros conteúdos.
- **LLMs (Large Language Models):** Modelos de linguagem treinados com grandes quantidades de dados:
  - GPT
  - LLAMA
  - Gemini
- **Agentes de IA:** São responsáveis por fornecer ferramentas aos modelos de linguagem (LLMs) a fim de enriquecer os outputs gerados por eles.

### Vantagens

- **Informações detalhadas e personalizadas:** Baseado nas preferências do usuário.
- **Rotina completa:** Incluindo eventos, preços e informações relevantes.
- **Automatização do processo:** Agiliza a construção de um roteiro de viagem.

### Desafios

- **Limitação de contexto:** LLMs possuem um limite de tokens (palavras) que podem processar, o que limita a quantidade de informações que podem ser utilizadas para gerar um retorno.
- **Atualização de informações:** É necessário garantir que as informações sejam atualizadas para que o agente não gere resultados errados.

## Aula 2 - ReAct, RAG e supervisor

### Conceitos

- **ReAct:** É a forma com que o modelo de linguagem processa as informações a fim de ganhar mais inteligência.
- **Supervisor:** Agente responsável por pegar os outputs de todos os demais agentes, analisar as informações e decidir a resposta final.
- **Retrieval-Augmented Generation (RAG):** A geração aumentada de recuperação é um processo em que o conteúdo de uma determinada fonte de dados é transformado em números *(Embedding Model)* para que o LLM consiga entendê-lo. Após, esses números são armazenados em uma banco de dados vetorial *(Chroma)* para que o LangChain possa mandá-los para o LLM, no caso deste projeto, o GPT.

### Estruturação do projeto

- Aplicação frontend se conecta com o nosso serviço.
- Nosso serviço utiliza o framework **LangChain** para dar novas ferramentas ao nosso modelo de LLM, como acesso à internet pelo **DuckDuckGo** e a informações históricas pelo **Wikipedia**.
- O LangChain também busca informações de um site de viagens, o [dicasdeviagem.com](dicasdeviagem.com), utilizando o processo de **RAG**.

### Libs

- **bs4:** Interpretador de HTML.
- **RecursiveCharacterTextSplitter:** Dividir o texto do documento em partes menores (chunks).