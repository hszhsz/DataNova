# 🚀 DataNova

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[English](./README.md) | [简体中文](./README_zh.md) | [日本語](./README_ja.md) | [Deutsch](./README_de.md) | [Español](./README_es.md) | [Русский](./README_ru.md) |[Portuguese](./README_pt.md)

> Datenlagerentwicklung mit KI-Intelligenz revolutionieren

**DataNova** ist eine KI-gestützte Datenlagerentwicklungsplattform, die große Sprachmodelle mit spezialisierten Tools kombiniert, um Datenteams intelligente Datenarchitekturdesign-, Abfrageoptimierungs- und automatisierte Pipeline-Generierungsfunktionen zu bieten. Unser Ziel ist es, die traditionelle Datenlagerentwicklung durch KI-gesteuerte Erkenntnisse und Empfehlungen zu transformieren.

DataNova ist jetzt offiziell im [FaaS-Anwendungszentrum von Volcengine](https://console.volcengine.com/vefaas/region:vefaas+cn-beijing/market) verfügbar, wo Benutzer über den [Erfahrungslink](https://console.volcengine.com/vefaas/region:vefaas+cn-beijing/market/datanova/?channel=github&source=datanova) eine Online-Erfahrung machen und seine leistungsstarken Funktionen und bequemen Bedienung intuitiv spüren können. Gleichzeitig unterstützt DataNova zur Erfüllung der Bereitstellungsanforderungen verschiedener Benutzer eine One-Click-Bereitstellung basierend auf Volcengine. Klicken Sie auf den [Bereitstellungslink](https://console.volcengine.com/vefaas/region:vefaas+cn-beijing/application/create?templateId=683adf9e372daa0008aaed5c&channel=github&source=datanova), um den Bereitstellungsprozess schnell abzuschließen und Ihre intelligente Datenlagerentwicklungsreise zu beginnen.

Bitte besuchen Sie die [offizielle Website von DataNova](https://datanova.tech/) für weitere Details.

## Demo

### Video

<https://github.com/user-attachments/assets/f3786598-1f2a-4d07-919e-8b99dfa1de3e>

In dieser Demo zeigen wir, wie man DataNova verwendet:

- Nahtlose Integration mit MCP-Services
- Durchführung von Tiefgang-Datenanalyseprozessen und Erstellung umfassender Berichte mit Diagrammen
- Erstellung von Podcast-Audio basierend auf generierten Analyseberichten

### Wiederholungsbeispiele

- [Design eines Sternschemas für ein E-Commerce-Datenlager](https://datanova.tech/chat?replay=ecommerce-star-schema-design)
- [Optimierung der Leistung komplexer SQL-Abfragen](https://datanova.tech/chat?replay=sql-query-optimization)
- [Aufbau von Echtzeit-Datenpipelines zur Verarbeitung von Streaming-Daten](https://datanova.tech/chat?replay=realtime-data-pipeline)
- [Implementierung von Datenqualitätsüberwachung und Warnsystemen](https://datanova.tech/chat?replay=data-quality-monitoring)
- [Besuchen Sie unsere offizielle Website, um weitere Wiederholungsbeispiele zu erkunden.](https://datanova.tech/#case-studies)

---

## 📑 Inhaltsverzeichnis

- [🚀 Schnellstart](#schnellstart)
- [🌟 Funktionen](#funktionen)
- [🏗️ Architektur](#architektur)
- [🛠️ Entwicklung](#entwicklung)
- [🗣️ Text-to-Speech-Integration](#text-to-speech-integration)
- [📚 Beispiele](#beispiele)
- [❓ FAQ](#faq)
- [📜 Lizenz](#lizenz)
- [💖 Danksagungen](#danksagungen)
- [⭐ Sternverlauf](#sternverlauf)

## Schnellstart

DataNova ist in Python entwickelt und verfügt über eine in Node.js geschriebene Web-Benutzeroberfläche. Um einen reibungslosen Setup-Prozess zu gewährleisten, empfehlen wir die Verwendung der folgenden Tools:

### Empfohlene Tools

- **[`uv`](https://docs.astral.sh/uv/getting-started/installation/):**
  Vereinfacht die Python-Umgebungs- und Abhängigkeitsverwaltung. `uv` erstellt automatisch eine virtuelle Umgebung im Stammverzeichnis und installiert alle erforderlichen Pakete für Sie—keine manuelle Installation von Python-Umgebungen erforderlich.

- **[`nvm`](https://github.com/nvm-sh/nvm):**
  Einfache Verwaltung mehrerer Node.js-Laufzeitversionen.

- **[`pnpm`](https://pnpm.io/installation):**
  Installation und Verwaltung von Abhängigkeiten für Node.js-Projekte.

### Umgebungsanforderungen

Stellen Sie sicher, dass Ihr System die folgenden Mindestanforderungen erfüllt:

- **[Python](https://www.python.org/downloads/):** Version `3.12+`
- **[Node.js](https://nodejs.org/en/download/):** Version `22+`

### Installation

```bash
# Repository klonen
git clone https://github.com/hszhsz/DataNova
cd DataNova

# Abhängigkeiten installieren, uv übernimmt die Erstellung des Python-Interpreters und der virtuellen Umgebung sowie die Installation der erforderlichen Pakete
uv sync

# .env mit Ihren API-Schlüsseln konfigurieren
# Tavily: https://app.tavily.com/home
# Brave_SEARCH: https://brave.com/search/api/
# Volcengine TTS: Hinzufügen, wenn Sie TTS-Anmeldeinformationen haben
cp .env.example .env

# Siehe die Abschnitte "Unterstützte Suchmaschinen" und "Text-to-Speech-Integration" unten für alle verfügbaren Optionen

# conf.yaml mit Ihren LLM-Modellen und API-Schlüsseln konfigurieren
# Siehe 'docs/configuration_guide.md' für weitere Details
cp conf.yaml.example conf.yaml

# marp für PPT-Generierung installieren
# https://github.com/marp-team/marp-cli?tab=readme-ov-file#use-package-manager
brew install marp-cli
```

Optional Web-UI-Abhängigkeiten über [pnpm](https://pnpm.io/installation) installieren:

```bash
cd DataNova/web
pnpm install
```

### Konfiguration

Siehe [Konfigurationsanleitung](docs/configuration_guide.md) für weitere Details.

> [!NOTE]
> Bitte lesen Sie den Leitfaden sorgfältig durch, bevor Sie das Projekt starten, und aktualisieren Sie die Konfiguration entsprechend Ihren spezifischen Einstellungen und Anforderungen.

### Konsolen-UI

Die schnellste Möglichkeit, das Projekt auszuführen, ist die Verwendung der Konsolen-UI.

```bash
# Das Projekt in einer bash-ähnlichen Shell ausführen
uv run main.py
```

### Web-UI

Dieses Projekt enthält auch eine Web-Benutzeroberfläche, die ein dynamischeres und ansprechenderes interaktives Erlebnis bietet.
> [!NOTE]
> Sie müssen zuerst die Web-UI-Abhängigkeiten installieren.

```bash
# Gleichzeitiges Ausführen von Backend- und Frontend-Servern im Entwicklungsmodus
# Auf macOS/Linux
./bootstrap.sh -d

# Auf Windows
bootstrap.bat -d
```

Öffnen Sie Ihren Browser und besuchen Sie [`http://localhost:3000`](http://localhost:3000), um die Web-Benutzeroberfläche zu erkunden.

Erforschen Sie weitere Details im [`web`](./web/)-Verzeichnis.

## Unterstützte Suchmaschinen

### Öffentliche Suchmaschinen

DataNova unterstützt mehrere Suchmaschinen, die in der `.env`-Datei über die `SEARCH_API`-Variable konfiguriert werden können:

- **Tavily** (Standard): Professionelle Such-API, speziell für KI-Anwendungen entwickelt
  - Erfordert das Setzen von `TAVILY_API_KEY` in der `.env`-Datei
  - Registrierungsadresse: <https://app.tavily.com/home>

- **DuckDuckGo**: Datenschutzorientierte Suchmaschine
  - Kein API-Schlüssel erforderlich

- **Brave Search**: Datenschutzorientierte Suchmaschine mit erweiterten Funktionen
  - Erfordert das Setzen von `BRAVE_SEARCH_API_KEY` in der `.env`-Datei
  - Registrierungsadresse: <https://brave.com/search/api/>

- **Arxiv**: Wissenschaftliche Papier-Suche für akademische Forschung
  - Kein API-Schlüssel erforderlich
  - Speziell für wissenschaftliche und akademische Papiere entwickelt

Um Ihre bevorzugte Suchmaschine zu konfigurieren, setzen Sie die `SEARCH_API`-Variable in der `.env`-Datei:

```bash
# Wählen Sie eine aus: tavily, duckduckgo, brave_search, arxiv
SEARCH_API=tavily
```

### Private Wissensdatenbank-Engines

DataNova unterstützt die Suche basierend auf privatem Domänenwissen. Sie können Dokumente in mehrere private Wissensdatenbanken hochladen, die während der Datenanalyse verwendet werden. Derzeit unterstützte private Wissensdatenbanken sind:

- **[RAGFlow](https://ragflow.io/docs/dev/)**: Open-Source-Wissensdatenbank-Engine basierend auf Retrieval-Augmented Generation
   ```
   # Siehe .env.example für die Konfiguration
   RAG_PROVIDER=ragflow
   RAGFLOW_API_URL="http://localhost:9388"
   RAGFLOW_API_KEY="ragflow-xxx"
   RAGFLOW_RETRIEVAL_SIZE=10
   ```

- **[VikingDB Wissensdatenbank](https://www.volcengine.com/docs/84313/1254457)**: Public-Cloud-Wissensdatenbank-Engine von Volcengine
   > Hinweis: Zuerst AK/SK von [Volcengine](https://www.volcengine.com/docs/84313/1254485) abrufen
   ```
   # Siehe .env.example für die Konfiguration
   RAG_PROVIDER=vikingdb_knowledge_base
   VIKINGDB_KNOWLEDGE_BASE_API_URL="api-knowledgebase.mlp.cn-beijing.volces.com"
   VIKINGDB_KNOWLEDGE_BASE_API_AK="volcengine-ak-xxx"
   VIKINGDB_KNOWLEDGE_BASE_API_SK="volcengine-sk-xxx"
   VIKINGDB_KNOWLEDGE_BASE_RETRIEVAL_SIZE=15
   ```

## Funktionen

### Kernfunktionen

- 🤖 **KI-gestütztes Datenarchitekturdesign**
  - Unterstützt die Integration der meisten Modelle durch [litellm](https://docs.litellm.ai/docs/providers)
  - Unterstützt Open-Source-Modelle wie Qwen
  - Kompatibel mit OpenAI-API-Schnittstelle
  - Mehrschichtige LLM-Systeme für Aufgaben unterschiedlicher Komplexität

### Datenwerkzeuge und MCP-Integration

- 🔍 **Datenexploration und -abruf**
  - Datenquellensuche durch Tavily, Brave Search und andere
  - Datencrawling mit Jina
  - Fortschrittliche Dateninhalts-Extraktion
  - Unterstützt den Abruf spezifizierter privater Wissensdatenbanken

- 📃 **RAG-Integration**
  - Unterstützt [RAGFlow](https://github.com/infiniflow/ragflow)-Wissensdatenbank
  - Unterstützt [VikingDB](https://www.volcengine.com/docs/84313/1254457) Volcengine-Wissensdatenbank

- 🔗 **MCP nahtlose Integration**
  - Erweitert Funktionen für Datenquellenzugriff, Datenqualitätsprüfungen, Abfrageoptimierung und mehr
  - Fördert die Integration vielfältiger Datenwerkzeuge und -methoden

### KI-gestützte Zusammenarbeit

- 🧠 **Human-in-the-Loop**
  - Unterstützt interaktive Änderung von Datenarchitekturplänen mit natürlicher Sprache
  - Unterstützt automatische Annahme von Architekturplänen

- 📝 **Datenbericht-Post-Editing**
  - Unterstützt Notion-ähnliche Block-Bearbeitung
  - Ermöglicht KI-Optimierung, einschließlich KI-unterstützter Feinabstimmung, Satzverkürzung und -erweiterung
  - Unterstützt von [tiptap](https://tiptap.dev/)

### Inhaltserstellung

- 🎙️ **Podcast- und Präsentationserstellung**
  - KI-gestützte Podcast-Skriptgenerierung und Audio-Synthese
  - Automatische Erstellung einfacher PowerPoint-Präsentationen
  - Anpassbare Vorlagen zur Erfüllung personalisierter Inhaltsbedürfnisse

## Architektur

DataNova implementiert eine modulare Multi-Agenten-Systemarchitektur, die für automatisierte Datenlagerentwicklung und Datenanalyse konzipiert ist. Das System basiert auf LangGraph und implementiert einen flexiblen zustandsbasierten Workflow, bei dem Komponenten durch ein klar definiertes Nachrichtenübermittlungssystem kommunizieren.

![Architekturdiagramm](./assets/architecture.png)

> Live-Demo unter [datanova.tech](https://datanova.tech/#multi-agent-architecture) anzeigen

Das System verwendet einen optimierten Workflow, der aus den folgenden Komponenten besteht:

1. **Koordinator**: Der Einstiegspunkt, der den Workflow-Lebenszyklus verwaltet

   - Initiierung des Datenanalyseprozesses basierend auf Benutzereingaben
   - Delegierung von Aufgaben an den Planer zu geeigneten Zeitpunkten
   - Dient als Hauptschnittstelle zwischen Benutzer und System

2. **Planer**: Die strategische Komponente, die für Aufgabendekomposition und -planung verantwortlich ist

   - Analyse von Datenanalysezielen und Erstellung strukturierter Ausführungspläne
   - Bestimmung, ob ausreichend Kontext vorhanden ist oder mehr Datenexploration erforderlich ist
   - Verwaltung des Datenanalyseprozesses und Entscheidung, wann der Abschlussbericht generiert wird

3. **Datenanalyseteam**: Eine Sammlung spezialisierter Agenten, die den Plan ausführen:
   - **Datenanalyst**: Durchführung von Datensuche und Informationssammlung mit Tools wie Datensuchmaschinen, Crawlern und sogar MCP-Services.
   - **Dateningenieur**: Handhabung von Datenverarbeitung, Analyse und technischen Aufgaben mit Python REPL-Tools.
   Jeder Agent hat Zugriff auf spezifische, für seine Rolle optimierte Tools und arbeitet innerhalb des LangGraph-Frameworks

4. **Reporter**: Der abschließende Prozessor für Datenanalyseausgaben
   - Aggregation von Erkenntnissen des Datenanalyseteams
   - Verarbeitung und Organisation gesammelter Informationen
   - Erstellung umfassender Datenanalyseberichte

## Text-to-Speech-Integration

DataNova enthält jetzt eine Text-to-Speech-(TTS)-Funktion, mit der Sie Forschungsberichte in Audio umwandeln können. Diese Funktion verwendet die Volcengine TTS API zur Erstellung hochwertiger Text-Audio. Eigenschaften wie Geschwindigkeit, Lautstärke und Tonhöhe können ebenfalls angepasst werden.

### Verwendung der TTS-API

Sie können über den `/api/tts`-Endpunkt auf die TTS-Funktion zugreifen:

```bash
# Beispiel-API-Aufruf mit curl
curl --location 'http://localhost:8000/api/tts' \
--header 'Content-Type: application/json' \
--data '{
    "text": "Dies ist ein Test der Text-to-Speech-Funktion.",
    "speed_ratio": 1.0,
    "volume_ratio": 1.0,
    "pitch_ratio": 1.0
}' \
--output speech.mp3
```

## Entwicklung

### Testen

Test-Suite ausführen:

```bash
# Alle Tests ausführen
make test

# Bestimmte Testdateien ausführen
pytest tests/integration/test_workflow.py

# Abdeckungstests ausführen
make coverage
```

### Codequalität

```bash
# Code-Linting ausführen
make lint

# Code formatieren
make format
```

### Debuggen mit LangGraph Studio

DataNova verwendet LangGraph als Workflow-Architektur. Sie können LangGraph Studio verwenden, um Workflows in Echtzeit zu debuggen und zu visualisieren.

#### Lokales Ausführen von LangGraph Studio

DataNova enthält eine `langgraph.json`-Konfigurationsdatei, die die Graphenstruktur und Abhängigkeiten für LangGraph Studio definiert. Diese Datei verweist auf den im Projekt definierten Workflow-Graphen und lädt automatisch Umgebungsvariablen aus der `.env`-Datei.

##### Mac

```bash
# Installieren Sie den uv-Paketmanager, falls Sie ihn nicht haben
curl -LsSf https://astral.sh/uv/install.sh | sh

# Abhängigkeiten installieren und den LangGraph-Server starten
uvx --refresh --from "langgraph-cli[inmem]" --with-editable . --python 3.12 langgraph dev --allow-blocking
```

##### Windows / Linux

```bash
# Abhängigkeiten installieren
pip install -e .
pip install -U "langgraph-cli[inmem]"

# Den LangGraph-Server starten
langgraph dev
```

Nach dem Start des LangGraph-Servers sehen Sie mehrere URLs im Terminal:

- API: <http://127.0.0.1:2024>
- Studio UI: <https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024>
- API-Dokumentation: <http://127.0.0.1:2024/docs>

Öffnen Sie den Studio UI-Link in Ihrem Browser, um auf die Debugging-Oberfläche zuzugreifen.

#### Verwendung von LangGraph Studio

In der Studio UI können Sie:

1. Den Workflow-Graphen visualisieren und sehen, wie Komponenten verbunden sind
2. Die Ausführung in Echtzeit verfolgen, um zu verstehen, wie Daten durch das System fließen
3. Den Status jedes Schritts im Workflow prüfen
4. Probleme debuggen, indem Sie die Ein- und Ausgabe jeder Komponente untersuchen
5. Feedback während der Planungsphase geben, um den Forschungsplan zu verfeinern

Wenn Sie ein Datenanalyse-Thema in der Studio UI einreichen, können Sie den gesamten Workflow-Ausführungsprozess sehen, einschließlich:

- Die Planungsphase, in der der Datenanalyseplan erstellt wird
- Feedback-Schleifen, in denen der Plan geändert werden kann
- Datenanalysephasen für jeden Abschnitt
- Abschließende Berichtsgenerierung

### Aktivierung von LangSmith-Tracing

DataNova unterstützt die LangSmith-Tracing-Funktionalität, um Ihnen bei der Fehlersuche und Überwachung von Workflows zu helfen. Um LangSmith-Tracing zu aktivieren:

1. Stellen Sie sicher, dass Sie die folgende Konfiguration in Ihrer `.env`-Datei haben (siehe `.env.example`):

   ```bash
   LANGSMITH_TRACING=true
   LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
   LANGSMITH_API_KEY="xxx"
   LANGSMITH_PROJECT="xxx"
   ```

2. Starten Sie LangSmith-Tracing lokal, indem Sie Folgendes ausführen:

   ```bash
   langgraph dev
   ```

Dadurch wird die Tracing-Visualisierung in LangGraph Studio aktiviert und Ihre Traces werden zur Überwachung und Analyse an LangSmith gesendet.

## Docker

Sie können dieses Projekt auch mit Docker ausführen.

Zuerst müssen Sie den Abschnitt [Konfiguration](#konfiguration) unten lesen. Stellen Sie sicher, dass die `.env`- und `.conf.yaml`-Dateien bereit sind.

Erstellen Sie als Nächstes Ihr eigenes Webserver-Docker-Image:

```bash
docker build -t datanova-api .
```

Starten Sie abschließend den Docker-Container, der den Webserver ausführt:

```bash
# Ersetzen Sie datanova-api-app durch Ihren bevorzugten Containernamen
# Starten Sie den Server und binden Sie ihn an localhost:8000
docker run -d -t -p 127.0.0.1:8000:8000 --env-file .env --name datanova-api-app datanova-api

# Stoppen Sie den Server
docker stop datanova-api-app
```

### Docker Compose

Sie können dieses Projekt auch mit Docker Compose einrichten:

```bash
# Docker-Images erstellen
docker compose build

# Den Server starten
docker compose up
```

> [!WARNING]
> Wenn Sie DataNova in einer Produktionsumgebung bereitstellen möchten, fügen Sie bitte Authentifizierung zur Website hinzu und bewerten Sie die Sicherheitsprüfungen für MCPServer und Python Repl.

## Beispiele

Die folgenden Beispiele zeigen die Fähigkeiten von DataNova:

### Datenanalyseberichte

1. **E-Commerce-Datenlagerdesign** - Sternschema-Design für ein E-Commerce-Analyse-Datenlager
   - Diskussion über Faktentabellen-, Dimensionstabellen-Design und bewährte Datenmodellierungspraktiken
   - [Vollständigen Bericht anzeigen](examples/ecommerce_data_warehouse_design.md)

2. **SQL-Abfrageoptimierungsstrategien** - SQL-Abfrageleistungs-Optimierung für große Datensätze
   - Erkundung von Indizierungsstrategien, Abfrageneuschreibung und Kostenoptimierungstechniken
   - [Vollständigen Bericht anzeigen](examples/sql_query_optimization.md)

3. **Aufbau von Echtzeit-Datenpipelines** - Aufbau von Echtzeit-Datenpipelines mit modernen Streaming-Technologien
   - Forschung zu Kafka, Spark Streaming und Echtzeit-Datenverarbeitungsarchitekturen
   - [Vollständigen Bericht anzeigen](examples/realtime_data_pipeline.md)

4. **Datenqualitätsüberwachungsrahmen** - Implementierung automatisierter Datenqualitätsprüfungen und -überwachung
   - Erkundung von Datenqualitätsmetriken, Anomalieerkennung und automatisierten Abhilfestrategien
   - [Vollständigen Bericht anzeigen](examples/data_quality_monitoring.md)

5. **Was ist LLM?** - Eine tiefgehende Erkundung großer Sprachmodelle
   - Diskussion über Architektur, Training, Anwendungen und ethische Überlegungen
   - [Vollständigen Bericht anzeigen](examples/what_is_llm.md)

6. **Wie verwendet man Claude für Tiefgang-Forschung?** - Best Practices und Workflows für die Verwendung von Claude in Tiefgang-Forschung
   - Deckt Prompt-Engineering, Datenanalyse und Integration mit anderen Tools ab
   - [Vollständigen Bericht anzeigen](examples/how_to_use_claude_deep_research.md)

7. **KI-Einführung im Gesundheitswesen: Einflussfaktoren** - Analyse der Faktoren, die die KI-Einführung im Gesundheitswesen beeinflussen
   - Diskussion über KI-Technologien, Datenqualität, ethische Überlegungen, Wirtschaftsbewertung, Organisationsbereitschaft und digitale Infrastruktur
   - [Vollständigen Bericht anzeigen](examples/AI_adoption_in_healthcare.md)

8. **Auswirkung von Quantencomputing auf Kryptographie** - Analyse der Auswirkung von Quantencomputing auf Kryptographie

   - Diskussion über Schwachstellen klassischer Kryptographie, Post-Quanten-Kryptographie und quantenresistente kryptographische Lösungen
   - [Vollständigen Bericht anzeigen](examples/Quantum_Computing_Impact_on_Cryptography.md)

9. **Cristiano Ronaldos Leistungshighlights** - Analyse der Leistungshighlights von Cristiano Ronaldo
   - Diskussion über seine Karriereerfolge, internationale Tore und Leistungen in verschiedenen Wettbewerben
   - [Vollständigen Bericht anzeigen](examples/Cristiano_Ronaldo's_Performance_Highlights.md)

Um diese Beispiele auszuführen oder Ihre eigenen Forschungsberichte zu erstellen, können Sie die folgenden Befehle verwenden:

```bash
# Mit einer bestimmten Abfrage ausführen
uv run main.py "Entwerfen Sie eine Datenlagerarchitektur für E-Commerce-Analysen"

# Mit benutzerdefinierten Planungsparametern ausführen
uv run main.py --max_plan_iterations 3 "Wie optimiert man die Leistung komplexer SQL-Abfragen?"

# Im interaktiven Modus mit integrierten Fragen ausführen
uv run main.py --interactive

# Oder mit grundlegendem interaktivem Prompt ausführen
uv run main.py

# Alle verfügbaren Optionen anzeigen
uv run main.py --help
```

### Interaktiver Modus

DataNova unterstützt einen interaktiven Modus mit integrierten Fragen in Englisch und Chinesisch, die speziell auf Szenarien der Datenlagerentwicklung zugeschnitten sind:

1. Interaktiven Modus starten:

   ```bash
   uv run main.py --interactive
   ```

2. Bevorzugte Sprache auswählen (Englisch oder Chinesisch)

3. Aus der integrierten Datenlager-Fragenliste wählen oder die Option auswählen, eine eigene Frage zu stellen

4. Das System verarbeitet Ihre Frage und erstellt einen umfassenden Datenanalysebericht

### Human-in-the-Loop

DataNova enthält einen Human-in-the-Loop-Mechanismus, der es Ihnen ermöglicht, Datenanalysepläne vor der Ausführung zu überprüfen, zu bearbeiten und zu genehmigen:

1. **Planüberprüfung**: Wenn Human-in-the-Loop aktiviert ist, zeigt das System Ihnen den generierten Datenanalyseplan vor der Ausführung an

2. **Feedback geben**: Sie können:

   - Den Plan akzeptieren, indem Sie `[ACCEPTED]` antworten
   - Den Plan bearbeiten, indem Sie Feedback geben (z.B. `[EDIT PLAN] Fügen Sie weitere Schritte zu Datenqualitätsprüfungen hinzu`)
   - Das System wird Ihr Feedback einbeziehen und einen überarbeiteten Plan erstellen

3. **Automatische Annahme**: Sie können die automatische Annahme aktivieren, um den Überprüfungsprozess zu überspringen:
   - Über API: Setzen Sie `auto_accepted_plan: true` in der Anfrage

4. **API-Integration**: Bei Verwendung der API können Sie Feedback über den `feedback`-Parameter geben:

   ```json
   {
     "messages": [{ "role": "user", "content": "Entwerfen Sie eine E-Commerce-Datenlagerarchitektur" }],
     "thread_id": "my_thread_id",
     "auto_accepted_plan": false,
     "feedback": "[EDIT PLAN] Fügen Sie mehr Inhalte zur Echtzeit-Datenverarbeitung hinzu"
   }
   ```

### Befehlszeilenargumente

DataNova unterstützt mehrere Befehlszeilenargumente zur Anpassung des Verhaltens:

- **query**: Die zu verarbeitende Datenanalyseabfrage (kann mehrere Wörter sein)
- **--interactive**: Im interaktiven Modus mit integrierten Fragen ausführen
- **--max_plan_iterations**: Maximale Anzahl von Planungszyklen (Standard: 1)
- **--max_step_num**: Maximale Anzahl von Schritten in einem Datenanalyseplan (Standard: 3)
- **--debug**: Ausführliche Debug-Protokollierung aktivieren

## FAQ

Siehe [FAQ.md](docs/FAQ.md) für weitere Details.

## Lizenz

Dieses Projekt ist Open Source unter der [MIT-Lizenz](./LICENSE).

## Danksagungen

DataNova basiert auf der hervorragenden Arbeit der Open-Source-Community. Wir schätzen alle Projekte und Mitwirkenden zutiefst, die DataNova möglich gemacht haben. Tatsächlich stehen wir auf den Schultern von Riesen.

Wir möchten den folgenden Projekten für ihre wertvollen Beiträge herzlich danken:

- **[LangChain](https://github.com/langchain-ai/langchain)**: Ihr hervorragendes Framework treibt unsere LLM-Interaktionen und -Ketten an und ermöglicht eine nahtlose Integration und Funktionalität.
- **[LangGraph](https://github.com/langchain-ai/langgraph)**: Ihr innovativer Ansatz für Multi-Agenten-Orchestrierung ist entscheidend für die Implementierung komplexer Workflows von DataNova.

Diese Projekte demonstrieren die transformative Kraft der Open-Source-Zusammenarbeit, und wir sind stolz darauf, auf ihren Grundlagen aufzubauen.

### Hauptmitwirkende

Wir danken den Hauptautoren von `DataNova` herzlich für ihre Vision, Leidenschaft und Hingabe, die dieses Projekt möglich gemacht haben:

- **[Daniel Walnut](https://github.com/hetaoBackend/)**
- **[Henry Li](https://github.com/magiccube/)**

Ihr unerschütterliches Engagement und Ihre Expertise sind die treibende Kraft hinter dem Erfolg von DataNova. Wir sind geehrt, dass Sie diese Reise leiten.

## Sternverlauf

[![Star History Chart](https://api.star-history.com/svg?repos=hszhsz/DataNova&type=Date)](https://star-history.com/#hszhsz/DataNova&Date)