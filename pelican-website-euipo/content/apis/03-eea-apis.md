Title: EEA APIs
Slug: eea-apis
Summary: EEA APIs : EUTM Search API, Eutm Filing Api
order: 03

##  <a href="https://git.euipo.europa.eu/projects/EEA/repos/eutm-search-api/browse" target="_blank">BitBucket</a>

## _EUTM Search API_

- **AWS-Dev**:  http://{{ EEE_PREFIX_DEV }}-{{ EUTM_SEARCH_API_APPLICATION_NAME }}.{{ EEE_NETWORK_AWS }}/{{ EUTM_SEARCH_API_EOPW_URI }}
- **AWS-Test**:  http://{{ EEE_PREFIX_TEST }}-{{ EUTM_SEARCH_API_APPLICATION_NAME }}.{{ EEE_NETWORK_AWS }}/{{ EUTM_SEARCH_API_EOPW_URI }}
- **AWS-Prod**:  http://{{ EEE_PREFIX_PROD }}-{{ EUTM_SEARCH_API_APPLICATION_NAME }}.{{ EEE_NETWORK_AWS_PROD }}/{{ EUTM_SEARCH_API_EOPW_URI }}

---------------------

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

## _Eutm Filing Api_ - <a href="https://git.euipo.europa.eu/projects/EEA/repos/eutm-filing-api/browse" target="_blank">BitBucket</a>

- **AWS-Dev**:  http://{{ EEE_PREFIX_DEV }}-{{ EUTM_FILING_API_APPLICATION_NAME }}.{{ EEE_NETWORK_AWS }}/{{ EUTM_FILING_API_EOPW_URI }}
- **AWS-Test**:  http://{{ EEE_PREFIX_TEST }}-{{ EUTM_FILING_API_APPLICATION_NAME }}.{{ EEE_NETWORK_AWS }}/{{ EUTM_FILING_API_EOPW_URI }}
- **AWS-Prod**:  http://{{ EEE_PREFIX_PROD }}-{{ EUTM_FILING_API_APPLICATION_NAME }}.{{ EEE_NETWORK_AWS_PROD }}/{{ EUTM_FILING_API_EOPW_URI }}

