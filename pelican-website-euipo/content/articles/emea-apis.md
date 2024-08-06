Title: EMEA APIs
Date: 2018-02-26
Category: Rest APIs
Slug: emea-apis
Summary: EMEA APIs : Me API
order: 05

{% set EOPW_URI = 'eop/me/' %}
{% set PREFIX_DEV='dev'%}
{% set PREFIX_TEST='test'%}
{% set PREFIX_PROD='production'%}
{% set APPLICATION_NAME='me-api'%}
{% set NETWORK_AWS='nonprod.aws.oami.eu'%}
{% set NETWORK_AWS_PROD='prod.aws.oami.eu'%}

## _Me API_ - <a href="https://git.euipo.europa.eu/projects/EMEA/repos/me-api/browse" target="_blank">BitBucket</a> - <a href="https://argocd-dev.nonprod.aws.oami.eu/applications/me-api-dev-aws?resource=" target="_blank">ArgoCD</a>


- **AWS-Dev**:  http://{{PREFIX_DEV}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{EOPW_URI}}
- **AWS-Test**:  http://{{PREFIX_TEST}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{EOPW_URI}}
- **AWS-Prod**:  http://{{PREFIX_PROD}}-{{APPLICATION_NAME}}.{{NETWORK_AWS_PROD}}/{{EOPW_URI}}

---------------------

<details>
<summary>Legacy links</summary>
<ul>
  <li>**Integration**:  http://int-api.dev.oami.eu/{{EOPW_URI}}</li>
  <li>**PreProd**:  http://pp-api.test.oami.eu/{{EOPW_URI}}</li>
  <li>**Test**:  http://test-eutm-api.test.oami.eu/{{EOPW_URI}}</li>
  <li>**Prod**:  http://api.prod.oami.eu/{{EOPW_URI}}</li>
</ul>
</details>


---------------------

_Syntax_

> /trademarks?keyword=IF/mb&page=0&size=10&sort=applicationDate:desc

> /oppositions?size=10&page=0

> /cancellations?sort=cancellationDate:desc&roleKind=DEFENDANT

> /designs?size=200&page=0&query=designNumber!=0
