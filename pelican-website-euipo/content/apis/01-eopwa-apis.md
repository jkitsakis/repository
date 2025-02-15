Title: EOPWA APIs
Slug: eopwa-apis
Summary: EOPWA APIs : Appeals Search API, Communications API, Designs Search API, Drafts Search API, Feedback Search API, Interpartes Search API, User Profile Api
order: 01

## <a href="https://git.euipo.europa.eu/projects/EOPWA/repos/appeals-search-api/browse" target="_blank">BitBucket</a>-<a href="https://argocd-dev.nonprod.aws.oami.eu/applications/argocd/website-api-dev-aws?view=tree&resource=" target="_blank">ArgoCD</a>

## _Appeals Search API_ 

- **AWS-Dev**:  http://{{ EOPWA_PREFIX_DEV }}-{{ APPEALS_SEARCH_APPLICATION_NAME }}.{{ EOPWA_NETWORK_AWS }}/{{ APPEALS_SEARCH_EOPW_URI }}
- **AWS-Test**:  http://{{ EOPWA_PREFIX_TEST }}-{{ APPEALS_SEARCH_APPLICATION_NAME }}.{{ EOPWA_NETWORK_AWS }}/{{ APPEALS_SEARCH_EOPW_URI }}
- **AWS-Prod**:  http://{{ EOPWA_PREFIX_PROD }}-{{ APPEALS_SEARCH_APPLICATION_NAME }}.{{ EOPWA_NETWORK_AWS_PROD }}/{{ APPEALS_SEARCH_EOPW_URI }}

_Syntax_ 
> ... ?query=appealNumber=='R00*'&roleKind=CLAIMANT&page=0&size=25&sort=appealDate:desc

-------------------

## Communications Search API-<a href="https://git.euipo.europa.eu/projects/EOPWA/repos/communications-api/browse" target="_blank">BitBucket</a>

- **AWS-Dev**:  http://{{ EOPWA_PREFIX_DEV }}-{{ COMMUNICATIONS_SEARCH_APPLICATION_NAME }}.{{ EOPWA_NETWORK_AWS }}/{{ COMMUNICATIONS_SEARCH_EOPW_URI }}
- **AWS-Test**:  http://{{ EOPWA_PREFIX_TEST }}-{{ COMMUNICATIONS_SEARCH_APPLICATION_NAME }}.{{ EOPWA_NETWORK_AWS }}/{{ COMMUNICATIONS_SEARCH_EOPW_URI }}
- **AWS-Prod**:  http://{{ EOPWA_PREFIX_PROD }}-{{ COMMUNICATIONS_SEARCH_APPLICATION_NAME }}.{{ EOPWA_NETWORK_AWS_PROD }}/{{ COMMUNICATIONS_SEARCH_EOPW_URI }}


-------------------

## Designs Search API-<a href="https://git.euipo.europa.eu/projects/EOPWA/repos/design-search-api/browse" target="_blank">BitBucket</a>

- **AWS-Dev**:  http://{{ EOPWA_PREFIX_DEV }}-{{ DESIGNS_SEARCH_APPLICATION_NAME }}.{{ EOPWA_NETWORK_AWS }}/{{ DESIGNS_SEARCH_EOPW_URI }}
- **AWS-Test**:  http://{{ EOPWA_PREFIX_TEST }}-{{ DESIGNS_SEARCH_APPLICATION_NAME }}.{{ EOPWA_NETWORK_AWS }}/{{ DESIGNS_SEARCH_EOPW_URI }}
- **AWS-Prod**:  http://{{ EOPWA_PREFIX_PROD }}-{{ DESIGNS_SEARCH_APPLICATION_NAME }}.{{ EOPWA_NETWORK_AWS_PROD }}/{{ DESIGNS_SEARCH_EOPW_URI }}

_Syntax_ 
> ... ?query=designNumber!=9*&size=10&page=0&sort=applicationDate:desc

-------------------

## Drafts Search API-<a href="https://git.euipo.europa.eu/projects/EOPWA/repos/drafts-api/browse" target="_blank">BitBucket</a>

- **AWS-Dev**:  http://{{ EOPWA_PREFIX_DEV }}-{{ DRAFTS_SEARCH_APPLICATION_NAME }}.{{ EOPWA_NETWORK_AWS }}/{{ DRAFTS_SEARCH_EOPW_URI }}
- **AWS-Test**:  http://{{ EOPWA_PREFIX_TEST }}-{{ DRAFTS_SEARCH_APPLICATION_NAME }}.{{ EOPWA_NETWORK_AWS }}/{{ DRAFTS_SEARCH_EOPW_URI }}
- **AWS-Prod**:  http://{{ EOPWA_PREFIX_PROD }}-{{ DRAFTS_SEARCH_APPLICATION_NAME }}.{{ EOPWA_NETWORK_AWS_PROD }}/{{ DRAFTS_SEARCH_EOPW_URI }}


### eutms: /drafts/eutms?size=10&page=0&sort=creationDate:DESC

### designs: /drafts/designs?size=10&page=0&sort=creationDate:DESC

### interpartes: /drafts/interpartes?page=0&size=10&actions=OPPOSITION&sort=draftdate:desc

### other: /drafts/other?size=10&page=0&sort=creationDate:DESC

-------------------

## Feedback Search API-<a href="https://git.euipo.europa.eu/projects/EOPWA/repos/feedback-api/browse" target="_blank">BitBucket</a>

- **AWS-Dev**:  http://{{ EOPWA_PREFIX_DEV }}-{{ FEEDBACK_SEARCH_APPLICATION_NAME }}.{{ EOPWA_NETWORK_AWS }}/{{ FEEDBACK_SEARCH_EOPW_URI }}
- **AWS-Test**:  http://{{ EOPWA_PREFIX_TEST }}-{{ FEEDBACK_SEARCH_APPLICATION_NAME }}.{{ EOPWA_NETWORK_AWS }}/{{ FEEDBACK_SEARCH_EOPW_URI }}
- **AWS-Prod**:  http://{{ EOPWA_PREFIX_PROD }}-{{ FEEDBACK_SEARCH_APPLICATION_NAME }}.{{ EOPWA_NETWORK_AWS_PROD }}/{{ FEEDBACK_SEARCH_EOPW_URI }}

-------------------

## Interpartes Search API-<a href="https://git.euipo.europa.eu/projects/EOPWA/repos/interpartes-search-api/browse" target="_blank">BitBucket</a>

- **AWS-Dev**:  http://{{ EOPWA_PREFIX_DEV }}-{{ INTERPARTES_SEARCH_APPLICATION_NAME }}.{{ EOPWA_NETWORK_AWS }}/{{ INTERPARTES_SEARCH_EOPW_URI }}
- **AWS-Test**:  http://{{ EOPWA_PREFIX_TEST }}-{{ INTERPARTES_SEARCH_APPLICATION_NAME }}.{{ EOPWA_NETWORK_AWS }}/{{ INTERPARTES_SEARCH_EOPW_URI }}
- **AWS-Prod**:  http://{{ EOPWA_PREFIX_PROD }}-{{ INTERPARTES_SEARCH_APPLICATION_NAME }}.{{ EOPWA_NETWORK_AWS_PROD }}/{{ INTERPARTES_SEARCH_EOPW_URI }}

### oppositions: /oppositions?query=opponentRepresentatives.identifier==10014&size=100&page=0&sort=oppositionDate:desc

### cancellations: /cancellations?page=0&sort=cancellationNumber:desc&size=160

### invalidities: /invalidities?query=claimantRepresentatives.name=="HO+*"&size=100&page=0&sort=invalidityDate:desc

-------------------

## Notes Search API-<a href="https://git.euipo.europa.eu/projects/EOPWA/repos/notes-api/browse" target="_blank">BitBucket</a>

- **AWS-Dev**:  http://{{ EOPWA_PREFIX_DEV }}-{{ NOTES_SEARCH_APPLICATION_NAME }}.{{ EOPWA_NETWORK_AWS }}/{{ NOTES_SEARCH_EOPW_URI }}
- **AWS-Test**:  http://{{ EOPWA_PREFIX_TEST }}-{{ NOTES_SEARCH_APPLICATION_NAME }}.{{ EOPWA_NETWORK_AWS }}/{{ NOTES_SEARCH_EOPW_URI }}
- **AWS-Prod**:  http://{{ EOPWA_PREFIX_PROD }}-{{ NOTES_SEARCH_APPLICATION_NAME }}.{{ EOPWA_NETWORK_AWS_PROD }}/{{ NOTES_SEARCH_EOPW_URI }}

---------------------

## Pre-Assesement Search API-<a href="https://git.euipo.europa.eu/projects/EOPWA/repos/pre-assessment-api/browse" target="_blank">BitBucket</a>

- **AWS-Dev**:  http://{{ EOPWA_PREFIX_DEV }}-{{ PRE_ASSESEMENT_SEARCH_APPLICATION_NAME }}.{{ EOPWA_NETWORK_AWS }}/{{ PRE_ASSESEMENT_SEARCH_EOPW_URI }}
- **AWS-Test**:  http://{{ EOPWA_PREFIX_TEST }}-{{ PRE_ASSESEMENT_SEARCH_APPLICATION_NAME }}.{{ EOPWA_NETWORK_AWS }}/{{ PRE_ASSESEMENT_SEARCH_EOPW_URI }}
- **AWS-Prod**:  http://{{ EOPWA_PREFIX_PROD }}-{{ PRE_ASSESEMENT_SEARCH_APPLICATION_NAME }}.{{ EOPWA_NETWORK_AWS_PROD }}/{{ PRE_ASSESEMENT_SEARCH_EOPW_URI }}

-------------------------

## Settings Search API-<a href="https://git.euipo.europa.eu/projects/EOPWA/repos/settings-api/browse" target="_blank">BitBucket</a>

{% set SETTINGS_SEARCH_EOPW_URI = 'eop/settings/' %}
{% set SETTINGS_SEARCH_APPLICATION_NAME = 'settings-api' %}
- **AWS-Dev**:  http://{{ EOPWA_PREFIX_DEV }}-{{ SETTINGS_SEARCH_APPLICATION_NAME }}.{{ EOPWA_NETWORK_AWS }}/{{ SETTINGS_SEARCH_EOPW_URI }}
- **AWS-Test**:  http://{{ EOPWA_PREFIX_TEST }}-{{ SETTINGS_SEARCH_APPLICATION_NAME }}.{{ EOPWA_NETWORK_AWS }}/{{ SETTINGS_SEARCH_EOPW_URI }}
- **AWS-Prod**:  http://{{ EOPWA_PREFIX_PROD }}-{{ SETTINGS_SEARCH_APPLICATION_NAME }}.{{ EOPWA_NETWORK_AWS_PROD }}/{{ SETTINGS_SEARCH_EOPW_URI }}

-----------------------------

## User Profile API-<a href="https://git.euipo.europa.eu/projects/EOPWA/repos/user-profile-api/browse" target="_blank">BitBucket</a>

- **AWS-Dev**:  http://{{ EOPWA_PREFIX_DEV }}-{{ USER_PROFILE_APPLICATION_NAME }}.{{ EOPWA_NETWORK_AWS }}/{{ USER_PROFILE_EOPW_URI }}
- **AWS-Test**:  http://{{ EOPWA_PREFIX_TEST }}-{{ USER_PROFILE_APPLICATION_NAME }}.{{ EOPWA_NETWORK_AWS }}/{{ USER_PROFILE_EOPW_URI }}
- **AWS-Prod**:  http://{{ EOPWA_PREFIX_PROD }}-{{ USER_PROFILE_APPLICATION_NAME }}.{{ EOPWA_NETWORK_AWS_PROD }}/{{ USER_PROFILE_EOPW_URI }}

