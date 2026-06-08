-- DIM 维度: 机构网点
{{ config(materialized='table') }}

select
    org_id,
    org_name,
    region
from {{ source('ods', 'dim_org') }}
