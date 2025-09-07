# 🚀 DataNova

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[English](./README.md) | [简体中文](./README_zh.md) | [日本語](./README_ja.md) | [Deutsch](./README_de.md) | [Español](./README_es.md) | [Русский](./README_ru.md) |[Portuguese](./README_pt.md)

> Revolutionizing data warehouse development with AI intelligence.

**DataNova** is an AI-powered data warehouse development platform that combines large language models with specialized tools to provide intelligent data architecture design, query optimization, and automated pipeline generation capabilities for data teams. Our goal is to transform traditional data warehouse development through AI-driven insights and recommendations.

DataNova is now officially available on [Volcengine's FaaS Application Center](https://console.volcengine.com/vefaas/region:vefaas+cn-beijing/market), where users can experience its powerful features and convenient operations through the [experience link](https://console.volcengine.com/vefaas/region:vefaas+cn-beijing/market/datanova/?channel=github&source=datanova). At the same time, to meet the deployment needs of different users, DataNova supports one-click deployment based on Volcengine. Click the [deployment link](https://console.volcengine.com/vefaas/region:vefaas+cn-beijing/application/create?templateId=683adf9e372daa0008aaed5c&channel=github&source=datanova) to quickly complete the deployment process and start your intelligent data warehouse development journey.

Please visit [DataNova's official website](https://datanova.tech/) for more details.

## Demo

### Video

<https://github.com/user-attachments/assets/f3786598-1f2a-4d07-919e-8b99dfa1de3e>

In this demo, we showcase how to use DataNova:

- Seamless integration with MCP services
- Conducting in-depth data analysis processes and generating comprehensive reports with charts
- Creating podcast audio based on generated analysis reports

### Replay Examples

- [Designing a star schema for e-commerce data warehouse](https://datanova.tech/chat?replay=ecommerce-star-schema-design)
- [Optimizing performance of complex SQL queries](https://datanova.tech/chat?replay=sql-query-optimization)
- [Building real-time data pipelines to process streaming data](https://datanova.tech/chat?replay=realtime-data-pipeline)
- [Implementing data quality monitoring and alerting systems](https://datanova.tech/chat?replay=data-quality-monitoring)
- [Visit our official website to explore more replay examples.](https://datanova.tech/#case-studies)

---

## 📑 Table of Contents

- [🚀 Quick Start](#quick-start)
- [🌟 Features](#features)
- [🏗️ Architecture](#architecture)
- [🛠️ Development](#development)
- [🗣️ Text-to-Speech Integration](#text-to-speech-integration)
- [📚 Examples](#examples)
- [❓ FAQ](#faq)
- [📜 License](#license)
- [💖 Acknowledgements](#acknowledgements)
- [⭐ Star History](#star-history)

## Quick Start

DataNova is developed in Python and comes with a Web UI written in Node.js. To ensure a smooth setup process, we recommend using the following tools:

### Recommended Tools

- **[`uv`](https://docs.astral.sh/uv/getting-started/installation/):**
  Simplifies Python environment and dependency management. `uv` will automatically create a virtual environment in the root directory and install all required packages for you—no need to manually install Python environments.

- **[`nvm`](https://github.com/nvm-sh/nvm):**
  Easily manage multiple Node.js runtime versions.

- **[`pnpm`](https://pnpm.io/installation):**
  Install and manage dependencies for Node.js projects.

### Environment Requirements

Ensure your system meets the following minimum requirements:

- **[Python](https://www.python.org/downloads/):** Version `3.12+`
- **[Node.js](https://nodejs.org/en/download/):** Version `22+`

### Installation

```bash
# Clone the repository
git clone https://github.com/hszhsz/DataNova
cd DataNova

# Install dependencies, uv will handle the creation of Python interpreter and virtual environment, and install the required packages
uv sync

# Configure .env with your API keys
# Tavily: https://app.tavily.com/home
# Brave_SEARCH: https://brave.com/search/api/
# Volcengine TTS: Add if you have TTS credentials
cp .env.example .env

# See the "Supported Search Engines" and "Text-to-Speech Integration" sections below for all available options

# Configure conf.yaml with your LLM models and API keys
# See 'docs/configuration_guide.md' for more details
cp conf.yaml.example conf.yaml

# Install marp for PPT generation
# https://github.com/marp-team/marp-cli?tab=readme-ov-file#use-package-manager
brew install marp-cli
```

Optionally, install Web UI dependencies via [pnpm](https://pnpm.io/installation):

```bash
cd DataNova/web
pnpm install
```

### Configuration

See [Configuration Guide](docs/configuration_guide.md) for more details.

> [!NOTE]
> Please read the guide carefully before starting the project and update the configuration to match your specific settings and requirements.

### Console UI

The fastest way to run the project is using the console UI.

```bash
# Run the project in a bash-like shell
uv run main.py
```

### Web UI

This project also includes a Web UI that provides a more dynamic and engaging interactive experience.
> [!NOTE]
> You need to install the Web UI dependencies first.

```bash
# Run both backend and frontend servers in development mode
# On macOS/Linux
./bootstrap.sh -d

# On Windows
bootstrap.bat -d
```

Open your browser and visit [`http://localhost:3000`](http://localhost:3000) to explore the Web UI.

Explore more details in the [`web`](./web/) directory.

## Supported Search Engines

### Public Domain Search Engines

DataNova supports multiple search engines that can be configured in the `.env` file through the `SEARCH_API` variable:

- **Tavily** (default): Professional search API designed for AI applications
  - Requires setting `TAVILY_API_KEY` in the `.env` file
  - Registration address: <https://app.tavily.com/home>

- **DuckDuckGo**: Privacy-focused search engine
  - No API key required

- **Brave Search**: Privacy-focused search engine with advanced features
  - Requires setting `BRAVE_SEARCH_API_KEY` in the `.env` file
  - Registration address: <https://brave.com/search/api/>

- **Arxiv**: Scientific paper search for academic research
  - No API key required
  - Designed specifically for scientific and academic papers

To configure your preferred search engine, set the `SEARCH_API` variable in the `.env` file:

```bash
# Choose one: tavily, duckduckgo, brave_search, arxiv
SEARCH_API=tavily
```

### Private Knowledge Base Engines

DataNova supports retrieval based on private domain knowledge. You can upload documents to multiple private knowledge bases for use during data analysis. Currently supported private knowledge bases include:

- **[RAGFlow](https://ragflow.io/docs/dev/)**: Open-source knowledge base engine based on Retrieval-Augmented Generation
   ```
   # Refer to .env.example for configuration
   RAG_PROVIDER=ragflow
   RAGFLOW_API_URL="http://localhost:9388"
   RAGFLOW_API_KEY="ragflow-xxx"
   RAGFLOW_RETRIEVAL_SIZE=10
   ```

- **[VikingDB Knowledge Base](https://www.volcengine.com/docs/84313/1254457)**: Public cloud knowledge base engine provided by Volcengine
   > Note: First obtain account AK/SK from [Volcengine](https://www.volcengine.com/docs/84313/1254485)
   ```
   # Refer to .env.example for configuration
   RAG_PROVIDER=vikingdb_knowledge_base
   VIKINGDB_KNOWLEDGE_BASE_API_URL="api-knowledgebase.mlp.cn-beijing.volces.com"
   VIKINGDB_KNOWLEDGE_BASE_API_AK="volcengine-ak-xxx"
   VIKINGDB_KNOWLEDGE_BASE_API_SK="volcengine-sk-xxx"
   VIKINGDB_KNOWLEDGE_BASE_RETRIEVAL_SIZE=15
   ```

## Features

### Core Capabilities

- 🤖 **AI-Powered Data Architecture Design**
  - Supports integration of most models through [litellm](https://docs.litellm.ai/docs/providers)
  - Supports open-source models like Qwen
  - Compatible with OpenAI API interface
  - Multi-layer LLM system for tasks of different complexities

### Data Tools and MCP Integration

- 🔍 **Data Exploration and Retrieval**
  - Data source search through Tavily, Brave Search, and others
  - Data crawling using Jina
  - Advanced data content extraction
  - Supports retrieval of specified private knowledge bases

- 📃 **RAG Integration**
  - Supports [RAGFlow](https://github.com/infiniflow/ragflow) knowledge base
  - Supports [VikingDB](https://www.volcengine.com/docs/84313/1254457) Volcengine knowledge base

- 🔗 **MCP Seamless Integration**
  - Extends capabilities for data source access, data quality checks, query optimization, and more
  - Promotes integration of diverse data tools and methodologies

### AI-Powered Collaboration

- 🧠 **Human-in-the-Loop**
  - Supports interactive modification of data architecture plans using natural language
  - Supports automatic acceptance of architecture plans

- 📝 **Data Report Post-Editing**
  - Supports Notion-like block editing
  - Allows AI optimization, including AI-assisted polishing, sentence shortening, and expansion
  - Powered by [tiptap](https://tiptap.dev/)

### Content Creation

- 🎙️ **Podcast and Presentation Generation**
  - AI-powered podcast script generation and audio synthesis
  - Automatic creation of simple PowerPoint presentations
  - Customizable templates to meet personalized content needs

## Architecture

DataNova implements a modular multi-agent system architecture designed for automated data warehouse development and data analysis. The system is built on LangGraph, implementing a flexible state-based workflow where components communicate through a well-defined message passing system.

![Architecture Diagram](./assets/architecture.png)

> View live demo at [datanova.tech](https://datanova.tech/#multi-agent-architecture)

The system employs a streamlined workflow consisting of the following components:

1. **Coordinator**: The entry point managing the workflow lifecycle

   - Initiates the data analysis process based on user input
   - Delegates tasks to the planner at appropriate times
   - Serves as the main interface between the user and the system

2. **Planner**: The strategic component responsible for task decomposition and planning

   - Analyzes data analysis goals and creates structured execution plans
   - Determines if there is sufficient context or if more data exploration is needed
   - Manages the data analysis process and decides when to generate the final report

3. **Data Analysis Team**: A collection of specialized agents that execute the plan:
   - **Data Analyst**: Conducts data search and information gathering using tools such as data search engines, crawlers, and even MCP services.
   - **Data Engineer**: Handles data processing, analysis, and technical tasks using Python REPL tools.
   Each agent has access to specific tools optimized for their role and operates within the LangGraph framework

4. **Reporter**: The final stage processor for data analysis outputs
   - Aggregates findings from the data analysis team
   - Processes and organizes collected information
   - Generates comprehensive data analysis reports

## Text-to-Speech Integration

DataNova now includes a text-to-speech (TTS) feature that allows you to convert research reports to audio. This feature uses the Volcengine TTS API to generate high-quality text audio. Characteristics such as speed, volume, and pitch can also be customized.

### Using the TTS API

You can access the TTS feature through the `/api/tts` endpoint:

```bash
# Example API call using curl
curl --location 'http://localhost:8000/api/tts' \
--header 'Content-Type: application/json' \
--data '{
    "text": "This is a test of the text-to-speech feature.",
    "speed_ratio": 1.0,
    "volume_ratio": 1.0,
    "pitch_ratio": 1.0
}' \
--output speech.mp3
```

## Development

### Testing

Run the test suite:

```bash
# Run all tests
make test

# Run specific test files
pytest tests/integration/test_workflow.py

# Run coverage tests
make coverage
```

### Code Quality

```bash
# Run code linting
make lint

# Format code
make format
```

### Debugging with LangGraph Studio

DataNova uses LangGraph as its workflow architecture. You can use LangGraph Studio to debug and visualize workflows in real-time.

#### Running LangGraph Studio Locally

DataNova includes a `langgraph.json` configuration file that defines the graph structure and dependencies for LangGraph Studio. This file points to the workflow graph defined in the project and automatically loads environment variables from the `.env` file.

##### Mac

```bash
# Install uv package manager if you don't have it
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies and start the LangGraph server
uvx --refresh --from "langgraph-cli[inmem]" --with-editable . --python 3.12 langgraph dev --allow-blocking
```

##### Windows / Linux

```bash
# Install dependencies
pip install -e .
pip install -U "langgraph-cli[inmem]"

# Start the LangGraph server
langgraph dev
```

After starting the LangGraph server, you will see several URLs in the terminal:

- API: <http://127.0.0.1:2024>
- Studio UI: <https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024>
- API Documentation: <http://127.0.0.1:2024/docs>

Open the Studio UI link in your browser to access the debugging interface.

#### Using LangGraph Studio

In the Studio UI, you can:

1. Visualize the workflow graph and see how components connect
2. Track execution in real-time to understand how data flows through the system
3. Inspect the status of each step in the workflow
4. Debug issues by examining the input and output of each component
5. Provide feedback during the planning phase to refine the research plan

When you submit a data analysis topic in the Studio UI, you will be able to see the entire workflow execution process, including:

- The planning phase where the data analysis plan is created
- Feedback loops where the plan can be modified
- Data analysis phases for each section
- Final report generation

### Enabling LangSmith Tracing

DataNova supports LangSmith tracing functionality to help you debug and monitor workflows. To enable LangSmith tracing:

1. Ensure you have the following configuration in your `.env` file (see `.env.example`):

   ```bash
   LANGSMITH_TRACING=true
   LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
   LANGSMITH_API_KEY="xxx"
   LANGSMITH_PROJECT="xxx"
   ```

2. Start LangSmith tracing locally by running:

   ```bash
   langgraph dev
   ```

This will enable tracing visualization in LangGraph Studio and send your traces to LangSmith for monitoring and analysis.

## Docker

You can also run this project using Docker.

First, you need to read the [Configuration](#configuration) section below. Make sure the `.env` and `.conf.yaml` files are ready.

Next, build your own Web server Docker image:

```bash
docker build -t datanova-api .
```

Finally, start the Docker container running the Web server:

```bash
# Replace datanova-api-app with your preferred container name
# Start the server and bind to localhost:8000
docker run -d -t -p 127.0.0.1:8000:8000 --env-file .env --name datanova-api-app datanova-api

# Stop the server
docker stop datanova-api-app
```

### Docker Compose

You can also set up this project using docker compose:

```bash
# Build docker images
docker compose build

# Start the server
docker compose up
```

> [!WARNING]
> If you want to deploy DataNova to a production environment, please add authentication to the website and evaluate the security checks for MCPServer and Python Repl.

## Examples

The following examples showcase DataNova's capabilities:

### Data Analysis Reports

1. **E-commerce Data Warehouse Design** - Star schema design for e-commerce analytics data warehouse
   - Discusses fact table, dimension table design, and data modeling best practices
   - [View full report](examples/ecommerce_data_warehouse_design.md)

2. **SQL Query Optimization Strategies** - SQL query performance optimization for large datasets
   - Explores indexing strategies, query rewriting, and cost optimization techniques
   - [View full report](examples/sql_query_optimization.md)

3. **Real-time Data Pipeline Construction** - Building real-time data pipelines using modern streaming technologies
   - Researches Kafka, Spark Streaming, and real-time data processing architectures
   - [View full report](examples/realtime_data_pipeline.md)

4. **Data Quality Monitoring Framework** - Implementing automated data quality checks and monitoring
   - Explores data quality metrics, anomaly detection, and automated remediation strategies
   - [View full report](examples/data_quality_monitoring.md)

5. **What is LLM?** - An in-depth exploration of large language models
   - Discusses architecture, training, applications, and ethical considerations
   - [View full report](examples/what_is_llm.md)

6. **How to Use Claude for Deep Research?** - Best practices and workflows for using Claude in deep research
   - Covers prompt engineering, data analysis, and integration with other tools
   - [View full report](examples/how_to_use_claude_deep_research.md)

7. **AI Adoption in Healthcare: Influencing Factors** - Analysis of factors influencing AI adoption in healthcare
   - Discusses AI technologies, data quality, ethical considerations, economic evaluation, organizational readiness, and digital infrastructure
   - [View full report](examples/AI_adoption_in_healthcare.md)

8. **Quantum Computing's Impact on Cryptography** - Analysis of quantum computing's impact on cryptography

   - Discusses vulnerabilities of classical cryptography, post-quantum cryptography, and quantum-resistant cryptographic solutions
   - [View full report](examples/Quantum_Computing_Impact_on_Cryptography.md)

9. **Cristiano Ronaldo's Performance Highlights** - Analysis of Cristiano Ronaldo's performance highlights
   - Discusses his career achievements, international goals, and performances in various competitions
   - [View full report](examples/Cristiano_Ronaldo's_Performance_Highlights.md)

To run these examples or create your own research reports, you can use the following commands:

```bash
# Run with a specific query
uv run main.py "Design a data warehouse architecture for e-commerce analytics"

# Run with custom planning parameters
uv run main.py --max_plan_iterations 3 "How to optimize performance of complex SQL queries?"

# Run in interactive mode with built-in questions
uv run main.py --interactive

# Or run with basic interactive prompt
uv run main.py

# View all available options
uv run main.py --help
```

### Interactive Mode

DataNova supports an interactive mode with built-in questions in both English and Chinese, specifically tailored for data warehouse development scenarios:

1. Start interactive mode:

   ```bash
   uv run main.py --interactive
   ```

2. Select your preferred language (English or Chinese)

3. Choose from the built-in data warehouse question list or select the option to ask your own question

4. The system will process your question and generate a comprehensive data analysis report

### Human-in-the-Loop

DataNova includes a human-in-the-loop mechanism that allows you to review, edit, and approve before executing data analysis plans:

1. **Plan Review**: When human-in-the-loop is enabled, the system will show you the generated data analysis plan before execution

2. **Provide Feedback**: You can:

   - Accept the plan by replying `[ACCEPTED]`
   - Edit the plan by providing feedback (e.g., `[EDIT PLAN] Add more steps about data quality checks`)
   - The system will incorporate your feedback and generate a revised plan

3. **Automatic Acceptance**: You can enable automatic acceptance to skip the review process:
   - Via API: Set `auto_accepted_plan: true` in the request

4. **API Integration**: When using the API, you can provide feedback through the `feedback` parameter:

   ```json
   {
     "messages": [{ "role": "user", "content": "Design an e-commerce data warehouse architecture" }],
     "thread_id": "my_thread_id",
     "auto_accepted_plan": false,
     "feedback": "[EDIT PLAN] Include more content about real-time data processing"
   }
   ```

### Command Line Arguments

DataNova supports multiple command line arguments to customize its behavior:

- **query**: The data analysis query to process (can be multiple words)
- **--interactive**: Run in interactive mode with built-in questions
- **--max_plan_iterations**: Maximum number of planning cycles (default: 1)
- **--max_step_num**: Maximum number of steps in a data analysis plan (default: 3)
- **--debug**: Enable verbose debug logging

## FAQ

See [FAQ.md](docs/FAQ.md) for more details.

## License

This project is open source under the [MIT License](./LICENSE).

## Acknowledgements

DataNova is built upon the outstanding work of the open-source community. We deeply appreciate all the projects and contributors that made DataNova possible. Indeed, we stand on the shoulders of giants.

We would like to express our sincere gratitude to the following projects for their valuable contributions:

- **[LangChain](https://github.com/langchain-ai/langchain)**: Their excellent framework powers our LLM interactions and chains, enabling seamless integration and functionality.
- **[LangGraph](https://github.com/langchain-ai/langgraph)**: Their innovative approach to multi-agent orchestration is crucial for implementing DataNova's complex workflows.

These projects demonstrate the transformative power of open-source collaboration, and we are proud to build upon their foundations.

### Core Contributors

We extend our heartfelt thanks to the core authors of `DataNova` whose vision, passion, and dedication made this project possible:

- **[Daniel Walnut](https://github.com/hetaoBackend/)**
- **[Henry Li](https://github.com/magiccube/)**

Your unwavering commitment and expertise are the driving force behind DataNova's success. We are honored to have you lead this journey.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=hszhsz/DataNova&type=Date)](https://star-history.com/#hszhsz/DataNova&Date)