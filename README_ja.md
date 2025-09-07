# 🚀 DataNova

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[English](./README.md) | [简体中文](./README_zh.md) | [日本語](./README_ja.md) | [Deutsch](./README_de.md) | [Español](./README_es.md) | [Русский](./README_ru.md) |[Portuguese](./README_pt.md)

> AIインテリジェンスでデータウェアハウス開発を革新する

**DataNova** は、大規模言語モデルと専門ツールを組み合わせたAI駆動型データウェアハウス開発プラットフォームで、データチームにインテリジェントなデータアーキテクチャ設計、クエリ最適化、自動化パイプライン生成機能を提供します。私たちの目標は、AI駆動のインサイトと推奨を通じて、従来のデータウェアハウス開発を変革することです。

DataNovaは、[火山エンジンのFaaSアプリケーションセンター](https://console.volcengine.com/vefaas/region:vefaas+cn-beijing/market)に正式に登録されており、[体験リンク](https://console.volcengine.com/vefaas/region:vefaas+cn-beijing/market/datanova/?channel=github&source=datanova)を通じてオンライン体験が可能です。その強力な機能と便利な操作を直感的に感じ取ることができます。同時に、異なるユーザーのデプロイメントニーズを満たすため、DataNovaは火山エンジンベースのワンクリックデプロイメントをサポートしています。[デプロイメントリンク](https://console.volcengine.com/vefaas/region:vefaas+cn-beijing/application/create?templateId=683adf9e372daa0008aaed5c&channel=github&source=datanova)をクリックすることで、迅速にデプロイメントプロセスを完了し、インテリジェントなデータウェアハウス開発の旅を始めることができます。

[DataNovaの公式ウェブサイト](https://datanova.tech/)をご覧ください。

## デモ

### 動画

<https://github.com/user-attachments/assets/f3786598-1f2a-4d07-919e-8b99dfa1de3e>

このデモでは、DataNovaの使用方法を紹介します：

- MCPサービスとのシームレスな統合
- 深度のあるデータ分析プロセスとチャートを含む包括的なレポートの生成
- 生成された分析レポートに基づくポッドキャストオーディオの作成

### リプレイ例

- [eコマースデータウェアハウスのスター型スキーマ設計](https://datanova.tech/chat?replay=ecommerce-star-schema-design)
- [複雑なSQLクエリのパフォーマンス最適化](https://datanova.tech/chat?replay=sql-query-optimization)
- [ストリーミングデータを処理するリアルタイムデータパイプラインの構築](https://datanova.tech/chat?replay=realtime-data-pipeline)
- [データ品質監視およびアラートシステムの実装](https://datanova.tech/chat?replay=data-quality-monitoring)
- [公式ウェブサイトでより多くのリプレイ例を探索してください。](https://datanova.tech/#case-studies)

---

## 📑 目次

- [🚀 クイックスタート](#クイックスタート)
- [🌟 特徴](#特徴)
- [🏗️ アーキテクチャ](#アーキテクチャ)
- [🛠️ 開発](#開発)
- [🗣️ 音声合成統合](#音声合成統合)
- [📚 例](#例)
- [❓ FAQ](#faq)
- [📜 ライセンス](#ライセンス)
- [💖 謝辞](#謝辞)
- [⭐ スター履歴](#スター履歴)

## クイックスタート

DataNovaはPythonで開発され、Node.jsで書かれたWeb UIを備えています。スムーズなセットアッププロセスを確保するために、以下のツールの使用を推奨します：

### 推奨ツール

- **[`uv`](https://docs.astral.sh/uv/getting-started/installation/):**
  Python環境と依存関係管理を簡素化します。`uv`はルートディレクトリに仮想環境を自動的に作成し、必要なすべてのパッケージをインストールします—Python環境を手動でインストールする必要はありません。

- **[`nvm`](https://github.com/nvm-sh/nvm):**
  複数のNode.jsランタイムバージョンを簡単に管理できます。

- **[`pnpm`](https://pnpm.io/installation):**
  Node.jsプロジェクトの依存関係をインストールおよび管理します。

### 環境要件

システムが以下の最小要件を満たしていることを確認してください：

- **[Python](https://www.python.org/downloads/):** バージョン `3.12+`
- **[Node.js](https://nodejs.org/en/download/):** バージョン `22+`

### インストール

```bash
# リポジトリをクローン
git clone https://github.com/hszhsz/DataNova
cd DataNova

# 依存関係をインストール、uvがPythonインタープリターと仮想環境の作成を処理し、必要なパッケージをインストールします
uv sync

# .envをAPIキーで設定
# Tavily: https://app.tavily.com/home
# Brave_SEARCH: https://brave.com/search/api/
# 火山エンジンTTS: TTS認証情報がある場合は追加
cp .env.example .env

# 以下の「サポートされている検索エンジン」と「音声合成統合」のセクションで利用可能なすべてのオプションを確認してください

# LLMモデルとAPIキーでconf.yamlを設定
# 詳細は'docs/configuration_guide.md'を参照
cp conf.yaml.example conf.yaml

# PPT生成用にmarpをインストール
# https://github.com/marp-team/marp-cli?tab=readme-ov-file#use-package-manager
brew install marp-cli
```

オプションで、[pnpm](https://pnpm.io/installation)経由でWeb UIの依存関係をインストール：

```bash
cd DataNova/web
pnpm install
```

### 設定

詳細は[設定ガイド](docs/configuration_guide.md)を参照してください。

> [!NOTE]
> プロジェクトを開始する前にガイドをよく読み、設定を特定の設定と要件に合わせて更新してください。

### コンソールUI

プロジェクトを実行する最も速い方法はコンソールUIを使用することです。

```bash
# bash-likeシェルでプロジェクトを実行
uv run main.py
```

### Web UI

このプロジェクトには、より動的で魅力的なインタラクティブな体験を提供するWeb UIも含まれています。
> [!NOTE]
> まずWeb UIの依存関係をインストールする必要があります。

```bash
# 開発モードでバックエンドとフロントエンドのサーバーを同時に実行
# macOS/Linux上
./bootstrap.sh -d

# Windows上
bootstrap.bat -d
```

ブラウザを開いて[`http://localhost:3000`](http://localhost:3000)にアクセスしてWeb UIを探索してください。

[`web`](./web/)ディレクトリで詳細を探索してください。

## サポートされている検索エンジン

### パブリックドメイン検索エンジン

DataNovaは、`.env`ファイルの`SEARCH_API`変数で設定できる複数の検索エンジンをサポートしています：

- **Tavily**（デフォルト）：AIアプリケーション用に設計されたプロフェッショナル検索API
  - `.env`ファイルで`TAVILY_API_KEY`を設定する必要があります
  - 登録アドレス：<https://app.tavily.com/home>

- **DuckDuckGo**：プライバシー重視の検索エンジン
  - APIキー不要

- **Brave Search**：高度な機能を持つプライバシー重視の検索エンジン
  - `.env`ファイルで`BRAVE_SEARCH_API_KEY`を設定する必要があります
  - 登録アドレス：<https://brave.com/search/api/>

- **Arxiv**：学術研究用の科学論文検索
  - APIキー不要
  - 科学および学術論文用に特別に設計

お好みの検索エンジンを設定するには、`.env`ファイルで`SEARCH_API`変数を設定してください：

```bash
# 1つ選択：tavily, duckduckgo, brave_search, arxiv
SEARCH_API=tavily
```

### プライベート知識ベースエンジン

DataNovaは、プライベートドメイン知識に基づく検索をサポートしています。データ分析中に使用するために、ドキュメントを複数のプライベート知識ベースにアップロードできます。現在サポートされているプライベート知識ベースは以下の通りです：

- **[RAGFlow](https://ragflow.io/docs/dev/)**：検索強化生成に基づくオープンソース知識ベースエンジン
   ```
   # 設定については.env.exampleを参照
   RAG_PROVIDER=ragflow
   RAGFLOW_API_URL="http://localhost:9388"
   RAGFLOW_API_KEY="ragflow-xxx"
   RAGFLOW_RETRIEVAL_SIZE=10
   ```

- **[VikingDB 知識ベース](https://www.volcengine.com/docs/84313/1254457)**：火山エンジンが提供するパブリッククラウド知識ベースエンジン
   > 注：まず[火山エンジン](https://www.volcengine.com/docs/84313/1254485)からアカウントAK/SKを取得してください
   ```
   # 設定については.env.exampleを参照
   RAG_PROVIDER=vikingdb_knowledge_base
   VIKINGDB_KNOWLEDGE_BASE_API_URL="api-knowledgebase.mlp.cn-beijing.volces.com"
   VIKINGDB_KNOWLEDGE_BASE_API_AK="volcengine-ak-xxx"
   VIKINGDB_KNOWLEDGE_BASE_API_SK="volcengine-sk-xxx"
   VIKINGDB_KNOWLEDGE_BASE_RETRIEVAL_SIZE=15
   ```

## 特徴

### コア機能

- 🤖 **AI駆動型データアーキテクチャ設計**
  - [litellm](https://docs.litellm.ai/docs/providers)を通じてほとんどのモデルの統合をサポート
  - Qwenなどのオープンソースモデルをサポート
  - OpenAI APIインターフェースと互換性あり
  - 異なる複雑さのタスク用のマルチレイヤーLLMシステム

### データツールとMCP統合

- 🔍 **データ探索と検索**
  - Tavily、Brave Searchなどを通じたデータソース検索
  - Jinaを使用したデータクローリング
  - 高度なデータコンテンツ抽出
  - 指定されたプライベート知識ベースの検索をサポート

- 📃 **RAG統合**
  - [RAGFlow](https://github.com/infiniflow/ragflow)知識ベースをサポート
  - [VikingDB](https://www.volcengine.com/docs/84313/1254457)火山エンジン知識ベースをサポート

- 🔗 **MCPシームレス統合**
  - データソースアクセス、データ品質チェック、クエリ最適化などの機能を拡張
  - 多様なデータツールと方法論の統合を促進

### AI駆動型コラボレーション

- 🧠 **ヒューマンインザループ**
  - 自然言語を使用したデータアーキテクチャ計画のインタラクティブな修正をサポート
  - アーキテクチャ計画の自動承認をサポート

- 📝 **データレポート事後編集**
  - Notionのようなブロック編集をサポート
  - AI最適化を許可、AI支援の推敲、文の短縮と拡張を含む
  - [tiptap](https://tiptap.dev/)によって提供

### コンテンツ作成

- 🎙️ **ポッドキャストとプレゼンテーション生成**
  - AI駆動のポッドキャストスクリプト生成とオーディオ合成
  - 単純なPowerPointプレゼンテーションの自動作成
  - 個人的なコンテンツニーズを満たすカスタマイズ可能なテンプレート

## アーキテクチャ

DataNovaは、自動化されたデータウェアハウス開発とデータ分析用に設計されたモジュラー型マルチエージェントシステムアーキテクチャを実装しています。このシステムはLangGraph上に構築され、コンポーネントが明確に定義されたメッセージパッシングシステムを通じて通信する柔軟なステートベースのワークフローを実装しています。

![アーキテクチャ図](./assets/architecture.png)

> [datanova.tech](https://datanova.tech/#multi-agent-architecture)でライブデモを表示

システムは、以下のコンポーネントで構成される効率的なワークフローを採用しています：

1. **コーディネーター**：ワークフローのライフサイクルを管理するエントリポイント

   - ユーザー入力に基づいてデータ分析プロセスを開始
   - 適切なタイミングでプランナーにタスクを委任
   - ユーザーとシステム間の主要インターフェースとして機能

2. **プランナー**：タスクの分解と計画に責任を持つ戦略的コンポーネント

   - データ分析目標を分析し、構造化された実行計画を作成
   - 十分なコンテキストがあるか、またはより多くのデータ探索が必要かを判断
   - データ分析プロセスを管理し、最終レポートの生成タイミングを決定

3. **データ分析チーム**：計画を実行する専門エージェントのコレクション：
   - **データアナリスト**：データ検索エンジン、クローラー、MCPサービスなどのツールを使用してデータ検索と情報収集を実施。
   - **データエンジニア**：Python REPLツールを使用してデータ処理、分析、技術タスクを処理。
   各エージェントは、その役割に最適化された特定のツールにアクセスでき、LangGraphフレームワーク内で動作

4. **レポーター**：データ分析出力の最終段階プロセッサ
   - データ分析チームからの発見を集約
   - 収集された情報を処理および整理
   - 包括的なデータ分析レポートを生成

## 音声合成統合

DataNovaには、研究レポートを音声に変換できる音声合成（TTS）機能が含まれています。この機能は火山エンジンTTS APIを使用して高品質なテキストオーディオを生成します。速度、音量、ピッチなどの特性もカスタマイズできます。

### TTS APIの使用

`/api/tts`エンドポイントを通じてTTS機能にアクセスできます：

```bash
# curlを使用したAPI呼び出し例
curl --location 'http://localhost:8000/api/tts' \
--header 'Content-Type: application/json' \
--data '{
    "text": "これは音声合成機能のテストです。",
    "speed_ratio": 1.0,
    "volume_ratio": 1.0,
    "pitch_ratio": 1.0
}' \
--output speech.mp3
```

## 開発

### テスト

テストスイートを実行：

```bash
# すべてのテストを実行
make test

# 特定のテストファイルを実行
pytest tests/integration/test_workflow.py

# カバレッジテストを実行
make coverage
```

### コード品質

```bash
# コードリントを実行
make lint

# コードをフォーマット
make format
```

### LangGraph Studioでのデバッグ

DataNovaはワークフローアーキテクチャとしてLangGraphを使用しています。LangGraph Studioを使用して、ワークフローをリアルタイムでデバッグおよび視覚化できます。

#### ローカルでのLangGraph Studio実行

DataNovaには、LangGraph Studioのグラフ構造と依存関係を定義する`langgraph.json`設定ファイルが含まれています。このファイルはプロジェクトで定義されたワークフローグラフを指し、`.env`ファイルから環境変数を自動的にロードします。

##### Mac

```bash
# uvパッケージマネージャーがない場合はインストール
curl -LsSf https://astral.sh/uv/install.sh | sh

# 依存関係をインストールし、LangGraphサーバーを起動
uvx --refresh --from "langgraph-cli[inmem]" --with-editable . --python 3.12 langgraph dev --allow-blocking
```

##### Windows / Linux

```bash
# 依存関係をインストール
pip install -e .
pip install -U "langgraph-cli[inmem]"

# LangGraphサーバーを起動
langgraph dev
```

LangGraphサーバーを起動した後、ターミナルにいくつかのURLが表示されます：

- API: <http://127.0.0.1:2024>
- Studio UI: <https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024>
- APIドキュメント：<http://127.0.0.1:2024/docs>

ブラウザでStudio UIリンクを開いて、デバッグインターフェースにアクセスしてください。

#### LangGraph Studioの使用

Studio UIでは、以下が可能です：

1. ワークフローグラフを視覚化し、コンポーネントの接続方法を確認
2. 実行をリアルタイムで追跡し、システムを通じたデータの流れを理解
3. ワークフローの各ステップのステータスを検査
4. 各コンポーネントの入力と出力を検査して問題をデバッグ
5. 計画段階でフィードバックを提供して研究計画を洗練

Studio UIでデータ分析トピックを送信すると、ワークフローの実行プロセス全体を見ることができます：

- データ分析計画が作成される計画段階
- 計画を修正できるフィードバックループ
- 各セクションのデータ分析段階
- 最終レポート生成

### LangSmithトレースの有効化

DataNovaは、ワークフローのデバッグと監視に役立つLangSmithトレース機能をサポートしています。LangSmithトレースを有効にするには：

1. `.env`ファイルに以下の設定があることを確認（`.env.example`を参照）：

   ```bash
   LANGSMITH_TRACING=true
   LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
   LANGSMITH_API_KEY="xxx"
   LANGSMITH_PROJECT="xxx"
   ```

2. 以下を実行してローカルでLangSmithトレースを開始：

   ```bash
   langgraph dev
   ```

これにより、LangGraph Studioでのトレース視覚化が有効になり、トレースがLangSmithに送信されて監視と分析が行われます。

## Docker

Dockerを使用してこのプロジェクトを実行することもできます。

まず、以下の[設定](#configuration)セクションを読んでください。`.env`と`.conf.yaml`ファイルの準備ができていることを確認してください。

次に、独自のWebサーバーDockerイメージをビルド：

```bash
docker build -t datanova-api .
```

最後に、Webサーバーを実行するDockerコンテナを開始：

```bash
# datanova-api-appをお好みのコンテナ名に置き換え
# サーバーを起動し、localhost:8000にバインド
docker run -d -t -p 127.0.0.1:8000:8000 --env-file .env --name datanova-api-app datanova-api

# サーバーを停止
docker stop datanova-api-app
```

### Docker Compose

docker composeを使用してこのプロジェクトをセットアップすることもできます：

```bash
# dockerイメージをビルド
docker compose build

# サーバーを起動
docker compose up
```

> [!WARNING]
> DataNovaを本番環境にデプロイする場合は、ウェブサイトに認証を追加し、MCPServerとPython Replのセキュリティチェックを評価してください。

## 例

以下の例は、DataNovaの機能を示しています：

### データ分析レポート

1. **eコマースデータウェアハウス設計** - eコマース分析用データウェアハウスのスター型スキーマ設計
   - ファクトテーブル、ディメンションテーブル設計、データモデリングのベストプラクティスについて説明
   - [完全なレポートを表示](examples/ecommerce_data_warehouse_design.md)

2. **SQLクエリ最適化戦略** - 大規模データセットのSQLクエリパフォーマンス最適化
   - インデックス戦略、クエリ書き換え、コスト最適化技術について探求
   - [完全なレポートを表示](examples/sql_query_optimization.md)

3. **リアルタイムデータパイプライン構築** - 現代のストリーミング技術を使用したリアルタイムデータパイプラインの構築
   - Kafka、Spark Streaming、リアルタイムデータ処理アーキテクチャについて研究
   - [完全なレポートを表示](examples/realtime_data_pipeline.md)

4. **データ品質監視フレームワーク** - 自動化されたデータ品質チェックと監視の実装
   - データ品質メトリクス、異常検出、自動修復戦略について探求
   - [完全なレポートを表示](examples/data_quality_monitoring.md)

5. **LLMとは？** - 大規模言語モデルの詳細な探求
   - アーキテクチャ、トレーニング、アプリケーション、倫理的考慮について議論
   - [完全なレポートを表示](examples/what_is_llm.md)

6. **Claudeを使用した深度研究の方法？** - 深度研究でClaudeを使用するためのベストプラクティスとワークフロー
   - プロンプトエンジニアリング、データ分析、他のツールとの統合についてカバー
   - [完全なレポートを表示](examples/how_to_use_claude_deep_research.md)

7. **医療におけるAI採用：影響要因** - 医療におけるAI採用の影響要因の分析
   - AI技術、データ品質、倫理的考慮、経済評価、組織準備度、デジタルインフラについて議論
   - [完全なレポートを表示](examples/AI_adoption_in_healthcare.md)

8. **量子コンピューティングが暗号に与える影響** - 量子コンピューティングが暗号に与える影響の分析

   - 従来の暗号の脆弱性、ポスト量子暗号、量子耐性暗号ソリューションについて議論
   - [完全なレポートを表示](examples/Quantum_Computing_Impact_on_Cryptography.md)

9. **クリスティアーノ・ロナウドのパフォーマンスハイライト** - クリスティアーノ・ロナウドのパフォーマンスハイライトの分析
   - 彼のキャリアの成果、国際的なゴール、様々な競技でのパフォーマンスについて議論
   - [完全なレポートを表示](examples/Cristiano_Ronaldo's_Performance_Highlights.md)

これらの例を実行するか、独自の研究レポートを作成するには、以下のコマンドを使用できます：

```bash
# 特定のクエリで実行
uv run main.py "eコマース分析用データウェアハウスアーキテクチャを設計"

# カスタム計画パラメータで実行
uv run main.py --max_plan_iterations 3 "複雑なSQLクエリのパフォーマンスを最適化する方法？"

# 組み込み質問でインタラクティブモードで実行
uv run main.py --interactive

# または基本的なインタラクティブプロンプトで実行
uv run main.py

# 利用可能なすべてのオプションを表示
uv run main.py --help
```

### インタラクティブモード

DataNovaは、データウェアハウス開発シナリオに特化して調整された英語と中国語の組み込み質問を備えたインタラクティブモードをサポートしています：

1. インタラクティブモードを開始：

   ```bash
   uv run main.py --interactive
   ```

2. お好みの言語（英語または中国語）を選択

3. 組み込みのデータウェアハウス質問リストから選択するか、独自の質問をするオプションを選択

4. システムが質問を処理し、包括的なデータ分析レポートを生成

### ヒューマンインザループ

DataNovaには、データ分析計画を実行する前にレビュー、編集、承認できるヒューマンインザループメカニズムが含まれています：

1. **計画レビュー**：ヒューマンインザループが有効になっている場合、システムは実行前に生成されたデータ分析計画を表示

2. **フィードバックの提供**：以下が可能です：

   - `[ACCEPTED]`と返信して計画を承認
   - フィードバックを提供して計画を編集（例：`[EDIT PLAN] データ品質チェックのステップをさらに追加`）
   - システムはフィードバックを組み込み、改訂された計画を生成

3. **自動承認**：レビュープロセスをスキップするために自動承認を有効にできます：
   - API経由：リクエストで`auto_accepted_plan: true`を設定

4. **API統合**：APIを使用する場合、`feedback`パラメータを通じてフィードバックを提供できます：

   ```json
   {
     "messages": [{ "role": "user", "content": "eコマースデータウェアハウスアーキテクチャを設計" }],
     "thread_id": "my_thread_id",
     "auto_accepted_plan": false,
     "feedback": "[EDIT PLAN] リアルタイムデータ処理に関するコンテンツをさらに含める"
   }
   ```

### コマンドライン引数

DataNovaは、動作をカスタマイズするための複数のコマンドライン引数をサポートしています：

- **query**：処理するデータ分析クエリ（複数の単語が可能）
- **--interactive**：組み込み質問でインタラクティブモードで実行
- **--max_plan_iterations**：計画サイクルの最大数（デフォルト：1）
- **--max_step_num**：データ分析計画の最大ステップ数（デフォルト：3）
- **--debug**：詳細なデバッグログを有効化

## FAQ

詳細は[FAQ.md](docs/FAQ.md)を参照してください。

## ライセンス

このプロジェクトは[MITライセンス](./LICENSE)の下でオープンソースです。

## 謝辞

DataNovaは、オープンソースコミュニティの優れた仕事に基づいて構築されています。DataNovaを可能にしたすべてのプロジェクトと貢献者に深く感謝します。確かに、私たちは巨人の肩の上に立っています。

以下のプロジェクトに、価値ある貢献に対して心から感謝を表します：

- **[LangChain](https://github.com/langchain-ai/langchain)**：彼らの優れたフレームワークが私たちのLLMインタラクションとチェーンを動かし、シームレスな統合と機能を可能にしています。
- **[LangGraph](https://github.com/langchain-ai/langgraph)**：彼らのマルチエージェントオーケストレーションへの革新的なアプローチは、DataNovaの複雑なワークフローの実装に不可欠です。

これらのプロジェクトは、オープンソースコラボレーションの変革的な力を示しており、その基盤の上に構築できることを誇りに思っています。

### コア貢献者

`DataNova`のコア著者である以下の皆さんに、そのビジョン、情熱、献身によりこのプロジェクトを可能にしたことに心から感謝を表します：

- **[Daniel Walnut](https://github.com/hetaoBackend/)**
- **[Henry Li](https://github.com/magiccube/)**

皆さんの揺るぎないコミットメントと専門知識は、DataNovaの成功の原動力です。この旅をリードしていただき、光栄です。

## スター履歴

[![Star History Chart](https://api.star-history.com/svg?repos=hszhsz/DataNova&type=Date)](https://star-history.com/#hszhsz/DataNova&Date)