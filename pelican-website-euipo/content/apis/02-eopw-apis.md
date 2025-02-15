Title: EOPW APIs
Slug: eopw-apis
Summary: EOPW APIs : Website BE, Admin Tool, Story Block
order: 02

## <a href="https://git.euipo.europa.eu/projects/EOPW/repos/eop-website-backend/browse" target="_blank">BitBucket</a> - <a href="https://argocd-dev.nonprod.aws.oami.eu/applications/argocd/website-dev-aws?view=tree&resource=" target="_blank">Argo CD Dev</a> - <a href="https://jenkins.prod.oami.eu/job/EOP/" target="_blank">Jenkins</a>

## _Website BE_ 

- **AWS-Dev**:  http://{{ EOPW_PREFIX_DEV }}-{{ WEBSITE_BE_APPLICATION_NAME }}.{{ EOPW_NETWORK_AWS }}/{{ WEBSITE_BE_EOPW_URI }}
- **AWS-Test**:  http://{{ EOPW_PREFIX_TEST }}-{{ WEBSITE_BE_APPLICATION_NAME }}.{{ EOPW_NETWORK_AWS }}/{{ WEBSITE_BE_EOPW_URI }}
- **AWS-Prod**:  http://{{ EOPW_PREFIX_PROD }}-{{ WEBSITE_BE_APPLICATION_NAME }}.{{ EOPW_NETWORK_AWS_PROD }}/{{ WEBSITE_BE_EOPW_URI }}

---------------------
<details>
<summary>Syntax</summary>
<ul>
<li>templates?page=0&size=10&sort=creationDate:desc</li>
<li>templates/:templateIdentifier/notes</li>
<li>drafts/designs</li>
<li>drafts/interpartes?keyword&size=5&page=0&sort=draftdate:DESC</li>
<li>drafts/interpartes?page=0&size=5&sort=draftdate%3Adesc</li>
<li>drafts/other?keyword&size=5&page=0&sort=draftdate:DESC</li>
<li>portfolio/trademarks?keyword=IF/mb&size=10&page=0&sort=applicationDate:desc</li>
<li>portfolio/trademarks?query=markBasis==EU_TRADEMARK and status=in=(ACCEPTANCE_PENDING,ACCEPTED)&page=0&sort=applicationDate:desc
</li>
<li>portfolio/oppositions?size=10&roleKind=CLAIMANT&page=0&sort=oppositionDate:desc</li>
<li>portfolio/oppositions?roleKind=CLAIMANT&size=10&page=0&sort=oppositionDate:desc&query=status=in=(ADMISSIBILITY_CHECK)
</li>
<li>portfolio/oppositions?size=50&page=0&roleKind=CLAIMANT</li>
<li>portfolio/trademarks?keyword=IF/mb&size=10&page=0&sort=applicationDate:desc</li>
<li>portfolio/trademarks/:applicationNumber</li>
<li>portfolio/oppositions/:oppositionId</li>
<li>portfolio/cancellations?size=20&page=0&roleKind=CLAIMANT</li>
<li>portfolio/designs?page=0&sort=applicationDate:desc&size=20&query=keyword==DM416DR</li>
<li>portfolio/designs?size=200&page=0&query=designNumber!=0</li>
<li>portfolio/designs?size=200&page=0&query=designNumber==000094560-0006</li>
<li>portfolio/designs/001754292-0001/comments</li>
<li>portfolio/appeals?page=0&size=25&roleKind=CLAIMANT&query=appealDate%3E%3D2022-05-01&sort=appealDate%3Adesc
</li>
<li>userprofile/:documentId/export</li>
<li>surveys/:identifier</li>
<li>surveys/:identifier/answer</li>
</ul>

</details>

--------------------- 

## _Admin Tool_ - <a href="https://git.euipo.europa.eu/projects/EOPW/repos/eop-admintool-backend/browse" target="_blank">BitBucket</a>

- **AWS-Dev**:  http://{{ EOPW_PREFIX_DEV }}-{{ ADMIN_TOOL_APPLICATION_NAME }}.{{ EOPW_NETWORK_AWS }}/{{ ADMIN_TOOL_EOPW_URI }}
- **AWS-Test**:  http://{{ EOPW_PREFIX_TEST }}-{{ ADMIN_TOOL_APPLICATION_NAME }}.{{ EOPW_NETWORK_AWS }}/{{ ADMIN_TOOL_EOPW_URI }}
- **AWS-Prod**:  http://{{ EOPW_PREFIX_PROD }}-{{ ADMIN_TOOL_APPLICATION_NAME }}.{{ EOPW_NETWORK_AWS_PROD }}/{{ ADMIN_TOOL_EOPW_URI }}

---------------------

## _Story Blok_ - <a href="https://git.euipo.europa.eu/projects/EOPW/repos/eop-storyblok-api/browse" target="_blank">BitBucket</a>

- **AWS-Dev**:  http://{{ EOPW_PREFIX_DEV }}-{{ STORY_BLOK_APPLICATION_NAME }}.{{ EOPW_NETWORK_AWS }}/{{ STORY_BLOK_EOPW_URI }}
- **AWS-Test**:  http://{{ EOPW_PREFIX_TEST }}-{{ STORY_BLOK_APPLICATION_NAME }}.{{ EOPW_NETWORK_AWS }}/{{ STORY_BLOK_EOPW_URI }}
- **AWS-Prod**:  http://{{ EOPW_PREFIX_PROD }}-{{ STORY_BLOK_APPLICATION_NAME }}.{{ EOPW_NETWORK_AWS_PROD }}/{{ STORY_BLOK_EOPW_URI }}


