-- DWD 明细: 交易清洗
-- 清洗规则: 过滤异常巨额(埋坑#4), 标准化交易类型与状态
{{ config(materialized='table') }}

select
    txn_id,
    cust_id,
    acct_id,
    txn_amount,
    txn_type,
    txn_status,
    txn_time,
    cast(txn_time as date)                                 as txn_date,
    -- 数据质量标记: 异常巨额(> 1亿) 打标而非删除, 供 DQC Agent 审计
    case when txn_amount > 100000000 then true else false end as is_amount_outlier
from {{ source('ods', 'txn_flow') }}
where txn_amount > 0
