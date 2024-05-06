#query for dev environment
#this query will only be selected when the environment is dev
#this query has all the tables related to the dev gcp project
query="""select meta.correlationId as id, specversion, type, dataschema, datacontenttype, source, subject, meta.publishTime time, 
data,meta from (SELECT 
'1.0' as specversion,
'com.hsbc.wpb.fraud.customer.chagetelephones.gb.notifications.v1' as type,
'https://{schemaregistry}/hsbc/schemas/data/nonmon/1' as dataschema,
'application/json' as datacontenttype,
'/hsbc/<>/fraud/feedzai' as source,
'' as subject,
--current_datetime() as time,
[struct(case when TRIM(Institution_Id)='1' then 'MS_COP'
when  TRIM(Institution_Id)='3' or TRIM(Institution_Id)='S' then 'PB_COP'
when  TRIM(Institution_Id)='O' then 'CIOM_COP' 
when  TRIM(Institution_Id)='Z' then 'EXPT_COP'
when  TRIM(Institution_Id)='F' then 'FD_COP' 
ELSE 'UK_COP' END as source, 'UK_CDM' as appSource,(struct(
struct('' as transactionTimestamp,
"" as changeEventOld,
TRIM(CIN_Create_Date) as changeEventNew,
'BusinessCreatedate' as changeEventReason,
'Insert' as changeEventDelivery) as transactionDetail )] as data,
struct(generate_uuid() as correlationId,
'Restricted' as dataClassification,
format_timestamp('%FT%X%Ez', current_timestamp) as publishTime,
'This is a customer demo event' as description) as meta
FROM `hsbc-10534429-sasefm-dev.f24_cdu.SEFM_CUST_NON_PERS_VW`
)
"""
