# 🚀 DataNova

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[English](./README.md) | [简体中文](./README_zh.md) | [日本語](./README_ja.md) | [Deutsch](./README_de.md) | [Español](./README_es.md) | [Русский](./README_ru.md) |[Portuguese](./README_pt.md)

> Revolucionando el desarrollo de almacenes de datos con inteligencia artificial

**DataNova** es una plataforma de desarrollo de almacenes de datos impulsada por IA que combina modelos de lenguaje grandes con herramientas especializadas para proporcionar a los equipos de datos capacidades inteligentes de diseño de arquitectura de datos, optimización de consultas y generación automatizada de pipelines. Nuestro objetivo es transformar el desarrollo tradicional de almacenes de datos a través de insights y recomendaciones impulsadas por IA.

DataNova ahora está oficialmente disponible en el [Centro de Aplicaciones FaaS de Volcengine](https://console.volcengine.com/vefaas/region:vefaas+cn-beijing/market), donde los usuarios pueden experimentar sus potentes funciones y operaciones convenientes a través del [enlace de experiencia](https://console.volcengine.com/vefaas/region:vefaas+cn-beijing/market/datanova/?channel=github&source=datanova). Al mismo tiempo, para satisfacer las necesidades de implementación de diferentes usuarios, DataNova admite implementación con un solo clic basada en Volcengine. Haga clic en el [enlace de implementación](https://console.volcengine.com/vefaas/region:vefaas+cn-beijing/application/create?templateId=683adf9e372daa0008aaed5c&channel=github&source=datanova) para completar rápidamente el proceso de implementación y comenzar su viaje de desarrollo inteligente de almacenes de datos.

Por favor, visite el [sitio web oficial de DataNova](https://datanova.tech/) para más detalles.

## Demo

### Video

<https://github.com/user-attachments/assets/f3786598-1f2a-4d07-919e-8b99dfa1de3e>

En esta demostración, mostramos cómo usar DataNova:

- Integración perfecta con servicios MCP
- Realización de procesos de análisis de datos profundos y generación de informes completos con gráficos
- Creación de audio de podcast basado en informes de análisis generados

### Ejemplos de reproducción

- [Diseño de esquema estrella para almacén de datos de comercio electrónico](https://datanova.tech/chat?replay=ecommerce-star-schema-design)
- [Optimización del rendimiento de consultas SQL complejas](https://datanova.tech/chat?replay=sql-query-optimization)
- [Construcción de pipelines de datos en tiempo real para procesar datos de streaming](https://datanova.tech/chat?replay=realtime-data-pipeline)
- [Implementación de monitoreo de calidad de datos y sistemas de alerta](https://datanova.tech/chat?replay=data-quality-monitoring)
- [Visite nuestro sitio web oficial para explorar más ejemplos de reproducción.](https://datanova.tech/#case-studies)

---

## 📑 Tabla de contenidos

- [🚀 Inicio rápido](#inicio-rápido)
- [🌟 Características](#características)
- [🏗️ Arquitectura](#arquitectura)
- [🛠️ Desarrollo](#desarrollo)
- [🗣️ Integración de texto a voz](#integración-de-texto-a-voz)
- [📚 Ejemplos](#ejemplos)
- [❓ Preguntas frecuentes](#preguntas-frecuentes)
- [📜 Licencia](#licencia)
- [💖 Agradecimientos](#agradecimientos)
- [⭐ Historial de estrellas](#historial-de-estrellas)

## Inicio rápido

DataNova está desarrollado en Python y viene con una interfaz web escrita en Node.js. Para garantizar un proceso de configuración fluido, recomendamos usar las siguientes herramientas:

### Herramientas recomendadas

- **[`uv`](https://docs.astral.sh/uv/getting-started/installation/):**
  Simplifica la gestión del entorno Python y las dependencias. `uv` creará automáticamente un entorno virtual en el directorio raíz e instalará todos los paquetes necesarios para usted—no es necesario instalar manualmente entornos Python.

- **[`nvm`](https://github.com/nvm-sh/nvm):**
  Administre fácilmente múltiples versiones de tiempo de ejecución de Node.js.

- **[`pnpm`](https://pnpm.io/installation):**
  Instale y administre dependencias para proyectos Node.js.

### Requisitos del entorno

Asegúrese de que su sistema cumpla con los siguientes requisitos mínimos:

- **[Python](https://www.python.org/downloads/):** Versión `3.12+`
- **[Node.js](https://nodejs.org/en/download/):** Versión `22+`

### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/hszhsz/DataNova
cd DataNova

# Instalar dependencias, uv se encargará de la creación del intérprete Python y el entorno virtual, e instalará los paquetes requeridos
uv sync

# Configurar .env con sus claves API
# Tavily: https://app.tavily.com/home
# Brave_SEARCH: https://brave.com/search/api/
# Volcengine TTS: Agregue si tiene credenciales TTS
cp .env.example .env

# Vea las secciones "Motores de búsqueda compatibles" e "Integración de texto a voz" a continuación para todas las opciones disponibles

# Configure conf.yaml con sus modelos LLM y claves API
# Vea 'docs/configuration_guide.md' para más detalles
cp conf.yaml.example conf.yaml

# Instale marp para generación de PPT
# https://github.com/marp-team/marp-cli?tab=readme-ov-file#use-package-manager
brew install marp-cli
```

Opcionalmente, instale las dependencias de la interfaz web a través de [pnpm](https://pnpm.io/installation):

```bash
cd DataNova/web
pnpm install
```

### Configuración

Vea la [Guía de configuración](docs/configuration_guide.md) para más detalles.

> [!NOTE]
> Por favor, lea la guía cuidadosamente antes de iniciar el proyecto y actualice la configuración para que coincida con sus configuraciones y requisitos específicos.

### Interfaz de consola

La forma más rápida de ejecutar el proyecto es usando la interfaz de consola.

```bash
# Ejecute el proyecto en un shell similar a bash
uv run main.py
```

### Interfaz web

Este proyecto también incluye una interfaz web que proporciona una experiencia interactiva más dinámica y atractiva.
> [!NOTE]
> Primero necesita instalar las dependencias de la interfaz web.

```bash
# Ejecute servidores backend y frontend simultáneamente en modo de desarrollo
# En macOS/Linux
./bootstrap.sh -d

# En Windows
bootstrap.bat -d
```

Abra su navegador y visite [`http://localhost:3000`](http://localhost:3000) para explorar la interfaz web.

Explore más detalles en el directorio [`web`](./web/).

## Motores de búsqueda compatibles

### Motores de búsqueda de dominio público

DataNova admite múltiples motores de búsqueda que se pueden configurar en el archivo `.env` a través de la variable `SEARCH_API`:

- **Tavily** (predeterminado): API de búsqueda profesional diseñada para aplicaciones de IA
  - Requiere establecer `TAVILY_API_KEY` en el archivo `.env`
  - Dirección de registro: <https://app.tavily.com/home>

- **DuckDuckGo**: Motor de búsqueda enfocado en la privacidad
  - No se requiere clave API

- **Brave Search**: Motor de búsqueda enfocado en la privacidad con funciones avanzadas
  - Requiere establecer `BRAVE_SEARCH_API_KEY` en el archivo `.env`
  - Dirección de registro: <https://brave.com/search/api/>

- **Arxiv**: Búsqueda de artículos científicos para investigación académica
  - No se requiere clave API
  - Diseñado específicamente para artículos científicos y académicos

Para configurar su motor de búsqueda preferido, establezca la variable `SEARCH_API` en el archivo `.env`:

```bash
# Elija uno: tavily, duckduckgo, brave_search, arxiv
SEARCH_API=tavily
```

### Motores de bases de conocimiento privadas

DataNova admite recuperación basada en conocimiento de dominio privado. Puede cargar documentos en múltiples bases de conocimiento privadas para usar durante el análisis de datos. Las bases de conocimiento privadas actualmente compatibles incluyen:

- **[RAGFlow](https://ragflow.io/docs/dev/)**: Motor de base de conocimiento de código abierto basado en Generación Aumentada por Recuperación
   ```
   # Consulte .env.example para la configuración
   RAG_PROVIDER=ragflow
   RAGFLOW_API_URL="http://localhost:9388"
   RAGFLOW_API_KEY="ragflow-xxx"
   RAGFLOW_RETRIEVAL_SIZE=10
   ```

- **[Base de conocimiento VikingDB](https://www.volcengine.com/docs/84313/1254457)**: Motor de base de conocimiento en la nube pública proporcionado por Volcengine
   > Nota: Primero obtenga AK/SK de [Volcengine](https://www.volcengine.com/docs/84313/1254485)
   ```
   # Consulte .env.example para la configuración
   RAG_PROVIDER=vikingdb_knowledge_base
   VIKINGDB_KNOWLEDGE_BASE_API_URL="api-knowledgebase.mlp.cn-beijing.volces.com"
   VIKINGDB_KNOWLEDGE_BASE_API_AK="volcengine-ak-xxx"
   VIKINGDB_KNOWLEDGE_BASE_API_SK="volcengine-sk-xxx"
   VIKINGDB_KNOWLEDGE_BASE_RETRIEVAL_SIZE=15
   ```

## Características

### Capacidades principales

- 🤖 **Diseño de arquitectura de datos impulsado por IA**
  - Admite la integración de la mayoría de los modelos a través de [litellm](https://docs.litellm.ai/docs/providers)
  - Admite modelos de código abierto como Qwen
  - Compatible con la interfaz API de OpenAI
  - Sistema LLM multicapa para tareas de diferentes complejidades

### Herramientas de datos e integración MCP

- 🔍 **Exploración y recuperación de datos**
  - Búsqueda de fuentes de datos a través de Tavily, Brave Search y otros
  - Rastreo de datos usando Jina
  - Extracción avanzada de contenido de datos
  - Admite recuperación de bases de conocimiento privadas especificadas

- 📃 **Integración RAG**
  - Admite base de conocimiento [RAGFlow](https://github.com/infiniflow/ragflow)
  - Admite base de conocimiento [VikingDB](https://www.volcengine.com/docs/84313/1254457) de Volcengine

- 🔗 **Integración perfecta MCP**
  - Amplía capacidades para acceso a fuentes de datos, verificación de calidad de datos, optimización de consultas y más
  - Promueve la integración de diversas herramientas y metodologías de datos

### Colaboración impulsada por IA

- 🧠 **Human-in-the-Loop**
  - Admite modificación interactiva de planes de arquitectura de datos usando lenguaje natural
  - Admite aceptación automática de planes de arquitectura

- 📝 **Edición posterior de informes de datos**
  - Admite edición de bloques similar a Notion
  - Permite optimización de IA, incluyendo pulido asistido por IA, acortamiento y expansión de oraciones
  - Impulsado por [tiptap](https://tiptap.dev/)

### Creación de contenido

- 🎙️ **Generación de podcasts y presentaciones**
  - Generación de guiones de podcast y síntesis de audio impulsados por IA
  - Creación automática de presentaciones PowerPoint simples
  - Plantillas personalizables para satisfacer necesidades de contenido personalizadas

## Arquitectura

DataNova implementa una arquitectura de sistema multiagente modular diseñada para desarrollo automatizado de almacenes de datos y análisis de datos. El sistema está construido sobre LangGraph, implementando un flujo de trabajo basado en estado flexible donde los componentes se comunican a través de un sistema de paso de mensajes claramente definido.

![Diagrama de arquitectura](./assets/architecture.png)

> Ver demostración en vivo en [datanova.tech](https://datanova.tech/#multi-agent-architecture)

El sistema emplea un flujo de trabajo optimizado que consiste en los siguientes componentes:

1. **Coordinador**: El punto de entrada que gestiona el ciclo de vida del flujo de trabajo

   - Inicia el proceso de análisis de datos basado en la entrada del usuario
   - Delega tareas al planificador en momentos apropiados
   - Sirve como interfaz principal entre el usuario y el sistema

2. **Planificador**: El componente estratégico responsable de la descomposición y planificación de tareas

   - Analiza los objetivos de análisis de datos y crea planes de ejecución estructurados
   - Determina si hay suficiente contexto o si se necesita más exploración de datos
   - Gestiona el proceso de análisis de datos y decide cuándo generar el informe final

3. **Equipo de análisis de datos**: Una colección de agentes especializados que ejecutan el plan:
   - **Analista de datos**: Realiza búsqueda de datos y recopilación de información usando herramientas como motores de búsqueda de datos, rastreadores e incluso servicios MCP.
   - **Ingeniero de datos**: Maneja el procesamiento de datos, análisis y tareas técnicas usando herramientas REPL de Python.
   Cada agente tiene acceso a herramientas específicas optimizadas para su rol y opera dentro del marco LangGraph

4. **Reportero**: El procesador de etapa final para las salidas de análisis de datos
   - Agrega hallazgos del equipo de análisis de datos
   - Procesa y organiza la información recopilada
   - Genera informes de análisis de datos completos

## Integración de texto a voz

DataNova ahora incluye una función de texto a voz (TTS) que le permite convertir informes de investigación en audio. Esta función usa la API TTS de Volcengine para generar audio de texto de alta calidad. Características como velocidad, volumen y tono también se pueden personalizar.

### Usando la API TTS

Puede acceder a la función TTS a través del endpoint `/api/tts`:

```bash
# Ejemplo de llamada API usando curl
curl --location 'http://localhost:8000/api/tts' \
--header 'Content-Type: application/json' \
--data '{
    "text": "Esta es una prueba de la función de texto a voz.",
    "speed_ratio": 1.0,
    "volume_ratio": 1.0,
    "pitch_ratio": 1.0
}' \
--output speech.mp3
```

## Desarrollo

### Pruebas

Ejecute la suite de pruebas:

```bash
# Ejecute todas las pruebas
make test

# Ejecute archivos de prueba específicos
pytest tests/integration/test_workflow.py

# Ejecute pruebas de cobertura
make coverage
```

### Calidad del código

```bash
# Ejecute linting de código
make lint

# Formatee el código
make format
```

### Depuración con LangGraph Studio

DataNova usa LangGraph como su arquitectura de flujo de trabajo. Puede usar LangGraph Studio para depurar y visualizar flujos de trabajo en tiempo real.

#### Ejecutando LangGraph Studio localmente

DataNova incluye un archivo de configuración `langgraph.json` que define la estructura del grafo y las dependencias para LangGraph Studio. Este archivo apunta al grafo de flujo de trabajo definido en el proyecto y carga automáticamente variables de entorno del archivo `.env`.

##### Mac

```bash
# Instale el administrador de paquetes uv si no lo tiene
curl -LsSf https://astral.sh/uv/install.sh | sh

# Instale dependencias e inicie el servidor LangGraph
uvx --refresh --from "langgraph-cli[inmem]" --with-editable . --python 3.12 langgraph dev --allow-blocking
```

##### Windows / Linux

```bash
# Instale dependencias
pip install -e .
pip install -U "langgraph-cli[inmem]"

# Inicie el servidor LangGraph
langgraph dev
```

Después de iniciar el servidor LangGraph, verá varias URLs en la terminal:

- API: <http://127.0.0.1:2024>
- Studio UI: <https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024>
- Documentación de API: <http://127.0.0.1:2024/docs>

Abra el enlace Studio UI en su navegador para acceder a la interfaz de depuración.

#### Usando LangGraph Studio

En la interfaz Studio, puede:

1. Visualizar el grafo de flujo de trabajo y ver cómo se conectan los componentes
2. Rastrear la ejecución en tiempo real para entender cómo fluyen los datos a través del sistema
3. Inspeccionar el estado de cada paso en el flujo de trabajo
4. Depurar problemas examinando la entrada y salida de cada componente
5. Proporcionar retroalimentación durante la fase de planificación para refinar el plan de investigación

Cuando envíe un tema de análisis de datos en la interfaz Studio, podrá ver todo el proceso de ejecución del flujo de trabajo, incluyendo:

- La fase de planificación donde se crea el plan de análisis de datos
- Bucles de retroalimentación donde se puede modificar el plan
- Fases de análisis de datos para cada sección
- Generación del informe final

### Habilitando el rastreo LangSmith

DataNova admite la funcionalidad de rastreo LangSmith para ayudarle a depurar y monitorear flujos de trabajo. Para habilitar el rastreo LangSmith:

1. Asegúrese de tener la siguiente configuración en su archivo `.env` (vea `.env.example`):

   ```bash
   LANGSMITH_TRACING=true
   LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
   LANGSMITH_API_KEY="xxx"
   LANGSMITH_PROJECT="xxx"
   ```

2. Inicie el rastreo LangSmith localmente ejecutando:

   ```bash
   langgraph dev
   ```

Esto habilitará la visualización de rastreo en LangGraph Studio y enviará sus rastros a LangSmith para monitoreo y análisis.

## Docker

También puede ejecutar este proyecto usando Docker.

Primero, necesita leer la sección [Configuración](#configuración) a continuación. Asegúrese de que los archivos `.env` y `.conf.yaml` estén listos.

A continuación, construya su propia imagen Docker del servidor web:

```bash
docker build -t datanova-api .
```

Finalmente, inicie el contenedor Docker que ejecuta el servidor web:

```bash
# Reemplace datanova-api-app con su nombre de contenedor preferido
# Inicie el servidor y enlácelo a localhost:8000
docker run -d -t -p 127.0.0.1:8000:8000 --env-file .env --name datanova-api-app datanova-api

# Detenga el servidor
docker stop datanova-api-app
```

### Docker Compose

También puede configurar este proyecto usando docker compose:

```bash
# Construya imágenes docker
docker compose build

# Inicie el servidor
docker compose up
```

> [!WARNING]
> Si desea implementar DataNova en un entorno de producción, por favor agregue autenticación al sitio web y evalúe las verificaciones de seguridad para MCPServer y Python Repl.

## Ejemplos

Los siguientes ejemplos muestran las capacidades de DataNova:

### Informes de análisis de datos

1. **Diseño de almacén de datos de comercio electrónico** - Diseño de esquema estrella para almacén de datos de análisis de comercio electrónico
   - Discute el diseño de tablas de hechos, tablas de dimensiones y mejores prácticas de modelado de datos
   - [Ver informe completo](examples/ecommerce_data_warehouse_design.md)

2. **Estrategias de optimización de consultas SQL** - Optimización del rendimiento de consultas SQL para grandes conjuntos de datos
   - Explora estrategias de indexación, reescritura de consultas y técnicas de optimización de costos
   - [Ver informe completo](examples/sql_query_optimization.md)

3. **Construcción de pipeline de datos en tiempo real** - Construcción de pipelines de datos en tiempo real usando tecnologías de streaming modernas
   - Investiga Kafka, Spark Streaming y arquitecturas de procesamiento de datos en tiempo real
   - [Ver informe completo](examples/realtime_data_pipeline.md)

4. **Marco de monitoreo de calidad de datos** - Implementación de verificaciones automatizadas de calidad de datos y monitoreo
   - Explora métricas de calidad de datos, detección de anomalías y estrategias de remediación automatizadas
   - [Ver informe completo](examples/data_quality_monitoring.md)

5. **¿Qué es LLM?** - Una exploración profunda de modelos de lenguaje grandes
   - Discute arquitectura, entrenamiento, aplicaciones y consideraciones éticas
   - [Ver informe completo](examples/what_is_llm.md)

6. **¿Cómo usar Claude para investigación profunda?** - Mejores prácticas y flujos de trabajo para usar Claude en investigación profunda
   - Cubre ingeniería de prompts, análisis de datos e integración con otras herramientas
   - [Ver informe completo](examples/how_to_use_claude_deep_research.md)

7. **Adopción de IA en salud: Factores influyentes** - Análisis de factores que influyen en la adopción de IA en salud
   - Discute tecnologías de IA, calidad de datos, consideraciones éticas, evaluación económica, preparación organizacional e infraestructura digital
   - [Ver informe completo](examples/AI_adoption_in_healthcare.md)

8. **Impacto de la computación cuántica en la criptografía** - Análisis del impacto de la computación cuántica en la criptografía

   - Discute vulnerabilidades de la criptografía clásica, criptografía post-cuántica y soluciones criptográficas resistentes a cuántica
   - [Ver informe completo](examples/Quantum_Computing_Impact_on_Cryptography.md)

9. **Aspectos destacados del rendimiento de Cristiano Ronaldo** - Análisis de aspectos destacados del rendimiento de Cristiano Ronaldo
   - Discute sus logros profesionales, goles internacionales y rendimientos en varias competencias
   - [Ver informe completo](examples/Cristiano_Ronaldo's_Performance_Highlights.md)

Para ejecutar estos ejemplos o crear sus propios informes de investigación, puede usar los siguientes comandos:

```bash
# Ejecute con una consulta específica
uv run main.py "Diseñe una arquitectura de almacén de datos para análisis de comercio electrónico"

# Ejecute con parámetros de planificación personalizados
uv run main.py --max_plan_iterations 3 "¿Cómo optimizar el rendimiento de consultas SQL complejas?"

# Ejecute en modo interactivo con preguntas integradas
uv run main.py --interactive

# O ejecute con prompt interactivo básico
uv run main.py

# Vea todas las opciones disponibles
uv run main.py --help
```

### Modo interactivo

DataNova admite un modo interactivo con preguntas integradas en inglés y chino, específicamente adaptadas para escenarios de desarrollo de almacenes de datos:

1. Inicie el modo interactivo:

   ```bash
   uv run main.py --interactive
   ```

2. Seleccione su idioma preferido (inglés o chino)

3. Elija de la lista de preguntas integradas sobre almacenes de datos o seleccione la opción para hacer su propia pregunta

4. El sistema procesará su pregunta y generará un informe de análisis de datos completo

### Human-in-the-Loop

DataNova incluye un mecanismo human-in-the-loop que le permite revisar, editar y aprobar planes de análisis de datos antes de ejecutarlos:

1. **Revisión de planes**: Cuando human-in-the-loop está habilitado, el sistema le mostrará el plan de análisis de datos generado antes de la ejecución

2. **Proporcionar retroalimentación**: Puede:

   - Aceptar el plan respondiendo `[ACCEPTED]`
   - Editar el plan proporcionando retroalimentación (por ejemplo, `[EDIT PLAN] Agregue más pasos sobre verificaciones de calidad de datos`)
   - El sistema incorporará su retroalimentación y generará un plan revisado

3. **Aceptación automática**: Puede habilitar la aceptación automática para omitir el proceso de revisión:
   - A través de API: Establezca `auto_accepted_plan: true` en la solicitud

4. **Integración API**: Al usar la API, puede proporcionar retroalimentación a través del parámetro `feedback`:

   ```json
   {
     "messages": [{ "role": "user", "content": "Diseñe una arquitectura de almacén de datos de comercio electrónico" }],
     "thread_id": "my_thread_id",
     "auto_accepted_plan": false,
     "feedback": "[EDIT PLAN] Incluya más contenido sobre procesamiento de datos en tiempo real"
   }
   ```

### Argumentos de línea de comandos

DataNova admite múltiples argumentos de línea de comandos para personalizar su comportamiento:

- **query**: La consulta de análisis de datos a procesar (puede ser varias palabras)
- **--interactive**: Ejecutar en modo interactivo con preguntas integradas
- **--max_plan_iterations**: Número máximo de ciclos de planificación (predeterminado: 1)
- **--max_step_num**: Número máximo de pasos en un plan de análisis de datos (predeterminado: 3)
- **--debug**: Habilitar registro detallado de depuración

## Preguntas frecuentes

Vea [FAQ.md](docs/FAQ.md) para más detalles.

## Licencia

Este proyecto es de código abierto bajo la [Licencia MIT](./LICENSE).

## Agradecimientos

DataNova está construido sobre el excelente trabajo de la comunidad de código abierto. Apreciamos profundamente todos los proyectos y contribuyentes que hicieron posible DataNova. De hecho, nos paramos sobre los hombros de gigantes.

Nos gustaría expresar nuestra sincera gratitud a los siguientes proyectos por sus valiosas contribuciones:

- **[LangChain](https://github.com/langchain-ai/langchain)**: Su excelente marco impulsa nuestras interacciones LLM y cadenas, permitiendo integración y funcionalidad fluidas.
- **[LangGraph](https://github.com/langchain-ai/langgraph)**: Su enfoque innovador para la orquestación multiagente es crucial para implementar los flujos de trabajo complejos de DataNova.

Estos proyectos demuestran el poder transformador de la colaboración de código abierto, y estamos orgullosos de construir sobre sus fundamentos.

### Contribuyentes principales

Extendemos nuestro sincero agradecimiento a los autores principales de `DataNova` cuya visión, pasión y dedicación hicieron posible este proyecto:

- **[Daniel Walnut](https://github.com/hetaoBackend/)**
- **[Henry Li](https://github.com/magiccube/)**

Su compromiso inquebrantable y experiencia son la fuerza motriz detrás del éxito de DataNova. Estamos honrados de tenerlos liderando este viaje.

## Historial de estrellas

[![Star History Chart](https://api.star-history.com/svg?repos=hszhsz/DataNova&type=Date)](https://star-history.com/#hszhsz/DataNova&Date)