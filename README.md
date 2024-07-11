# NWL Journey - Agente de Viagens com IA

- **Notion:** [NWL 16 - Journey](https://efficient-sloth-d85.notion.site/NLW-16-Journey-013b69ad79894122824abd76bc0dab9b)

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

## Aula 3 - Deploy do nosso agente de viagens na AWS

### Conceitos

- **Elastic Container Registry (ECR):** Serviço de registro de imagens Docker da AWS.
- **AWS Lambda:** Code as a service ou function serverless.
- **Application Load Balancer (ALB):** Pode ser utilizado como API para expor a função lambda a fim de ser utilizada por aplicações que não estão hospedadas na AWS. No caso de aplicações hospedadas na AWS, a plataforma fornece uma maneira direta de executar a função lambda.

### Comandos

```
$ docker build --platform linux/x86_64 -t travelagent .
$ aws configure
$ aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 653041657227.dkr.ecr.us-east-1.amazonaws.com
$ docker tag travelagent:latest 653041657227.dkr.ecr.us-east-1.amazonaws.com/travelagent:latest
$ docker push 653041657227.dkr.ecr.us-east-1.amazonaws.com/travelagent:latest
```
### Diagrama estrutural do projeto

![Diagrama estrutural do projeto](https://github.com/filipesiota/travel-agent/assets/69269724/14c08e1c-76e5-4a49-bd28-c26cfface370)
