# DataNova Sandbox — 银行业模拟数据平台

> 单机可复现的银行业数据平台沙箱: **PostgreSQL(源库) + MinIO(对象存储) + Trino(OLAP) + dbt(分层建模)**，并**故意埋设 7 类"坑"** 用于检验各类 Data Agent 的治理能力。
> 设计蓝图见 [docs/bank-platform-design.md](../docs/bank-platform-design.md)。

---

## 一、目录结构

```
sandbox/
├── docker-compose.yml         # PostgreSQL + MinIO + Trino (+ OpenMetadata 可选)
├── README.md                  # 本文件
├── seed/
│   └── generate_bank_data.py  # 银行数据生成脚本(含故意埋坑)
├── dbt/
│   ├── dbt_project.yml
│   ├── profiles.example.yml
│   ├── models/  ods/ dwd/ dws/ ads/ dim/
│   └── metrics/metrics.yml    # 核心指标口径(含冲突示例)
└── trino/
    └── catalog/postgres.properties
```

## 二、一键启动(傻瓜式步骤)

**前置**：本机已安装 Docker / Docker Compose、Python 3。

### 步骤 1 — 启动底层服务

```bash
cd sandbox
docker compose up -d           # 启动 PostgreSQL + MinIO + Trino
docker compose ps              # 确认三个容器 healthy
```

> 需要测元数据/血缘 Agent 时再启 OpenMetadata：`docker compose --profile gov up -d`

### 步骤 2 — 生成模拟数据(含埋坑)

```bash
pip install psycopg2-binary faker
python seed/generate_bank_data.py
```

默认生成 1000 客户 / 20000 笔交易。可用环境变量调整：`N_CUST=2000 N_TXN=50000 python seed/generate_bank_data.py`。

### 步骤 3 — 运行 dbt 分层建模

```bash
pip install dbt-postgres
cp dbt/profiles.example.yml ~/.dbt/profiles.yml   # 首次配置连接
cd dbt
dbt run                        # 执行 ODS→DWD→DWS→ADS+DIM
dbt test                       # 跑数据测试(唯一性/非空等)
dbt docs generate && dbt docs serve   # 查看血缘 & 文档
```

> ⚠️ `dbt run` 会在 `ads_broken_pipeline` 与 `ads_regulatory_report` 处**故意报错/断裂**（埋坑 #7/#5）。这是预期行为，用来检验运维/血缘 Agent。可用 `dbt run --exclude ads_broken_pipeline ads_regulatory_report` 跑通其余模型。

### 步骤 4 — 用 Trino 查询(可选)

访问 Trino UI：http://localhost:8080 ；MinIO 控制台：http://localhost:9001 （minioadmin/minioadmin）。

```sql
-- 在 Trino 中按层查询
SELECT * FROM postgres.ods.cust_info LIMIT 10;
SELECT * FROM postgres.ads.ads_cust_profile LIMIT 10;
```

---

## 三、埋坑清单(给 Agent 留活干)

| # | 坑 | 位置 | 检验哪个 Agent |
|---|---|---|---|
| 1 | **口径冲突**：活跃客户 零售口径(近30天) vs 对公口径(近90天) | `dws_active_cust_retail_d` / `dws_active_cust_corp_d` / `metrics.yml` | 指标治理 Agent |
| 2 | **敏感字段未脱敏**：身份证(C4)/手机号(C3) 明文 | `ods.cust_info` | 安全合规 / 数据分级 Agent |
| 3 | **不良率口径分散**：NPL 判定逻辑不统一、未认证 | `ads_npl_report` + 风险域 | 可信指标认证 |
| 4 | **脏数据**：负余额 / 异常巨额交易 / KYC 空值 | `ods.acct_deposit` / `ods.txn_flow` / `ods.cust_kyc` | 数据质量(DQC) Agent |
| 5 | **血缘断裂**：报送报表硬编码外部表，追不到源头 | `ads_regulatory_report` | 元数据/血缘 Agent |
| 6 | **僵尸表**：无下游引用的冗余汇总表 | `ods.zombie_acct_summary_bak` | 资产治理 Agent |
| 7 | **调度失败**：故意写错的 dbt 模型(字段不存在+除零) | `ads_broken_pipeline` | 运维/排障 Agent |

> 这是沙箱的精髓——没有坑，Agent 就没有用武之地。

---

## 四、清理

```bash
docker compose down -v         # 停止并删除容器与数据卷
```
