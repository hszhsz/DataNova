-- DWS 汇总: 活跃客户(对公口径) — 近 90 天有成功交易
-- ⚠️埋坑#1(其二): 对公口径定义为"近90天", 与零售口径(近30天)冲突
-- 同一个"活跃客户"指标存在两套时间窗口, 是典型的口径不一致问题
{{ config(materialized='table') }}

select distinct
    cust_id,
    '对公口径_近90天' as active_caliber
from {{ ref('dwd_txn_detail') }}
where txn_status = 'success'
  and txn_date >= current_date - interval '90 day'
