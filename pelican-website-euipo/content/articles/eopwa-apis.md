Title: EOPWA APIs
Date: 2018-02-26
Category: Rest APIs
Slug: eopwa-apis
Summary: EOPWA APIs : Appeals Search API, Communications Search API, Designs Search API, Drafts Search API, Feedback Search API, Interpartes Search API
order: 8
Tag: EOPWA APIs : Appeals Search API, Communications Search API, Designs Search API, Drafts Search API, Feedback Search API, Interpartes Search API


### Appeals Search API
 
### URL PATH: ... /eop/appeals-search

### <a href="https://git.euipo.europa.eu/projects/EOPWA/repos/appeals-search-api/browse" target="_blank">BitBucket</a>

- **Integration:** http://int-api.dev.oami.eu
- **PreProd:** http://pp-api.test.oami.eu 
- **Test:** http://test-api.test.oami.eu 

- **AWS-Dev:** http://dev-appeals-search-api.nonprod.aws.oami.eu 
- **AWS-Test:** http://test-appeals-search-api.nonprod.aws.oami.eu 
- **AWS-Prod:** http://production-appeals-search-api.prod.aws.oami.eu 

> ... ?query=appealNumber=='R00*'&roleKind=CLAIMANT&page=0&size=25&sort=appealDate:desc


### Communications Search API

### URL PATH: ... /eop/communications/

### <a href="https://git.euipo.europa.eu/projects/EOPWA/repos/communications-api/browse" target="_blank">BitBucket</a>

- **Integration:** http://int-api.dev.oami.eu
- **PreProd:** http://pp-api.test.oami.eu 
- **Test:** http://test-api.test.oami.eu 

- **AWS-Dev:** http://dev-communications-api.nonprod.aws.oami.eu 
- **AWS-Test:** http://test-communications-api.nonprod.aws.oami.eu
- **AWS-Prod:** http://production-communications-api.prod.aws.oami.eu 


### Designs Search API

### URL PATH: ... /eop/design-search

### <a href="https://git.euipo.europa.eu/projects/EOPWA/repos/design-search-api/browse" target="_blank">BitBucket</a>

- **Integration:** http://int-api.dev.oami.eu
- **PreProd:** http://pp-api.test.oami.eu 
- **Test:** http://test-api.test.oami.eu 

- **AWS-Dev:** http://dev-design-search-api.nonprod.aws.oami.eu 
- **AWS-Test:** http://test-design-search-api.nonprod.aws.oami.eu
- **AWS-Prod:** http://production-design-search-api.prod.aws.oami.eu 

> ... ?query=designNumber!=9*&size=10&page=0&sort=applicationDate:desc


### Drafts Search API

### URL PATH: ... /eop/drafts/**eutms**?size=10&page=10&sort=creationDate:DESC

### URL PATH: ... /eop/drafts/**designs**?size=10&page=10&sort=creationDate:DESC

### URL PATH: ... /eop/drafts/**interpartes**?size=10&page=10&sort=creationDate:DESC

### URL PATH: ... /eop/drafts/**other**?size=10&page=10&sort=creationDate:DESC

### <a href="https://git.euipo.europa.eu/projects/EOPWA/repos/drafts-api/browse" target="_blank">BitBucket</a>

- **Integration:** http://int-api.dev.oami.eu
- **PreProd:** http://pp-api.test.oami.eu 
- **Test:** http://test-api.test.oami.eu 

- **AWS-Dev:** http://dev-drafts-api.nonprod.aws.oami.eu 
- **AWS-Test:** http://test-drafts-api.nonprod.aws.oami.eu
- **AWS-Prod:** http://production-drafts-api.prod.aws.oami.eu   

### Feedback Search API

### URL PATH: ... /eop/feedback/surveys/:indentifier

### <a href="https://git.euipo.europa.eu/projects/EOPWA/repos/feedback-api/browse" target="_blank">BitBucket</a>

- **Integration:** http://int-api.dev.oami.eu
- **PreProd:** http://pp-api.test.oami.eu 
- **Test:** http://test-api.test.oami.eu 

- **AWS-Dev:** http://dev-feedback-api.nonprod.aws.oami.eu 
- **AWS-Test:** http://test-feedback-api.nonprod.aws.oami.eu 
- **AWS-Prod:** http://production-feedback-api.prod.aws.oami.eu   


### Interpartes Search API

### URL PATH: ... /eop/interpartes-search/oppositions?query=opponentRepresentatives.identifier==10014&size=100&page=0&sort=oppositionDate:desc

### URL PATH: ... /eop/interpartes-search/cancellations?page=0&sort=cancellationNumber:desc&size=160
### URL PATH: ... /eop/interpartes-search/invalidities?query=claimantRepresentatives.name=="HO+*"&size=100&page=0&sort=invalidityDate:desc

### <a href="https://git.euipo.europa.eu/projects/EOPWA/repos/interpartes-search-api/browse" target="_blank">BitBucket</a>

- **Integration:** http://int-api.dev.oami.eu
- **PreProd:** http://pp-api.test.oami.eu 
- **Test:** http://test-api.test.oami.eu 

- **AWS-Dev:** http://dev-interpartes-search-api.nonprod.aws.oami.eu  
- **AWS-Test:** http://test-interpartes-search-api.nonprod.aws.oami.eu 
- **AWS-Prod:** http://production-interpartes-search-api.prod.aws.oami.eu


### Notes Search API

### URL PATH: ... /eop/notes/

### <a href="https://git.euipo.europa.eu/projects/EOPWA/repos/notes-api/browse" target="_blank">BitBucket</a>

- **Integration:** http://int-api.dev.oami.eu
- **PreProd:** http://pp-api.test.oami.eu 
- **Test:** http://test-api.test.oami.eu 

- **AWS-Dev:** http://dev-notes-api.nonprod.aws.oami.eu   
- **AWS-Test:** http://test-notes-api.nonprod.aws.oami.eu 
- **AWS-Prod:** http://production-notes-api.prod.aws.oami.eu 


### Pre-Assesement Search API
### URL PATH: ... /eop/pre-assessment/

### <a href="https://git.euipo.europa.eu/projects/EOPWA/repos/pre-assessment-api/browse" target="_blank">BitBucket</a>

- **Integration:** http://int-api.dev.oami.eu
- **PreProd:** http://pp-api.test.oami.eu 
- **Test:** http://test-api.test.oami.eu 

- **AWS-Dev:** http://dev-pre-assessment-api.nonprod.aws.oami.eu  
- **AWS-Test:** http://test-pre-assessment-api.nonprod.aws.oami.eu 
- **AWS-Prod:** http://production-pre-assessment-api.prod.aws.oami.eu 

### Settings Search API

### URL PATH: ... /eop/settings/

### <a href="https://git.euipo.europa.eu/projects/EOPWA/repos/settings-api/browse" target="_blank">BitBucket</a>

- **Integration:** http://int-api.dev.oami.eu
- **PreProd:** http://pp-api.test.oami.eu 
- **Test:** http://test-api.test.oami.eu 

- **AWS-Dev:** http://dev-settings-api.nonprod.aws.oami.eu 
- **AWS-Test:** http://test-settings-api.nonprod.aws.oami.eu 
- **AWS-Prod:** http://production-settings-api.prod.aws.oami.eu 

### User Profile API

### URL PATH: ...  /eop/user-profile/

### <a href="https://git.euipo.europa.eu/projects/EOPWA/repos/user-profile-api/browse" target="_blank">BitBucket</a>

- **Integration:** http://int-api.dev.oami.eu
- **PreProd:** http://pp-api.test.oami.eu 
- **Test:** http://test-api.test.oami.eu 

- **AWS-Dev:** http://dev-user-profile-api.nonprod.aws.oami.eu 
- **AWS-Test:** http://test-user-profile-api.nonprod.aws.oami.eu 
- **AWS-Prod:** http://production-user-profile-api.prod.aws.oami.eu 