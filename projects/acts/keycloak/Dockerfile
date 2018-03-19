FROM openjdk:8-jre

ENV KEYCLOAK_VERSION 1.2.0.Final
ENV POSTGRESQL_JDBC_VERSION 9.4-1201.jdbc41
ENV KC_HOME /opt/jboss
ENV WILDFLY_MODULE_DIR $KC_HOME/keycloak/modules/org/postgresql/main



RUN \
  groupadd -r jboss -g 1001 && \
  useradd -u 1001 -r -g jboss -m -d $KC_HOME -s /bin/bash -c "JBoss user" jboss 

# Switch to user jboss
#USER jboss
# copy keycloak server to /opt/jboss
#ADD config/keycloak-server-dist-$KEYCLOAK_VERSION.tar.gz $KC_HOME
RUN cd $HOME &&\
	curl -O http://central.maven.org/maven2/org/keycloak/keycloak-server-dist/$KEYCLOAK_VERSION/keycloak-server-dist-$KEYCLOAK_VERSION.tar.gz &&\ 
	tar zxvf keycloak-server-dist-$KEYCLOAK_VERSION.tar.gz &&\ 
	mv $HOME/keycloak-$KEYCLOAK_VERSION $KC_HOME/keycloak 
    
RUN ln -s $KC_HOME/keycloak-$KEYCLOAK_VERSION $KC_HOME/keycloak


ADD config/postgresql-$POSTGRESQL_JDBC_VERSION.jar ${WILDFLY_MODULE_DIR}/postgresql-$POSTGRESQL_JDBC_VERSION.jar
ADD config/jboss-postgresql-module.xml ${WILDFLY_MODULE_DIR}/module.xml
ADD config/acts-realm.json $KC_HOME/keycloak/acts-realm.json
ADD config/wildfly-config.xml $KC_HOME/keycloak/standalone/configuration/standalone.xml

#static pages
RUN mkdir -p $KC_HOME/static
COPY config/ui-config $KC_HOME/static/

# permissions on opt/jboss
RUN chown -R jboss:jboss $KC_HOME/

#Wildfly User 
RUN $KC_HOME/keycloak/bin/add-user.sh --silent admin admin 

#Expose deployment and log volumes
#VOLUME ["/opt/jboss/keycloak/standalone/deployments", "/opt/jboss/keycloak/standalone/log", "/opt/jboss/static"]

CMD ["/opt/jboss/keycloak/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement", "0.0.0.0", "--debug", "8787", "-Dkeycloak.migration.action=import", "-Dkeycloak.migration.provider=singleFile", "-Dkeycloak.migration.file=$KC_HOME/keycloak/acts-realm.json", "-Dkeycloak.migration.strategy=OVERWRITE_EXISTING"]

