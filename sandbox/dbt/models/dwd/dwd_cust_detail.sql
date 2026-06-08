-- DWD 明细: 客户清洗 + 脱敏
-- 合规要求: 敏感字段在 DWD 层脱敏 (对照 ODS 埋坑#2 的明文)
-- 身份证保留首6+末4, 手机号保留首3+末4
{{ config(materialized='table') }}

select
    cust_id,
    cust_name,
    -- C4: 身份证脱敏
    case when length(id_card_no) = 18
         then substr(id_card_no, 1, 6) || '********' || substr(id_card_no, 15, 4)
         else '***' end                                   as id_card_masked,
    -- C3: 手机号脱敏
    case when length(mobile) = 11
         then substr(mobile, 1, 3) || '****' || substr(mobile, 8, 4)
         else '***' end                                   as mobile_masked,
    cust_type,
    open_date,
    org_id
from {{ source('ods', 'cust_info') }}
