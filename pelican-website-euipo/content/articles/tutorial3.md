Title: Authentication links for Postman
Slug: tutoria3
Date: 2018-02-26
Category: Tutorials
Summary: Deploy on ArgoCD
order:4

**Deploy on ArgoCD **

e.g. Website-be

1. Visit <a href="https://jenkins.prod.oami.eu/job/EOP/" target="_blank">Jenkins</a>  

2. Click Website > eop-website-backend > Build > master  

3. Click latest jenkins build on left  

4. Copy webapplication:1.4.0-RC6.3-SNAPSHOT-673a3707c46843a96d4c88645e4a791dda3a2c39 without "webapplication:"  

5. Open Manifest Branch in dev-aws and goto manifests/helm/values-dev.yaml  

6. Edit tag in website-backend: group



