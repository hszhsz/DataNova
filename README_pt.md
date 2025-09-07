# 🚀 DataNova

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[English](./README.md) | [简体中文](./README_zh.md) | [日本語](./README_ja.md) | [Deutsch](./README_de.md) | [Español](./README_es.md) | [Русский](./README_ru.md) |[Portuguese](./README_pt.md)

> Revolucionando o desenvolvimento de data warehouses com inteligência artificial

**DataNova** é uma plataforma de desenvolvimento de data warehouses impulsionada por IA que combina grandes modelos de linguagem com ferramentas especializadas para fornecer aos times de dados capacidades inteligentes de design de arquitetura de dados, otimização de consultas e geração automatizada de pipelines. Nosso objetivo é transformar o desenvolvimento tradicional de data warehouses através de insights e recomendações impulsionadas por IA.

DataNova está agora oficialmente disponível no [Centro de Aplicações FaaS da Volcengine](https://console.volcengine.com/vefaas/region:vefaas+cn-beijing/market), onde os usuários podem experimentá-lo online através do [link de experiência](https://console.volcengine.com/vefaas/region:vefaas+cn-beijing/market/datanova/?channel=github&source=datanova) para sentir intuitivamente suas poderosas funcionalidades e operações convenientes. Ao mesmo tempo, para atender às necessidades de implantação de diferentes usuários, DataNova suporta implantação com um clique baseada na Volcengine. Clique no [link de implantação](https://console.volcengine.com/vefaas/region:vefaas+cn-beijing/application/create?templateId=683adf9e372daa0008aaed5c&channel=github&source=datanova) para completar rapidamente o processo de implantação e iniciar sua jornada de desenvolvimento inteligente de data warehouses.

Por favor, visite [o site oficial do DataNova](https://datanova.tech/) para mais detalhes.

## Demo

### Video

<https://github.com/user-attachments/assets/f3786598-1f2a-4d07-919e-8b99dfa1de3e>

Nesta demo, demonstramos como usar o DataNova para:

- Integração perfeita com serviços MCP
- Conduzir o processo de análise de dados profunda e produzir um relatório abrangente com gráficos
- Criar um áudio de podcast baseado no relatório gerado

### Replays

- [Projetar um esquema de data warehouse estrela para análise de e-commerce](https://datanova.tech/chat?replay=ecommerce-star-schema-design)
- [Otimizar o desempenho de consultas SQL complexas](https://datanova.tech/chat?replay=sql-query-optimization)
- [Construir pipelines de dados em tempo real para processar dados de streaming](https://datanova.tech/chat?replay=realtime-data-pipeline)
- [Implementar monitoramento de qualidade de dados e sistemas de alerta](https://datanova.tech/chat?replay=data-quality-monitoring)
- [Visite nosso site oficial para explorar mais replays.](https://datanova.tech/#case-studies)

---

## 📑 Tabela de Conteúdos

- [🚀 Início Rápido](#início-rápido)
- [🌟 Funcionalidades](#funcionalidades)
- [🏗️ Arquitetura](#arquitetura)
- [🛠️ Desenvolvimento](#desenvolvimento)
- [🗣️ Integração Texto-para-Fala](#integração-texto-para-fala)
- [📚 Exemplos](#exemplos)
- [❓ FAQ](#faq)
- [📜 Licença](#licença)
- [💖 Agradecimentos](#agradecimentos)
- [⭐ Histórico de Estrelas](#histórico-de-estrelas)

## Início Rápido

DataNova é desenvolvido em Python e vem com uma IU web escrita em Node.js. Para garantir um processo de configuração suave, recomendamos o uso das seguintes ferramentas:

### Ferramentas Recomendadas

- **[`uv`](https://docs.astral.sh/uv/getting-started/installation/):**
  Simplifica o gerenciamento de ambiente e dependências Python. `uv` criará automaticamente um ambiente virtual no diretório raiz e instalará todos os pacotes necessários para você—sem necessidade de instalar ambientes Python manualmente.

- **[`nvm`](https://github.com/nvm-sh/nvm):**
  Gerencia facilmente múltiplas versões do runtime Node.js.

- **[`pnpm`](https://pnpm.io/installation):**
  Instala e gerencia dependências de projetos Node.js.

### Requisitos de Ambiente

Certifique-se de que seu sistema atenda aos seguintes requisitos mínimos:

- **[Python](https://www.python.org/downloads/):** Versão `3.12+`
- **[Node.js](https://nodejs.org/en/download/):** Versão `22+`

### Instalação

```bash
# Clone o repositório
git clone https://github.com/hszhsz/DataNova.git
cd DataNova

# Instale as dependências, uv irá lidar com o interpretador do python e a criação do venv, e instalar os pacotes necessários
uv sync

# Configure .env com suas chaves de API
# Tavily: https://app.tavily.com/home
# Brave_SEARCH: https://brave.com/search/api/
# volcengine TTS: Adicione sua credencial TTS caso você a possua
cp .env.example .env

# Veja as seções abaixo 'Mecanismos de Busca Suportados' and 'Integração Texto-para-Fala' para todas as opções disponíveis

# Configure o conf.yaml para o seu modelo LLM e chaves API
# Por favor, consulte 'docs/configuration_guide.md' para maiores detalhes
cp conf.yaml.example conf.yaml

# Instale marp para geração de ppt
# https://github.com/marp-team/marp-cli?tab=readme-ov-file#use-package-manager
brew install marp-cli
```

Opcionalmente, instale as dependências IU web via [pnpm](https://pnpm.io/installation):

```bash
cd DataNova/web
pnpm install
```

### Configurações

Por favor, consulte o [Guia de Configuração](docs/configuration_guide.md) para maiores detalhes.

> [!NOTA]
> Antes de iniciar o projeto, leia o guia detalhadamente, e atualize as configurações para baterem com os seus requisitos e configurações específicas.

### Console IU

A maneira mais rápida de rodar o projeto é usar o console IU.

```bash
# Execute o projeto em um shell tipo-bash
uv run main.py
```

### Web IU

Esse projeto também inclui uma IU Web, trazendo uma experiência mais interativa, dinâmica e engajadora.

> [!NOTA]
> Você precisa instalar as dependências do IU web primeiro.

```bash
# Execute ambos os servidores de backend e frontend em modo desenvolvimento
# No macOS/Linux
./bootstrap.sh -d

# No Windows
bootstrap.bat -d
```

Abra seu navegador e visite [`http://localhost:3000`](http://localhost:3000) para explorar a IU web.

Explore mais detalhes no diretório [`web`](./web/) .

## Mecanismos de Busca Suportados

DataNova suporta múltiplos mecanismos de busca que podem ser configurados no seu arquivo `.env` usando a variável `SEARCH_API`:

- **Tavily** (padrão): Uma API de busca especializada para aplicações de IA

  - Requer `TAVILY_API_KEY` no seu arquivo `.env`
  - Inscreva-se em: <https://app.tavily.com/home>

- **DuckDuckGo**: Mecanismo de busca focado em privacidade

  - Não requer chave API

- **Brave Search**: Mecanismo de busca focado em privacidade com funcionalidades avançadas

  - Requer `BRAVE_SEARCH_API_KEY` no seu arquivo `.env`
  - Inscreva-se em: <https://brave.com/search/api/>

- **Arxiv**: Busca de artigos científicos para pesquisa acadêmica
  - Não requer chave API
  - Especializado em artigos científicos e acadêmicos

Para configurar o seu mecanismo preferido, defina a variável `SEARCH_API` no seu arquivo:

```bash
# Escolha uma: tavily, duckduckgo, brave_search, arxiv
SEARCH_API=tavily
```

## Funcionalidades

### Principais Funcionalidades

- 🤖 **Integração LLM**

  - Suporta a integração da maioria dos modelos através de [litellm](https://docs.litellm.ai/docs/providers).
  - Suporte a modelos open source como Qwen
  - Interface API compatível com a OpenAI
  - Sistema LLM multicamadas para diferentes complexidades de tarefa

### Ferramentas e Integrações MCP

- 🔍 **Busca e Recuperação**

  - Busca web com Tavily, Brave Search e mais
  - Crawling com Jina
  - Extração de Conteúdo avançada

- 🔗 **Integração MCP perfeita**

  - Expansão de capacidades de acesso para acesso a domínios privados, grafo de conhecimento, navegação web e mais
  - Integração facilitdade de diversas ferramentas de pesquisa e metodologias

### Colaboração Impulsionada por IA

- 🧠 **Humano no Loop**

  - Suporta modificação interativa de planos de arquitetura de dados usando linguagem natural
  - Suporta aceitação automática de planos de arquitetura

- 📝 **Pós-edição de Relatórios de Dados**

  - Suporta edição de blocos similar ao Notion
  - Permite otimização de IA, incluindo polimento assistido por IA, encurtamento e expansão de frases
  - Impulsionado por [tiptap](https://tiptap.dev/)

### Criação de Conteúdo

- 🎙️ **Geração de Podcast e Apresentação**

  - Geração de roteiro de podcast e síntese de áudio impulsionados por IA
  - Criação automática de apresentações PowerPoint simples
  - Templates personalizáveis para atender necessidades de conteúdo personalizadas

## Arquitetura

DataNova implementa uma arquitetura de sistema multiagente modular projetada para desenvolvimento automatizado de data warehouses e análise de dados. O sistema é construído sobre o LangGraph, implementando um fluxo de trabalho baseado em estado flexível onde os componentes se comunicam através de um sistema de passagem de mensagens bem definido.

![Diagrama de Arquitetura](./assets/architecture.png)

> Veja a demo ao vivo em [datanova.tech](https://datanova.tech/#multi-agent-architecture)

O sistema emprega um fluxo de trabalho otimizado consistindo nos seguintes componentes:

1. **Coordenador**: O ponto de entrada gerenciando o ciclo de vida do fluxo de trabalho

   - Inicia o processo de análise de dados baseado na entrada do usuário
   - Delega tarefas ao planejador em momentos apropriados
   - Serve como a interface principal entre o usuário e o sistema

2. **Planejador**: O componente estratégico responsável pela decomposição e planejamento de tarefas

   - Analisa objetivos de análise de dados e cria planos de execução estruturados
   - Determina se há contexto suficiente ou se é necessário mais exploração de dados
   - Gerencia o processo de análise de dados e decide quando gerar o relatório final

3. **Equipe de Análise de Dados**: Uma coleção de agentes especializados que executam o plano:
   - **Analista de Dados**: Conduz busca de dados e coleta de informações usando ferramentas como mecanismos de busca de dados, crawlers e até mesmo serviços MCP.
   - **Engenheiro de Dados**: Lida com processamento de dados, análise e tarefas técnicas usando ferramentas REPL Python.
   Cada agente tem acesso a ferramentas específicas otimizadas para seu papel e opera dentro do framework LangGraph

4. **Repórter**: O processador de estágio final para saídas de análise de dados
   - Agrega descobertas da equipe de análise de dados
   - Processa e organiza informações coletadas
   - Gera relatórios de análise de dados abrangentes

## Integração Texto-para-Fala

DataNova agora inclui um recurso de texto-para-fala (TTS) que permite converter relatórios de pesquisa em áudio. Este recurso usa a API TTS da Volcengine para gerar áudio de texto de alta qualidade. Características como velocidade, volume e tom também podem ser personalizadas.

### Usando a API TTS

Você pode acessar o recurso TTS através do endpoint `/api/tts`:

```bash
# Exemplo de chamada API usando curl
curl --location 'http://localhost:8000/api/tts' \
--header 'Content-Type: application/json' \
--data '{
    "text": "Esta é uma demonstração do recurso de texto-para-fala.",
    "speed_ratio": 1.0,
    "volume_ratio": 1.0,
    "pitch_ratio": 1.0
}' \
--output speech.mp3
```

## Desenvolvimento

### Testes

Execute a suíte de testes:

```bash
# Execute todos os testes
make test

# Execute arquivos de teste específicos
pytest tests/integration/test_workflow.py

# Execute testes de cobertura
make coverage
```

### Qualidade do Código

```bash
# Execute linting de código
make lint

# Formate o código
make format
```

### Depuração com LangGraph Studio

DataNova usa LangGraph como sua arquitetura de fluxo de trabalho. Você pode usar o LangGraph Studio para depurar e visualizar fluxos de trabalho em tempo real.

#### Executando LangGraph Studio Localmente

DataNova inclui um arquivo de configuração `langgraph.json` que define a estrutura do grafo e dependências para o LangGraph Studio. Este arquivo aponta para o grafo de fluxo de trabalho definido no projeto e carrega automaticamente variáveis de ambiente do arquivo `.env`.

##### Mac

```bash
# Instale o gerenciador de pacotes uv se você não o tiver
curl -LsSf https://astral.sh/uv/install.sh | sh

# Instale dependências e inicie o servidor LangGraph
uvx --refresh --from "langgraph-cli[inmem]" --with-editable . --python 3.12 langgraph dev --allow-blocking
```

##### Windows / Linux

```bash
# Instale dependências
pip install -e .
pip install -U "langgraph-cli[inmem]"

# Inicie o servidor LangGraph
langgraph dev
```

Após iniciar o servidor LangGraph, você verá vários URLs no terminal:

- API: <http://127.0.0.1:2024>
- Studio UI: <https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024>
- Documentação da API: <http://127.0.0.1:2024/docs>

Abra o link Studio UI no seu navegador para acessar a interface de depuração.

#### Usando LangGraph Studio

Na UI Studio, você pode:

1. Visualizar o grafo de fluxo de trabalho e ver como os componentes se conectam
2. Rastrear a execução em tempo real para entender como os dados fluem através do sistema
3. Inspecionar o status de cada etapa no fluxo de trabalho
4. Depurar problemas examinando a entrada e saída de cada componente
5. Fornecer feedback durante a fase de planejamento para refinar o plano de pesquisa

Quando você enviar um tópico de análise de dados na UI Studio, poderá ver todo o processo de execução do fluxo de trabalho, incluindo:

- A fase de planejamento onde o plano de análise de dados é criado
- Loops de feedback onde o plano pode ser modificado
- Fases de análise de dados para cada seção
- Geração do relatório final

### Habilitando Rastreamento LangSmith

DataNova suporta a funcionalidade de rastreamento LangSmith para ajudá-lo a depurar e monitorar fluxos de trabalho. Para habilitar o rastreamento LangSmith:

1. Certifique-se de ter a seguinte configuração no seu arquivo `.env` (veja `.env.example`):

   ```bash
   LANGSMITH_TRACING=true
   LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
   LANGSMITH_API_KEY="xxx"
   LANGSMITH_PROJECT="xxx"
   ```

2. Inicie o rastreamento LangSmith localmente executando:

   ```bash
   langgraph dev
   ```

Isso habilitará a visualização de rastreamento no LangGraph Studio e enviará seus rastros para o LangSmith para monitoramento e análise.

## Docker

Você também pode executar este projeto com Docker.

Primeiro, você precisa ler a [configuração](#configuração) abaixo. Certifique-se de que o arquivo `.env` esteja pronto.

Segundo, para construir uma imagem Docker do seu próprio servidor web:

```bash
docker build -t datanova-api .
```

Finalmente, inicie um contêiner docker executando o servidor web:

```bash
# Substitua datanova-api-app com seu nome de contêiner preferido
docker run -d -t -p 127.0.0.1:8000:8000 --env-file .env --name datanova-api-app datanova-api

# pare o servidor
docker stop datanova-api-app
```

### Docker Compose

Você também pode configurar este projeto com o docker compose:

```bash
# construindo imagem docker
docker compose build

# inicie o servidor
docker compose up
```

> [!WARNING]
> Se você deseja implantar o DataNova em um ambiente de produção, por favor adicione autenticação ao site e avalie as verificações de segurança para MCPServer e Python Repl.

## Exemplos

Os seguintes exemplos demonstram as capacidades do DataNova:

### Relatórios de Análise de Dados

1. **Design de Data Warehouse de E-commerce** - Design de esquema estrela para data warehouse de análise de e-commerce
   - Discute design de tabelas de fatos, tabelas de dimensões e melhores práticas de modelagem de dados
   - [Ver relatório completo](examples/ecommerce_data_warehouse_design.md)

2. **Estratégias de Otimização de Consultas SQL** - Otimização de desempenho de consultas SQL para grandes conjuntos de dados
   - Explora estratégias de indexação, reescrita de consultas e técnicas de otimização de custos
   - [Ver relatório completo](examples/sql_query_optimization.md)

3. **Construção de Pipeline de Dados em Tempo Real** - Construção de pipelines de dados em tempo real usando tecnologias de streaming modernas
   - Pesquisa Kafka, Spark Streaming e arquiteturas de processamento de dados em tempo real
   - [Ver relatório completo](examples/realtime_data_pipeline.md)

4. **Framework de Monitoramento de Qualidade de Dados** - Implementação de verificações automatizadas de qualidade de dados e monitoramento
   - Explora métricas de qualidade de dados, detecção de anomalias e estratégias de correção automatizadas
   - [Ver relatório completo](examples/data_quality_monitoring.md)

5. **O que é LLM?** - Uma exploração profunda de grandes modelos de linguagem
   - Discute arquitetura, treinamento, aplicações e considerações éticas
   - [Ver relatório completo](examples/what_is_llm.md)

6. **Como Usar Claude para Pesquisa Profunda?** - Melhores práticas e fluxos de trabalho para usar Claude em pesquisa profunda
   - Abrange engenharia de prompts, análise de dados e integração com outras ferramentas
   - [Ver relatório completo](examples/how_to_use_claude_deep_research.md)

7. **Adoção de IA na Saúde: Fatores Influentes** - Análise de fatores que influenciam a adoção de IA na saúde
   - Discute tecnologias de IA, qualidade de dados, considerações éticas, avaliação econômica, prontidão organizacional e infraestrutura digital
   - [Ver relatório completo](examples/AI_adoption_in_healthcare.md)

8. **Impacto da Computação Quântica na Criptografia** - Análise do impacto da computação quântica na criptografia

   - Discute vulnerabilidades da criptografia clássica, criptografia pós-quântica e soluções criptográficas resistentes a quântica
   - [Ver relatório completo](examples/Quantum_Computing_Impact_on_Cryptography.md)

9. **Destaques de Desempenho de Cristiano Ronaldo** - Análise dos destaques de desempenho de Cristiano Ronaldo
   - Discute suas conquistas profissionais, gols internacionais e desempenhos em várias competições
   - [Ver relatório completo](examples/Cristiano_Ronaldo's_Performance_Highlights.md)

Para executar esses exemplos ou criar seus próprios relatórios de pesquisa, você pode usar os seguintes comandos:

```bash
# Execute com uma consulta específica
uv run main.py "Projete uma arquitetura de data warehouse para análise de e-commerce"

# Execute com parâmetros de planejamento personalizados
uv run main.py --max_plan_iterations 3 "Como otimizar o desempenho de consultas SQL complexas?"

# Execute em modo interativo com perguntas integradas
uv run main.py --interactive

# Ou execute com prompt interativo básico
uv run main.py

# Veja todas as opções disponíveis
uv run main.py --help
```

### Modo Interativo

DataNova suporta um modo interativo com perguntas integradas em inglês e chinês, especificamente adaptadas para cenários de desenvolvimento de data warehouses:

1. Inicie o modo interativo:

   ```bash
   uv run main.py --interactive
   ```

2. Selecione seu idioma preferido (inglês ou chinês)

3. Escolha da lista de perguntas integradas sobre data warehouses ou selecione a opção para fazer sua própria pergunta

4. O sistema processará sua pergunta e gerará um relatório de análise de dados abrangente

### Humano no Loop

DataNova inclui um mecanismo humano no loop que permite revisar, editar e aprovar planos de análise de dados antes da execução:

1. **Revisão de Plano**: Quando o humano no loop está habilitado, o sistema mostrará o plano de análise de dados gerado antes da execução

2. **Fornecer Feedback**: Você pode:

   - Aceitar o plano respondendo `[ACCEPTED]`
   - Editar o plano fornecendo feedback (por exemplo, `[EDIT PLAN] Adicione mais etapas sobre verificações de qualidade de dados`)
   - O sistema incorporará seu feedback e gerará um plano revisado

3. **Aceitação Automática**: Você pode habilitar a aceitação automática para pular o processo de revisão:
   - Via API: Defina `auto_accepted_plan: true` na solicitação

4. **Integração API**: Ao usar a API, você pode fornecer feedback através do parâmetro `feedback`:

   ```json
   {
     "messages": [{ "role": "user", "content": "Projete uma arquitetura de data warehouse de e-commerce" }],
     "thread_id": "my_thread_id",
     "auto_accepted_plan": false,
     "feedback": "[EDIT PLAN] Inclua mais conteúdo sobre processamento de dados em tempo real"
   }
   ```

### Argumentos de Linha de Comando

DataNova suporta múltiplos argumentos de linha de comando para personalizar seu comportamento:

- **query**: A consulta de análise de dados a ser processada (pode ser várias palavras)
- **--interactive**: Executar em modo interativo com perguntas integradas
- **--max_plan_iterations**: Número máximo de ciclos de planejamento (padrão: 1)
- **--max_step_num**: Número máximo de etapas em um plano de análise de dados (padrão: 3)
- **--debug**: Habilitar registro detalhado de depuração

## FAQ

Consulte [FAQ.md](docs/FAQ.md) para mais detalhes.

## Licença

Este projeto é de código aberto e disponível sob a [Licença MIT](./LICENSE).

## Agradecimentos

Estendemos nossa sincera gratidão à comunidade de código aberto por suas contribuições inestimáveis.
DataNova é construído sobre a fundação desses projetos excepcionais:

Em particular, queremos expressar nossa profunda apreciação por:

- [LangChain](https://github.com/langchain-ai/langchain) por seu framework excepcional
- [LangGraph](https://github.com/langchain-ai/langgraph) por sua abordagem inovadora para orquestração multiagente

Esses projetos excepcionais formam a espinha dorsal do DataNova e exemplificam o poder transformador da colaboração de código aberto.

### Contribuidores-Chave

Estendemos nossa sincera gratidão aos autores principais do `DataNova` cuja visão, paixão e dedicação tornaram este projeto possível:

- **[Daniel Walnut](https://github.com/hetaoBackend/)**
- **[Henry Li](https://github.com/magiccube/)**

Seu compromisso inabalável e expertise são a força motriz por trás do sucesso do DataNova. Estamos honrados por tê-los liderando esta jornada.

## Histórico de Estrelas

[![Gráfico do Histórico de Estrelas](https://api.star-history.com/svg?repos=hszhsz/DataNova&type=Date)](https://star-history.com/#hszhsz/DataNova&Date)