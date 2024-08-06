Title: EEE APIs
Date: 2018-02-26
Category: Rest APIs
Slug: eee-apis
Summary: EEE APIs : EOP EUTM eForms - eutm-eform-backend
order: 4

{% set EOPW_URI = 'eutm-efiling/app/api/' %}
{% set PREFIX_DEV='dev'%}
{% set PREFIX_TEST='test'%}
{% set PREFIX_PROD='production'%}
{% set APPLICATION_NAME='eutm-eform-backend'%}
{% set NETWORK_AWS='nonprod.aws.oami.eu'%}
{% set NETWORK_AWS_PROD='prod.aws.oami.eu'%}

## _EOP EUTM eForms_ - <a href="https://git.euipo.europa.eu/projects/EEE/repos/eutm-eform-backend/browse" target="_blank">BitBucket</a>

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



