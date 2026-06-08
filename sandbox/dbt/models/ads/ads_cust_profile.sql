-- ADS 应用: 客户画像宽表
-- 聚合客户基础信息 + 资产 + 活跃状态(零售口径), 供营销/画像应用
{{ config(materialized='table') }}

select
    c.cust_id,
    c.cust_name,
    c.cust_type,
    c.org_id,
    coalesce(a.deposit_balance, 0)                         as deposit_balance,
    coalesce(a.deposit_acct_cnt, 0)                        as deposit_acct_cnt,
    case when r.cust_id is not null then '活跃' else '沉默' end as activity_status
from {{ ref('dwd_cust_detail') }} c
left join {{ ref('dws_cust_asset_d') }} a       on c.cust_id = a.cust_id
left join {{ ref('dws_active_cust_retail_d') }} r on c.cust_id = r.cust_id
