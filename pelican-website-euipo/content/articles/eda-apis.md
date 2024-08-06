Title: EDA APIs
Date: 2018-02-26
Category: Rest APIs
Slug: eda-apis
Summary: EDA APIs : Design Filing API
order: 09

## _Design Filing API_ - <a href="https://git.euipo.europa.eu/projects/EDA/repos/design-filing-api/browse" target="_blank">BitBucket</a> - <a href="https://argocd-dev.nonprod.aws.oami.eu/applications/argocd/design-api-dev-aws?view=tree&resource=" target="_blank">ArgoCD Dev</a>



{% set EOPW_URI = 'eop/design-filing/' %}
{% set PREFIX_DEV='dev'%}
{% set PREFIX_TEST='test'%}
{% set PREFIX_PROD='production'%}
{% set APPLICATION_NAME='design-filing-api'%}
{% set NETWORK_AWS='nonprod.aws.oami.eu'%}
{% set NETWORK_AWS_PROD='prod.aws.oami.eu'%}

- **AWS-Dev**:  http://{{PREFIX_DEV}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{EOPW_URI}}
- **AWS-Test**:  http://{{PREFIX_TEST}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{EOPW_URI}}
- **AWS-Prod**:  http://{{PREFIX_PROD}}-{{APPLICATION_NAME}}.{{NETWORK_AWS_PROD}}/{{EOPW_URI}}  
<br/>
---------------------  
_Syntax_  
> templates?keyword=template1&page.page=0&page.size=10&page.sort=draftdate&page.sort.dir=asc

> templates/78023ccc-2a91-49aa-b759-3e1c19cdaa10/documents/012e81f5-00d3-45de-a60f-ee55ffe53d13/export  

> templates/78023ccc-2a91-49aa-b759-3e1c19cdaa10/lock  

> templates/78023ccc-2a91-49aa-b759-3e1c19cdaa10/notes  

> templates/78023ccc-2a91-49aa-b759-3e1c19cdaa10/application  


---------------------
<br/>
Databases:  

1. First item
	- uri: mongodb://${var.datasource.rcd-api.username}:${var.datasource.rcd-api.password}@ocvli-dbh605.dev.oami.eu:27000/?authSource=admin
		- database: rcd_filing_api_adap  
		- username: rcd_filing_api_adap  
		- password: Hjf9OlG#XLKY   
	  
	  

2. ( manifest/helm/config/design-filing-api/application-dev.yaml)  
	- uri: mongodb://${var.datasource.rcd-api.username}:${var.datasource.rcd-api.password}@iac-docdb-iacdeveuc1docdb.cluster-cr3azsaqamcu.eu-central-1.docdb.amazonaws.com:27017/?authSource=admin  
		- parameters: "readPreference=primaryPreferred&retryWrites=false"  
		- database: rcd_filing_api_adap  



