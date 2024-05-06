#query for prod environment
#this query will only be selected when the environment is prod
#this query has all the tables related to the prod gcp project
query="""select meta.correlationId as id, specversion, type, dataschema, datacontenttype, source, subject, meta.publishTime time, 
data,meta from (SELECT 
'1.0' as specversion,
'com.hsbc.wpb.fraud.customer.chagetelephones.gb.notifications.v1' as type,
'https://{schemaregistry}/hsbc/schemas/data/nonmon/1' as dataschema,
'application/json' as datacontenttype,
'/hsbc/<>/fraud/feedzai' as source,
'' as subject,
case when (cast(TRIM(Customer_Number) as int64) between 1100000000 and 1999999999) or (cast(TRIM(Customer_Number) as int64) between 0800000000 and 0999999999) then 'PERS'
when (cast(TRIM(Customer_Number) as int64) between 1000000000 and 1099999999) then 'BUSS' END as customerPortfolio)) as messageHeader,
struct(TRIM(Customer_Number) as customerNumber) as customerDetail,
struct('' as transactionTimestamp,
"" as changeEventOld,
TRIM(CIN_Create_Date) as changeEventNew,
'BusinessCreatedate' as changeEventReason,
'Insert' as changeEventDelivery) as transactionDetail )] as data,
struct(generate_uuid() as correlationId,
'Restricted' as dataClassification,
format_timestamp('%FT%X%Ez', current_timestamp) as publishTime,
'This is a customer demo event' as description) as meta
FROM `hsbc-10534429-sasefm-prod.f24_cdu_prod.SEFM_CUST_NON_PERS_VW`
)
"""
