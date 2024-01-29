Title: EOPW APIs
Date: 2018-02-26
Category: Rest APIs
Slug: eopw-apis
Summary: EOPW APIs : Website BE, Admin Tool, Story Block
order:6

## _Website BE_ 
### URL PATH: ... /portal/app/api/

### <a href="https://git.euipo.europa.eu/projects/EOPW/repos/eop-website-backend/browse" target="_blank">BitBucket</a>

- **Integration:** https://integration.euipo.europa.eu
- **PreProd:** https://pp.euipo.europa.eu

[//]: # (- **Test:** http://test-eutm-api.test.oami.eu)
- **Prod:** https://www.euipo.europa.eu


- **AWS-Dev:** https://dev-eop-website-backend.nonprod.aws.oami.eu
- **AWS-Test:** https://test-eop-website-backend.nonprod.aws.oami.eu
- **AWS-Prod:** https://production-eop-website-backend.nonprod.aws.oami.eu


> /templates?page=0&size=10&sort=creationDate:desc

> /templates/:templateIdentifier/notes 

> /drafts/designs

> /drafts/interpartes?keyword&size=5&page=0&sort=draftdate:DESC

> /drafts/interpartes?page=0&size=5&sort=draftdate%3Adesc

> /drafts/other?keyword&size=5&page=0&sort=draftdate:DESC

> /portfolio/trademarks?keyword=IF/mb&size=10&page=0&sort=applicationDate:desc

> /portfolio/trademarks?query=markBasis==EU_TRADEMARK and status=in=(ACCEPTANCE_PENDING,ACCEPTED)&page=0&sort=applicationDate:desc

> /portfolio/oppositions?size=10&roleKind=CLAIMANT&page=0&sort=oppositionDate:desc

> /portfolio/oppositions?roleKind=CLAIMANT&size=10&page=0&sort=oppositionDate:desc&query=status=in=(ADMISSIBILITY_CHECK)

> /portfolio/oppositions?size=50&page=0&roleKind=CLAIMANT

> /portfolio/trademarks?keyword=IF/mb&size=10&page=0&sort=applicationDate:desc

> /portfolio/trademarks/:applicationNumber

> /portfolio/oppositions/:oppositionId

> /portfolio/cancellations?size=20&page=0&roleKind=CLAIMANT

> /portfolio/designs?page=0&sort=applicationDate:desc&size=20&query=keyword==DM416DR

> /portfolio/designs?size=200&page=0&query=designNumber!=0

> /portfolio/designs?size=200&page=0&query=designNumber==000094560-0006

> /portfolio/designs/001754292-0001/comments

> /portfolio/appeals?page=0&size=25&roleKind=CLAIMANT&query=appealDate%3E%3D2022-05-01&sort=appealDate%3Adesc

> /userprofile/:documentId/export

> /surveys/:identifier

> /surveys/:identifier/answer


## _Admin Tool_
### URL PATH: ... /eop/admintool/app/api/

### <a href="https://git.euipo.europa.eu/projects/EOPW/repos/eop-admintool-backend/browse" target="_blank">BitBucket</a>

- **Integration:** https://integration.euipo.europa.eu
- **PreProd:** https://pp.euipo.europa.eu

[//]: # (- **Test:** http://test-eutm-api.test.oami.eu)
- **Prod:** https://www.euipo.europa.eu


- **AWS-Dev:** https://dev-eop-website-backend.nonprod.aws.oami.eu
- **AWS-Test:** https://test-eop-website-backend.nonprod.aws.oami.eu
- **AWS-Prod:** https://production-eop-website-backend.nonprod.aws.oami.eu

## _Story Blok_
### URL PATH: ... /eop/storyblok/

### <a href="https://git.euipo.europa.eu/projects/EOPW/repos/eop-storyblok-api/browse" target="_blank">BitBucket</a>
- 
- **Integration:** https://integration.euipo.europa.eu
- **PreProd:** https://pp.euipo.europa.eu

[//]: # (- **Test:** http://test-eutm-api.test.oami.eu)
- **Prod:** https://www.euipo.europa.eu


- **AWS-Dev:** https://dev-eop-website-backend.nonprod.aws.oami.eu
- **AWS-Test:** https://test-eop-website-backend.nonprod.aws.oami.eu
- **AWS-Prod:** https://production-eop-website-backend.nonprod.aws.oami.eu
