Title: EPA APIs
Date: 2018-02-26
Category: Rest APIs
Slug: epa-apis
Summary: EPA APIs : EOP Persons API
order: 06

## _EUTM Search API_ - <a href="https://git.euipo.europa.eu/projects/EPA/repos/persons-api/browse" target="_blank">BitBucket</a>

{% set EOPW_URI = 'eop/persons/applicants?name=S%26P' %}
{% set PREFIX_DEV='dev'%}
{% set PREFIX_TEST='test'%}
{% set PREFIX_PROD='production'%}
{% set APPLICATION_NAME='persons-api'%}
{% set NETWORK_AWS='nonprod.aws.oami.eu'%}
{% set NETWORK_AWS_PROD='prod.aws.oami.eu'%}

- **AWS-Dev**:  http://{{PREFIX_DEV}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{EOPW_URI}}
- **AWS-Test**:  http://{{PREFIX_TEST}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{EOPW_URI}}
- **AWS-Prod**:  http://{{PREFIX_PROD}}-{{APPLICATION_NAME}}.{{NETWORK_AWS_PROD}}/{{EOPW_URI}}

<details>
<summary>Legacy links</summary>
<ul>
  <li> **Integration** : http://int-api.dev.oami.eu/{{EOPW_URI}}</li>
  <li> **PreProd**: http://pp-api.test.oami.eu/{{EOPW_URI}}</li>
  <li> **Test**: http://test-api.test.oami.eu/{{EOPW_URI}}</li>
  <li> **Prod**: http://api.prod.oami.eu</li>
</ul>
</details>

