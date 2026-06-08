-- ADS 应用: 不良贷款率(NPL)报表
-- ⚠️埋坑#3: NPL 口径分散 — 此处用 overdue_days > 90 判定不良,
--   但风险域其他表可能用 status 或评级判定, 口径不统一, 待可信指标认证。
-- 不良率 = 不良贷款本金 / 贷款总本金
{{ config(materialized='table') }}

with loan as (
    select
        loan_id,
        principal,
        overdue_days,
        case when overdue_days > 90 then 1 else 0 end as is_npl
    from {{ source('ods', 'acct_loan') }}
    where status = 'active'
)
select
    current_date                                          as stat_date,
    sum(principal)                                        as total_principal,
    sum(case when is_npl = 1 then principal else 0 end)   as npl_principal,
    round(
        sum(case when is_npl = 1 then principal else 0 end)
        / nullif(sum(principal), 0), 4
    )                                                     as npl_ratio
from loan
