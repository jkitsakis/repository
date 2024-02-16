Title: EEA APIs
Date: 2018-02-26
Category: Rest APIs
Slug: eea-apis
Summary: EEA APIs : EUTM Search API, Eutm Filing Api
order:3

{% set EOPW_URI = 'eop/eutm-search/trademarks?' %}
{% set PREFIX_DEV='dev'%}
{% set PREFIX_TEST='test'%}
{% set PREFIX_PROD='production'%}
{% set APPLICATION_NAME='eutm-search-api'%}
{% set NETWORK_AWS='nonprod.aws.oami.eu'%}
{% set NETWORK_AWS_PROD='prod.aws.oami.eu'%}

## _EUTM Search API_ - <a href="https://git.euipo.europa.eu/projects/EEA/repos/eutm-search-api/browse" target="_blank">BitBucket</a>

- **AWS-Dev**:  http://{{PREFIX_DEV}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{EOPW_URI}}
- **AWS-Test**:  http://{{PREFIX_TEST}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{EOPW_URI}}
- **AWS-Prod**:  http://{{PREFIX_PROD}}-{{APPLICATION_NAME}}.{{NETWORK_AWS_PROD}}/{{EOPW_URI}}


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
> query=representatives.identifier==10014
 
> query=status==REGISTERED,markFeature==FIGURATIVE&page=0&fields=trademarks(applicationNumber)&sort=registrationDate:desc

> query=status==REGISTERED,markFeature==FIGURATIVE&page=0&fields=trademarks(applicationNumber,status)&sort=status:asc,applicationNumber:asc

> query=representatives.identifier==10014 and (applicantReference==IF/mb or applicationNumber==IF/mb)&page=0&sort=applicationDate:desc

> query=applicantReference==IF/mb or applicationNumber==IF/mb&page=0&sort=applicationDate:desc

> page=0&size=25&query=markBasis==EU_TRADEMARK and applicationNumber=='*012345*'&sort=applicationDate:desc

> query=markBasis==EU_TRADEMARK and status=in=(ACCEPTED)&page=0&sort=applicationDate:desc&size=1000

> query=markBasis==INTERNATIONAL_TRADEMARK and status=in=(ACCEPTED,REGISTERED)&page=0&sort=applicationDate:desc&size=1000

> query=representatives.identifier==10014 and markFeature==FIGURATIVE&page=0&sort=applicationDate:desc&size=10

> query=(markBasis==INTERNATIONAL_TRADEMARK and niceClasses=in=(1,2,3)) and representatives.identifier==10014&page=0&size=25&sort=applicationDate:desc

> trademarks/:applicationNumber

> trademarks/:applicationNumber/image 


-------

## _Eutm Filing Api_ - <a href="https://git.euipo.europa.eu/projects/EEA/repos/eutm-filing-api/browse" target="_blank">BitBucket</a>

{% set EOPW_URI = 'eop/eutm-filing/' %}
{% set APPLICATION_NAME = 'eutm-filing-api' %}

- **AWS-Dev**:  http://{{PREFIX_DEV}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{EOPW_URI}}
- **AWS-Test**:  http://{{PREFIX_TEST}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{EOPW_URI}}
- **AWS-Prod**:  http://{{PREFIX_PROD}}-{{APPLICATION_NAME}}.{{NETWORK_AWS_PROD}}/{{EOPW_URI}}


<details>
<summary>Legacy links</summary>
<ul>
  <li>**Integration**:  http://int-api.dev.oami.eu/{{EOPW_URI}}</li>
  <li>**PreProd**:  http://pp-api.test.oami.eu/{{EOPW_URI}}</li>
  <li>**Test**:  http://test-eutm-api.test.oami.eu/{{EOPW_URI}}</li>
  <li>**Prod**:  http://api.prod.oami.eu/{{EOPW_URI}}</li>
</ul>
</details>