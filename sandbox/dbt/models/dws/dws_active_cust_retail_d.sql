-- DWS 汇总: 活跃客户(零售口径) — 近 30 天有成功交易
-- ⚠️埋坑#1(其一): 零售口径定义为"近30天", 与对公口径(近90天)冲突
-- 指标治理 Agent 应发现两个口径并提示统一
{{ config(materialized='table') }}

select distinct
    cust_id,
    '零售口径_近30天' as active_caliber
from {{ ref('dwd_txn_detail') }}
where txn_status = 'success'
  and txn_date >= current_date - interval '30 day'
