Title: IPT API
Date: 2018-02-26
Category: Rest APIs
Slug: ipt-api
Summary: Proceeding Search API
order:2

## _Proceeding Search API_ - <a href="https://git.euipo.europa.eu/projects/IPT/repos/proceeding-search-api/browse" target="_blank">BitBucket</a>

{% set EOPW_URI = 'search?query=type==RCD' %}
{% set PREFIX_DEV='dev'%}
{% set PREFIX_TEST='test'%}
{% set PREFIX_PREPROD='pp'%}
{% set PREFIX_PROD='production'%}
{% set APPLICATION_NAME='api.dev.oami.eu/proceeding-search-api'%}
{% set NETWORK_AWS='nonprod.aws.oami.eu'%}
{% set NETWORK_AWS_PROD='prod.aws.oami.eu'%}

- **AWS-Dev**:  http://{{PREFIX_DEV}}-{{APPLICATION_NAME}}/{{EOPW_URI}}
- **AWS-Test**:  http://{{PREFIX_TEST}}-{{APPLICATION_NAME}}/{{EOPW_URI}}
- **AWS-Prod**:  http://{{PREFIX_PROD}}-{{APPLICATION_NAME}}/{{EOPW_URI}}


