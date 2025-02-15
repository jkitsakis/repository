Title: EMEA APIs
Slug: emea-apis
Summary: EMEA APIs : Me API
order: 05


## <a href="https://git.euipo.europa.eu/projects/EMEA/repos/me-api/browse" target="_blank">BitBucket</a> - <a href="https://argocd-dev.nonprod.aws.oami.eu/applications/me-api-dev-aws?resource=" target="_blank">ArgoCD</a>

## _Me API_ 

- **AWS-Dev**:  http://{{ EMEA_PREFIX_DEV }}-{{ ME_API_APPLICATION_NAME }}.{{ NETWORK_AWS }}/{{ ME_API_EOPW_URI }}
- **AWS-Test**:  http://{{ EMEA_PREFIX_TEST }}-{{ ME_API_APPLICATION_NAME }}.{{ NETWORK_AWS }}/{{ ME_API_EOPW_URI }}
- **AWS-Prod**:  http://{{ PREFIX_PROD }}-{{ ME_API_APPLICATION_NAME }}.{{ NETWORK_AWS_PROD }}/{{ ME_API_EOPW_URI }}

_Syntax_

> /trademarks?keyword=IF/mb&page=0&size=10&sort=applicationDate:desc

> /oppositions?size=10&page=0

> /cancellations?sort=cancellationDate:desc&roleKind=DEFENDANT

> /designs?size=200&page=0&query=designNumber!=0
