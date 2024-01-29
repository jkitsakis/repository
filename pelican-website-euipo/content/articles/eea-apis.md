Title: EEA APIs
Date: 2018-02-26
Category: Rest APIs
Slug: eea-apis
Summary: EEA APIs : EUTM Search API, Eutm Filing Api
order:3

## _EUTM Search API_ 

### URL PATH: ... /eop/eutm-search/trademarks?

### <a href="https://git.euipo.europa.eu/projects/EEA/repos/eutm-search-api/browse" target="_blank">BitBucket</a>

- **Integration:** http://int-api.dev.oami.eu
- **PreProd:** http://pp-api.test.oami.eu
- **Test:** http://test-eutm-api.test.oami.eu
- **Prod:** http://api.prod.oami.eu


- **AWS-Dev:** http://dev-eutm-search-api.nonprod.aws.oami.eu
- **AWS-Test:** http://test-eutm-search-api.nonprod.aws.oami.eu
- **AWS-Prod:** http://production-eutm-search-api.prod.aws.oami.eu

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


## _Eutm Filing Api_
### URL PATH: ... /eop/eutm-filing/

- **Integration:** http://int-api.dev.oami.eu
- **PreProd:** http://pp-api.test.oami.eu
- **Test:** http://test-eutm-api.test.oami.eu
- **Prod:** http://api.prod.oami.eu


- **AWS-Dev:** http://dev-eutm-filing-api.nonprod.aws.oami.eu
- **AWS-Test:** http://test-eutm-filing-api.nonprod.aws.oami.eu
- **AWS-Prod:** http://production-eutm-filing-api.prod.aws.oami.eu