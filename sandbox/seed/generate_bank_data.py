"""
DataNova 银行业模拟数据 — 源库数据生成脚本

生成贴源 (ODS 级) 银行业务数据并写入 PostgreSQL, 覆盖主题域:
客户 / 账户 / 交易 / 产品 / 风险 / 维度。

⚠️ 本脚本**故意埋设"坑"**以检验 Data Agent 的治理能力, 详见 README 的埋坑清单。
   - 敏感字段明文 (身份证/手机号) —— 未脱敏
   - 脏数据 (负余额/异常金额/KYC 空值)
   - 口径冲突 (活跃客户两种定义)
   - 僵尸表 (无人引用的冗余表)

依赖: pip install psycopg2-binary faker
用法: python generate_bank_data.py  (默认连 localhost:5432)
"""

import os
import random
import datetime as dt

try:
    import psycopg2
    from faker import Faker
except ImportError:
    raise SystemExit("请先安装依赖: pip install psycopg2-binary faker")

fake = Faker("zh_CN")
random.seed(42)
Faker.seed(42)

DB = dict(
    host=os.getenv("PGHOST", "localhost"),
    port=int(os.getenv("PGPORT", 5432)),
    user=os.getenv("PGUSER", "bank"),
    password=os.getenv("PGPASSWORD", "bank_demo_pwd"),
    dbname=os.getenv("PGDATABASE", "core_bank"),
)

N_CUST = int(os.getenv("N_CUST", 1000))
N_TXN = int(os.getenv("N_TXN", 20000))

DDL = """
DROP SCHEMA IF EXISTS ods CASCADE;
CREATE SCHEMA ods;

-- 客户信息: ⚠️埋坑#2 身份证/手机号明文未脱敏 (C4 敏感)
CREATE TABLE ods.cust_info (
    cust_id      VARCHAR(20) PRIMARY KEY,
    cust_name    VARCHAR(50),
    id_card_no   VARCHAR(18),   -- C4 敏感, 明文
    mobile       VARCHAR(11),   -- C3 敏感, 明文
    cust_type    VARCHAR(10),   -- retail/corporate
    open_date    DATE,
    org_id       VARCHAR(10)
);

-- KYC: ⚠️埋坑#4 部分字段为空
CREATE TABLE ods.cust_kyc (
    cust_id      VARCHAR(20),
    risk_level   VARCHAR(10),   -- 可能为 NULL
    occupation   VARCHAR(50)    -- 可能为 NULL
);

-- 存款账户
CREATE TABLE ods.acct_deposit (
    acct_id      VARCHAR(20) PRIMARY KEY,
    cust_id      VARCHAR(20),
    balance      NUMERIC(18,2), -- ⚠️埋坑#4 可能为负
    currency     VARCHAR(3),
    status       VARCHAR(10),
    open_date    DATE
);

-- 贷款账户
CREATE TABLE ods.acct_loan (
    loan_id      VARCHAR(20) PRIMARY KEY,
    cust_id      VARCHAR(20),
    principal    NUMERIC(18,2),
    overdue_days INT,            -- 逾期天数, 用于不良判定
    status       VARCHAR(10),
    open_date    DATE
);

-- 交易流水: ⚠️埋坑#4 个别金额异常
CREATE TABLE ods.txn_flow (
    txn_id       VARCHAR(30) PRIMARY KEY,
    cust_id      VARCHAR(20),
    acct_id      VARCHAR(20),
    txn_amount   NUMERIC(18,2),
    txn_type     VARCHAR(10),
    txn_status   VARCHAR(10),    -- success/fail
    txn_time     TIMESTAMP
);

-- 产品
CREATE TABLE ods.prod_info (
    prod_id      VARCHAR(20) PRIMARY KEY,
    prod_name    VARCHAR(50),
    prod_type    VARCHAR(20)
);

-- 维度: 机构网点
CREATE TABLE ods.dim_org (
    org_id       VARCHAR(10) PRIMARY KEY,
    org_name     VARCHAR(50),
    region       VARCHAR(20)
);

-- ⚠️埋坑#6 僵尸表: 无人引用的冗余汇总表
CREATE TABLE ods.zombie_acct_summary_bak (
    acct_id      VARCHAR(20),
    snapshot     NUMERIC(18,2)
);
"""


def main():
    conn = psycopg2.connect(**DB)
    conn.autocommit = True
    cur = conn.cursor()
    print("创建 schema 与表 ...")
    cur.execute(DDL)

    orgs = [(f"O{i:03d}", fake.city() + "支行", random.choice(["华东", "华北", "华南", "西部"])) for i in range(1, 21)]
    cur.executemany("INSERT INTO ods.dim_org VALUES (%s,%s,%s)", orgs)

    prods = [
        ("P001", "活期存款", "deposit"), ("P002", "定期存款", "deposit"),
        ("P003", "稳健理财", "wealth"), ("P004", "个人消费贷", "loan"),
        ("P005", "房贷", "loan"),
    ]
    cur.executemany("INSERT INTO ods.prod_info VALUES (%s,%s,%s)", prods)

    print(f"生成 {N_CUST} 个客户 ...")
    cust_ids = []
    for i in range(N_CUST):
        cid = f"C{i:06d}"
        cust_ids.append(cid)
        ctype = random.choices(["retail", "corporate"], weights=[8, 2])[0]
        cur.execute(
            "INSERT INTO ods.cust_info VALUES (%s,%s,%s,%s,%s,%s,%s)",
            (cid, fake.name(), fake.ssn(), fake.phone_number()[:11], ctype,
             fake.date_between("-5y", "today"), random.choice(orgs)[0]),
        )
        # KYC 埋坑#4: 15% 概率字段为空
        rl = None if random.random() < 0.15 else random.choice(["low", "mid", "high"])
        occ = None if random.random() < 0.15 else fake.job()
        cur.execute("INSERT INTO ods.cust_kyc VALUES (%s,%s,%s)", (cid, rl, occ))

        # 存款账户
        bal = round(random.uniform(0, 500000), 2)
        if random.random() < 0.01:  # 埋坑#4: 1% 负余额
            bal = -abs(bal)
        cur.execute(
            "INSERT INTO ods.acct_deposit VALUES (%s,%s,%s,%s,%s,%s)",
            (f"D{i:06d}", cid, bal, "CNY",
             random.choice(["active", "frozen", "closed"]),
             fake.date_between("-5y", "today")),
        )
        # 部分客户有贷款
        if random.random() < 0.3:
            overdue = random.choices([0, random.randint(1, 120)], weights=[85, 15])[0]
            cur.execute(
                "INSERT INTO ods.acct_loan VALUES (%s,%s,%s,%s,%s,%s)",
                (f"L{i:06d}", cid, round(random.uniform(10000, 1000000), 2),
                 overdue, "active", fake.date_between("-3y", "today")),
            )

    print(f"生成 {N_TXN} 笔交易 ...")
    for i in range(N_TXN):
        cid = random.choice(cust_ids)
        amt = round(random.uniform(1, 50000), 2)
        if random.random() < 0.002:  # 埋坑#4: 极小概率异常巨额
            amt = round(random.uniform(1e8, 1e9), 2)
        cur.execute(
            "INSERT INTO ods.txn_flow VALUES (%s,%s,%s,%s,%s,%s,%s)",
            (f"T{i:08d}", cid, f"D{int(cid[1:]):06d}", amt,
             random.choice(["transfer", "consume", "deposit", "withdraw"]),
             random.choices(["success", "fail"], weights=[95, 5])[0],
             fake.date_time_between("-90d", "now")),
        )

    cur.close()
    conn.close()
    print("✅ 完成。已生成银行业模拟源数据 (含故意埋设的坑, 见 README)。")


if __name__ == "__main__":
    main()
