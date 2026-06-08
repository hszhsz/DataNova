-- ADS 应用: 监管报送报表(简化)
-- ⚠️埋坑#5 血缘断裂: 本报表直接 from 一个写死的 schema.table (raw_regulatory.manual_input),
--   该表不在 dbt 管理范围、未声明为 source, 导致血缘无法回溯到 ODS。
--   元数据/血缘 Agent 应识别"血缘断点"并告警。
{{ config(materialized='table') }}

-- 注意: 此处故意绕过 ref()/source(), 直接硬编码外部表名
select
    report_date,
    deposit_total,
    loan_total,
    npl_ratio
from raw_regulatory.manual_input
