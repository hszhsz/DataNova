-- DWD 明细: 存款账户余额清洗
-- 清洗规则: 负余额(埋坑#4) 打标供 DQC Agent 识别
{{ config(materialized='table') }}

select
    acct_id,
    cust_id,
    balance,
    currency,
    status,
    open_date,
    case when balance < 0 then true else false end        as is_negative_balance
from {{ source('ods', 'acct_deposit') }}
