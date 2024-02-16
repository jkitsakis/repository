Title: EOPW APIs
Date: 2018-02-26
Category: Rest APIs
Slug: eopw-apis
Summary: EOPW APIs : Website BE, Admin Tool, Story Block
order:6

{% set EOPW_URI = 'portal/app/api' %}
{% set PREFIX_DEV='dev'%}
{% set PREFIX_TEST='test'%}
{% set PREFIX_PROD='production'%}
{% set APPLICATION_NAME='website-backend'%}
{% set NETWORK_AWS='nonprod.aws.oami.eu'%}
{% set NETWORK_AWS_PROD='prod.aws.oami.eu'%}

## _Website BE_ - <a href="https://git.euipo.europa.eu/projects/EOPW/repos/eop-website-backend/browse" target="_blank">BitBucket</a>

- **AWS-Dev**:  http://{{PREFIX_DEV}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{EOPW_URI}}
- **AWS-Test**:  http://{{PREFIX_TEST}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{EOPW_URI}}
- **AWS-Prod**:  http://{{PREFIX_PROD}}-{{APPLICATION_NAME}}.{{NETWORK_AWS_PROD}}/{{EOPW_URI}}

---------------------
<details>
<summary>Legacy links</summary>
<ul>
  <li>**Integration**:  https://integration.euipo.europa.eu/{{EOPW_URI}}</li>
  <li>**PreProd**:  https://pp.euipo.europa.eu/{{EOPW_URI}}</li>
  <li>**Prod**:  https://www.euipo.europa.eu/{{EOPW_URI}}</li>
</ul>
</details>
---------------------

<details>
<summary>Syntax</summary>
<ul>
<li>templates?page=0&size=10&sort=creationDate:desc</li>
<li>templates/:templateIdentifier/notes</li>
<li>drafts/designs</li>
<li>drafts/interpartes?keyword&size=5&page=0&sort=draftdate:DESC</li>
<li>drafts/interpartes?page=0&size=5&sort=draftdate%3Adesc</li>
<li>drafts/other?keyword&size=5&page=0&sort=draftdate:DESC</li>
<li>portfolio/trademarks?keyword=IF/mb&size=10&page=0&sort=applicationDate:desc</li>
<li>portfolio/trademarks?query=markBasis==EU_TRADEMARK and status=in=(ACCEPTANCE_PENDING,ACCEPTED)&page=0&sort=applicationDate:desc
</li>
<li>portfolio/oppositions?size=10&roleKind=CLAIMANT&page=0&sort=oppositionDate:desc</li>
<li>portfolio/oppositions?roleKind=CLAIMANT&size=10&page=0&sort=oppositionDate:desc&query=status=in=(ADMISSIBILITY_CHECK)
</li>
<li>portfolio/oppositions?size=50&page=0&roleKind=CLAIMANT</li>
<li>portfolio/trademarks?keyword=IF/mb&size=10&page=0&sort=applicationDate:desc</li>
<li>portfolio/trademarks/:applicationNumber</li>
<li>portfolio/oppositions/:oppositionId</li>
<li>portfolio/cancellations?size=20&page=0&roleKind=CLAIMANT</li>
<li>portfolio/designs?page=0&sort=applicationDate:desc&size=20&query=keyword==DM416DR</li>
<li>portfolio/designs?size=200&page=0&query=designNumber!=0</li>
<li>portfolio/designs?size=200&page=0&query=designNumber==000094560-0006</li>
<li>portfolio/designs/001754292-0001/comments</li>
<li>portfolio/appeals?page=0&size=25&roleKind=CLAIMANT&query=appealDate%3E%3D2022-05-01&sort=appealDate%3Adesc
</li>
<li>userprofile/:documentId/export</li>
<li>surveys/:identifier</li>
<li>surveys/:identifier/answer</li>
</ul>

</details>

---- 

## _Admin Tool_ - <a href="https://git.euipo.europa.eu/projects/EOPW/repos/eop-admintool-backend/browse" target="_blank">BitBucket</a>
{% set EOPW_URI = 'eop/admintool/app/api/' %}
{% set APPLICATION_NAME = 'eop-admintool-backend' %}
- **AWS-Dev**:  http://{{PREFIX_DEV}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{EOPW_URI}}
- **AWS-Test**:  http://{{PREFIX_TEST}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{EOPW_URI}}
- **AWS-Prod**:  http://{{PREFIX_PROD}}-{{APPLICATION_NAME}}.{{NETWORK_AWS_PROD}}/{{EOPW_URI}}

---------------------
<details>
<summary>Legacy links</summary>
<ul>
  <li>**Integration**:  https://integration.euipo.europa.eu/{{EOPW_URI}}</li>
  <li>**PreProd**:  https://pp.euipo.europa.eu/{{EOPW_URI}}</li>
  <li>**Prod**:  https://www.euipo.europa.eu/{{EOPW_URI}}</li>
</ul>
</details>
---------------------


## _Story Blok_ - <a href="https://git.euipo.europa.eu/projects/EOPW/repos/eop-storyblok-api/browse" target="_blank">BitBucket</a>
{% set EOPW_URI = 'eop/storyblok/' %}
{% set APPLICATION_NAME = 'storyblok-api' %}
- **AWS-Dev**:  http://{{PREFIX_DEV}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{EOPW_URI}}
- **AWS-Test**:  http://{{PREFIX_TEST}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{EOPW_URI}}
- **AWS-Prod**:  http://{{PREFIX_PROD}}-{{APPLICATION_NAME}}.{{NETWORK_AWS_PROD}}/{{EOPW_URI}}


---------------------
<details>
<summary>Legacy links</summary>
<ul>
  <li>**Integration**:  https://integration.euipo.europa.eu/{{EOPW_URI}}</li>
  <li>**PreProd**:  https://pp.euipo.europa.eu/{{EOPW_URI}}</li>
  <li>**Prod**:  https://www.euipo.europa.eu/{{EOPW_URI}}</li>
</ul>
</details>
---------------------
