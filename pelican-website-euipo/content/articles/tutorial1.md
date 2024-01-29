Title: Find API URLs
Date: 2018-02-26
Slug: tutorial1
Category: Tutorials
Summary: API URLs for AWS
order:2

**How to Find API URLs for AWS e.g designs search**

1. goto manifests-website-apis\helm\config\design-search-api\application-test.yaml : prefix: test- , aws: nonprod.aws.oami.eu
 
2. goto manifests-website-apis\helm\config\design-search-api\application.yaml : spring.application.name: design-search-api

3. goto manifests-website-apis\helm\values.yaml : design-search-api: path: '/eop/design-search/'

4. so : http://test-design-search-api.nonprod.aws.oami.eu/eop/design-search/



**Authentication links**

- Integration : 

Auth.openidconnect.issuerUri: https://auth.test.euipo.europa.eu/t/euipo.europa.eu/oauth2/token

- Other

openidconnect.issuerUri: https://pp.euipo.europa.eu/cas-server-webapp/oidc