-- ⚠️埋坑#7 调度失败: 故意写一个会运行报错的 dbt 模型
--   错误点: 引用了不存在的字段 non_existent_column, 且除以零保护缺失。
--   运维/排障 Agent 应捕获报错、定位行号、给出修复建议。
{{ config(materialized='table') }}

select
    cust_id,
    non_existent_column / 0 as broken_metric   -- 故意: 字段不存在 + 除零
from {{ ref('dwd_cust_detail') }}
