-- DWS 汇总: 客户资产日汇总 (AUM 雏形)
-- 客户粒度的存款余额汇总, 供 ADS 客户画像与 AUM 指标使用
{{ config(materialized='table') }}

select
    b.cust_id,
    current_date                                           as stat_date,
    sum(b.balance)                                         as deposit_balance,
    count(distinct b.acct_id)                              as deposit_acct_cnt
from {{ ref('dwd_acct_balance') }} b
where b.status = 'active'
group by b.cust_id
