Title: EGA APIs
Slug: ega-apis
Summary: EGA APIs : gs-loader, gs-lists, gs-api
order: 11

{% set URI = 'ega/gs-api' %}
{% set PREFIX_DEV='dev'%}
{% set PREFIX_TEST='test'%}
{% set PREFIX_PROD='production'%}
{% set APPLICATION_NAME='gs-api'%}
{% set NETWORK_AWS='nonprod.aws.oami.eu'%}
{% set NETWORK_AWS_PROD='prod.aws.oami.eu'%}

## _gs-api_ - <a href="https://git.euipo.europa.eu/projects/EGA/repos/gs-api/browse" target="_blank">BitBucket</a> - <a href="https://argocd-dev.nonprod.aws.oami.eu/applications/argocd/gs-api-dev-aws?view=tree&resource=" target="_blank">ArgoCD</a>


- **AWS-Dev**:  http://{{PREFIX_DEV}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{URI}}
- **AWS-Test**:  http://{{PREFIX_TEST}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{URI}}
- **AWS-Prod**:  http://{{PREFIX_PROD}}-{{APPLICATION_NAME}}.{{NETWORK_AWS_PROD}}/{{URI}}	

-------------------

## gs-lists API - <a href="https://git.euipo.europa.eu/projects/EGA/repos/gs-lists/browse" target="_blank">BitBucket</a>
{% set URI = 'ega/gs-lists/' %}
{% set APPLICATION_NAME = 'gs-lists' %}
- **AWS-Dev**:  http://{{PREFIX_DEV}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{URI}}
- **AWS-Test**:  http://{{PREFIX_TEST}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{URI}}
- **AWS-Prod**:  http://{{PREFIX_PROD}}-{{APPLICATION_NAME}}.{{NETWORK_AWS_PROD}}/{{URI}}

-------------------

## gs-loader API - <a href="https://git.euipo.europa.eu/projects/EGA/repos/gs-loader/browse" target="_blank">BitBucket</a>
{% set URI = 'ega/gs-loader/' %}
{% set APPLICATION_NAME = 'gs-loader' %}
- **AWS-Dev**:  http://{{PREFIX_DEV}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{URI}}
- **AWS-Test**:  http://{{PREFIX_TEST}}-{{APPLICATION_NAME}}.{{NETWORK_AWS}}/{{URI}}
- **AWS-Prod**:  http://{{PREFIX_PROD}}-{{APPLICATION_NAME}}.{{NETWORK_AWS_PROD}}/{{URI}}
