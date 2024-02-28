Title: IM - Infrastructure Microservices
Date: 2018-02-26
Category: Rest APIs
Slug: im-api
Summary: document-generator , document-repository
order:8

## _Infrastructure Microservices_ - <a href="https://git.euipo.europa.eu/projects/IM" target="_blank">BitBucket</a>

{% set GENERATOR_URI = 'eop/document-generator' %}
{% set REPOSITORY_URI = 'eop/document-repository' %}
{% set PREFIX_DEV='dev'%}
{% set PREFIX_TEST='test'%}
{% set PREFIX_PREPROD='pp'%}
{% set PREFIX_PROD='production'%}
{% set GENERATOR_APP_NAME='document-generator'%}
{% set REPOSITORY_APP_NAME='document-repository'%}
{% set NETWORK_AWS='nonprod.aws.oami.eu'%}
{% set NETWORK_AWS_PROD='prod.aws.oami.eu'%}

**{{GENERATOR_APP_NAME}}**

- **AWS-Dev**:  http://{{PREFIX_DEV}}-{{GENERATOR_APP_NAME}}.{{NETWORK_AWS}}/{{GENERATOR_URI}}
- **AWS-Test**:  http://{{PREFIX_TEST}}-{{GENERATOR_APP_NAME}}.{{NETWORK_AWS}}/{{GENERATOR_URI}}
- **AWS-PreProd**:  http://{{PREFIX_PREPROD}}-{{GENERATOR_APP_NAME}}.{{NETWORK_AWS}}/{{GENERATOR_URI}}
- **AWS-Prod**:  http://{{PREFIX_PROD}}-{{GENERATOR_APP_NAME}}.{{NETWORK_AWS_PROD}}/{{GENERATOR_URI}}

----

**{{REPOSITORY_APP_NAME}}**

- **AWS-Dev**:  http://{{PREFIX_DEV}}-{{REPOSITORY_APP_NAME}}.{{NETWORK_AWS}}/{{REPOSITORY_URI}}
- **AWS-Test**:  http://{{PREFIX_TEST}}-{{REPOSITORY_APP_NAME}}.{{NETWORK_AWS}}/{{REPOSITORY_URI}}
- **AWS-PreProd**:  http://{{PREFIX_PREPROD}}-{{REPOSITORY_APP_NAME}}.{{NETWORK_AWS}}/{{REPOSITORY_URI}}
- **AWS-Prod**:  http://{{PREFIX_PROD}}-{{REPOSITORY_APP_NAME}}.{{NETWORK_AWS_PROD}}/{{REPOSITORY_URI}}
