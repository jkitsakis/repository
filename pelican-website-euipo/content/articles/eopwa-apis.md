Title: EOPWA APIs
Date: 2018-02-26
Category: Rest APIs
Slug: eopwa-apis
Summary: EOPWA APIs : Appeals Search API, Communications API, Designs Search API, Drafts Search API, Feedback Search API, Interpartes Search API, User Profile Api
order: 01
Tag: EOPWA APIs : Appeals Search API, Communications API, Designs Search API, Drafts Search API, Feedback Search API, Interpartes Search API, User Profile Api

{% set EOPW_URI = 'eop/appeals-search' %}
{% set PREFIX_DEV='dev'%}
{% set PREFIX_TEST='test'%}
{% set PREFIX_PROD='production'%}
{% set APPLICATION_NAME='appeals-search-api'%}
{% set NETWORK_AWS='nonprod.aws.oami.eu'%}
{% set NETWORK_AWS_PROD='prod.aws.oami.eu'%}

## _Appeals Search API_ - <a href="https://git.euipo.europa.eu/projects/EOPWA/repos/appeals-search-api/browse" target="_blank">BitBucket</a> - <a href="https://argocd-dev.nonprod.aws.oami.eu/applications/argocd/website-api-dev-aws?view=tree&resource=" target="_blank">ArgoCD</a>


- **AWS-Dev**:  http://{{PREFIX_DEV}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{EOPW_URI}}
- **AWS-Test**:  http://{{PREFIX_TEST}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{EOPW_URI}}
- **AWS-Prod**:  http://{{PREFIX_PROD}}-{{APPLICATION_NAME}}.{{NETWORK_AWS_PROD}}/{{EOPW_URI}}

<details>
<summary>Legacy links</summary>
<ul>
  <li> **Integration**:  http://int-api.dev.oami.eu/{{EOPW_URI}}</li>
  <li> **PreProd**:  http://pp-api.test.oami.eu/{{EOPW_URI}}</li>
  <li> **Test**:  http://test-api.test.oami.eu/{{EOPW_URI}}</li>
</ul>
</details>

_Syntax_ 

> ... ?query=appealNumber=='R00*'&roleKind=CLAIMANT&page=0&size=25&sort=appealDate:desc

-------------------

## Communications Search API - <a href="https://git.euipo.europa.eu/projects/EOPWA/repos/communications-api/browse" target="_blank">BitBucket</a>
{% set EOPW_URI = 'eop/communications/' %}
{% set APPLICATION_NAME = 'communications-api' %}
- **AWS-Dev**:  http://{{PREFIX_DEV}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{EOPW_URI}}
- **AWS-Test**:  http://{{PREFIX_TEST}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{EOPW_URI}}
- **AWS-Prod**:  http://{{PREFIX_PROD}}-{{APPLICATION_NAME}}.{{NETWORK_AWS_PROD}}/{{EOPW_URI}}

<details>
<summary>Legacy links</summary>
<ul>
  <li> **Integration**:  http://int-api.dev.oami.eu/{{EOPW_URI}}</li>
  <li> **PreProd**:  http://pp-api.test.oami.eu/{{EOPW_URI}}</li>
  <li> **Test**:  http://test-api.test.oami.eu/{{EOPW_URI}}</li>
</ul>
</details>

-------------------

## Designs Search API - <a href="https://git.euipo.europa.eu/projects/EOPWA/repos/design-search-api/browse" target="_blank">BitBucket</a>
{% set EOPW_URI = 'eop/design-search/' %}
{% set APPLICATION_NAME = 'design-search-api' %}
- **AWS-Dev**:  http://{{PREFIX_DEV}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{EOPW_URI}}
- **AWS-Test**:  http://{{PREFIX_TEST}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{EOPW_URI}}
- **AWS-Prod**:  http://{{PREFIX_PROD}}-{{APPLICATION_NAME}}.{{NETWORK_AWS_PROD}}/{{EOPW_URI}}

<details>
<summary>Legacy links</summary>
<ul>
  <li> **Integration**:  http://int-api.dev.oami.eu/{{EOPW_URI}}</li>
  <li> **PreProd**:  http://pp-api.test.oami.eu/{{EOPW_URI}}</li>
  <li> **Test**:  http://test-api.test.oami.eu/{{EOPW_URI}}</li>
</ul>
</details>

_Syntax_ 
> ... ?query=designNumber!=9*&size=10&page=0&sort=applicationDate:desc

-------------------

## Drafts Search API - <a href="https://git.euipo.europa.eu/projects/EOPWA/repos/drafts-api/browse" target="_blank">BitBucket</a>

{% set EOPW_URI = 'eop/drafts' %}
{% set APPLICATION_NAME = 'drafts-api' %}
- **AWS-Dev**:  http://{{PREFIX_DEV}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{EOPW_URI}}
- **AWS-Test**:  http://{{PREFIX_TEST}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{EOPW_URI}}
- **AWS-Prod**:  http://{{PREFIX_PROD}}-{{APPLICATION_NAME}}.{{NETWORK_AWS_PROD}}/{{EOPW_URI}}


### eutms: /drafts/eutms?size=10&page=0&sort=creationDate:DESC

### designs: /drafts/designs?size=10&page=0&sort=creationDate:DESC

### interpartes: /drafts/interpartes?page=0&size=10&actions=OPPOSITION&sort=draftdate:desc

### other: /drafts/other?size=10&page=0&sort=creationDate:DESC

<details>
<summary>Legacy links</summary>
<ul>
  <li> **Integration**:  http://int-api.dev.oami.eu/{{EOPW_URI}}</li>
  <li> **PreProd**:  http://pp-api.test.oami.eu/{{EOPW_URI}}</li>
  <li> **Test**:  http://test-api.test.oami.eu/{{EOPW_URI}}</li>
</ul>
</details>

-------------------

## Feedback Search API - <a href="https://git.euipo.europa.eu/projects/EOPWA/repos/feedback-api/browse" target="_blank">BitBucket</a>

{% set EOPW_URI = 'eop/feedback/surveys/:indentifier' %}
{% set APPLICATION_NAME = 'feedback-api' %}
- **AWS-Dev**:  http://{{PREFIX_DEV}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{EOPW_URI}}
- **AWS-Test**:  http://{{PREFIX_TEST}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{EOPW_URI}}
- **AWS-Prod**:  http://{{PREFIX_PROD}}-{{APPLICATION_NAME}}.{{NETWORK_AWS_PROD}}/{{EOPW_URI}}

<details>
<summary>Legacy links</summary>
<ul>
  <li> **Integration**:  http://int-api.dev.oami.eu/{{EOPW_URI}}</li>
  <li> **PreProd**:  http://pp-api.test.oami.eu/{{EOPW_URI}}</li>
  <li> **Test**:  http://test-api.test.oami.eu/{{EOPW_URI}}</li>
</ul>
</details>

-------------------

## Interpartes Search API - <a href="https://git.euipo.europa.eu/projects/EOPWA/repos/interpartes-search-api/browse" target="_blank">BitBucket</a>

{% set EOPW_URI = 'eop/interpartes-search' %}
{% set APPLICATION_NAME = 'interpartes-search-api' %}
- **AWS-Dev**:  http://{{PREFIX_DEV}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{EOPW_URI}}
- **AWS-Test**:  http://{{PREFIX_TEST}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{EOPW_URI}}
- **AWS-Prod**:  http://{{PREFIX_PROD}}-{{APPLICATION_NAME}}.{{NETWORK_AWS_PROD}}/{{EOPW_URI}}


### oppositions: /oppositions?query=opponentRepresentatives.identifier==10014&size=100&page=0&sort=oppositionDate:desc

### cancellations: /cancellations?page=0&sort=cancellationNumber:desc&size=160

### invalidities: /invalidities?query=claimantRepresentatives.name=="HO+*"&size=100&page=0&sort=invalidityDate:desc

<details>
<summary>Legacy links</summary>
<ul>
  <li> **Integration**:  http://int-api.dev.oami.eu/{{EOPW_URI}}</li>
  <li> **PreProd**:  http://pp-api.test.oami.eu/{{EOPW_URI}}</li>
  <li> **Test**:  http://test-api.test.oami.eu/{{EOPW_URI}}</li>
</ul>
</details>

-------------------

## Notes Search API - <a href="https://git.euipo.europa.eu/projects/EOPWA/repos/notes-api/browse" target="_blank">BitBucket</a>

{% set EOPW_URI = 'eop/notes/' %}
{% set APPLICATION_NAME = 'notes-api' %}
- **AWS-Dev**:  http://{{PREFIX_DEV}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{EOPW_URI}}
- **AWS-Test**:  http://{{PREFIX_TEST}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{EOPW_URI}}
- **AWS-Prod**:  http://{{PREFIX_PROD}}-{{APPLICATION_NAME}}.{{NETWORK_AWS_PROD}}/{{EOPW_URI}}

<details>
<summary>Legacy links</summary>
<ul>
  <li> **Integration**:  http://int-api.dev.oami.eu/{{EOPW_URI}}</li>
  <li> **PreProd**:  http://pp-api.test.oami.eu/{{EOPW_URI}}</li>
  <li> **Test**:  http://test-api.test.oami.eu/{{EOPW_URI}}</li>
</ul>
</details>

---------------------

## Pre-Assesement Search API - <a href="https://git.euipo.europa.eu/projects/EOPWA/repos/pre-assessment-api/browse" target="_blank">BitBucket</a>

{% set EOPW_URI = 'eop/pre-assessment/' %}
{% set APPLICATION_NAME = 'pre-assessment-api' %}
- **AWS-Dev**:  http://{{PREFIX_DEV}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{EOPW_URI}}
- **AWS-Test**:  http://{{PREFIX_TEST}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{EOPW_URI}}
- **AWS-Prod**:  http://{{PREFIX_PROD}}-{{APPLICATION_NAME}}.{{NETWORK_AWS_PROD}}/{{EOPW_URI}}

<details>
<summary>Legacy links</summary>
<ul>
  <li> **Integration**:  http://int-api.dev.oami.eu/{{EOPW_URI}}</li>
  <li> **PreProd**:  http://pp-api.test.oami.eu/{{EOPW_URI}}</li>
  <li> **Test**:  http://test-api.test.oami.eu/{{EOPW_URI}}</li>
</ul>
</details>


-------------------------

## Settings Search API - <a href="https://git.euipo.europa.eu/projects/EOPWA/repos/settings-api/browse" target="_blank">BitBucket</a>

{% set EOPW_URI = 'eop/settings/' %}
{% set APPLICATION_NAME = 'settings-api' %}
- **AWS-Dev**:  http://{{PREFIX_DEV}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{EOPW_URI}}
- **AWS-Test**:  http://{{PREFIX_TEST}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{EOPW_URI}}
- **AWS-Prod**:  http://{{PREFIX_PROD}}-{{APPLICATION_NAME}}.{{NETWORK_AWS_PROD}}/{{EOPW_URI}}

<details>
<summary>Legacy links</summary>
<ul>
  <li> **Integration**:  http://int-api.dev.oami.eu/{{EOPW_URI}}</li>
  <li> **PreProd**:  http://pp-api.test.oami.eu/{{EOPW_URI}}</li>
  <li> **Test**:  http://test-api.test.oami.eu/{{EOPW_URI}}</li>
</ul>
</details>

-----------------------------

## User Profile API - <a href="https://git.euipo.europa.eu/projects/EOPWA/repos/user-profile-api/browse" target="_blank">BitBucket</a>

{% set EOPW_URI = 'eop/user-profile/' %}
{% set APPLICATION_NAME = 'user-profile-api' %}
- **AWS-Dev**:  http://{{PREFIX_DEV}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{EOPW_URI}}
- **AWS-Test**:  http://{{PREFIX_TEST}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{EOPW_URI}}
- **AWS-Prod**:  http://{{PREFIX_PROD}}-{{APPLICATION_NAME}}.{{NETWORK_AWS_PROD}}/{{EOPW_URI}}

<details>
<summary>Legacy links</summary>
<ul>
  <li> **Integration**:  http://int-api.dev.oami.eu/{{EOPW_URI}}</li>
  <li> **PreProd**:  http://pp-api.test.oami.eu/{{EOPW_URI}}</li>
  <li> **Test**:  http://test-api.test.oami.eu/{{EOPW_URI}}</li>
</ul>
</details>
