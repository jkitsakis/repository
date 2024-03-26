Title: Find API URLs
Date: 2018-02-26
Slug: tutorial1
Category: Tutorials
Summary: API URLs for AWS
order:2

**How to Find API URLs for AWS (e.g. for test env)

- designs search

	1. goto **manifests**-website-apis**\helm\config\design-search-api\application-test.yaml** :  
	**prefix:** test- , **aws:** nonprod.aws.oami.eu

	2. goto manifests-website-apis**\helm\values.yaml** :  
	... design-search-api: **name:** 'design-search-api' and **path:** '/eop/design-search/'  

	**so** : http://test-design-search-api.nonprod.aws.oami.eu/eop/design-search/

- website-be

	1. goto **manifests-website-apis\helm\config\design-search-api\application-dev.yaml** :  
	**prefix:** dev- , **aws:** nonprod.aws.oami.eu

	2. goto **manifests-website-apis\helm\values.yaml** :  
	    ...
		website-backend:  
			name:'website-backend:'  
			networking.path: '/portal/app/api/'
        ...  
		
	 **so** : http://test-design-search-api.nonprod.aws.oami.eu/eop/design-search/

