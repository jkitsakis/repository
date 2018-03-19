## JENKINS with SONARQUBE on POSTGRESQL database

This process describes how to run Jenkins CI service connected to a SonarQube service that persists its data in a Postgresql database. 

### Jenkins
The first step is to create a Jenkins image from the Dockerfile. To do so run : 
```docker build --build-arg JENKINS_VERSION=1.625.3 -t jenkins:1.625.3 .```

This will create an image `jenkins:1.625.3`.

### Sonar
The standard image from dockerhub is used for Sonar service; in the docker-compose is configured to use a PostgreSQL database.
 
### Postgres
The standard image from dockerhub is used for Postgres; a database SONAR is created for user sonar/sonar.


Review docker-compose.yml and start the infrastructure using 
``` docker-compose up -d```



## Upgrading infrastructure components

### Upgrading Jenkins
The following steps are required to upgrade Jenkins:

1. Build a new Jenkins image by passing the desired Jenkins version number e.g. ``` docker build --build-arg JENKINS_VERSION=<DESIGNATED_VERSION> -t jenkins:<DESIGNATED_VERSION>```
2. Update Jenkins service in the docker-compose.yml with the new version number
3. Stop running containers and recreate them using ```docker-compose up```
