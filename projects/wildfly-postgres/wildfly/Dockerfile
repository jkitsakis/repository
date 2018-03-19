FROM jboss/base-jdk:8
ENV PROXY_URL http://172.22.250.177:80
ENV WILDFLY_VERSION 10.1.0.Final
ENV POSTGRESQL_JDBC_VERSION 42.0.0
ENV JBOSS_HOME /opt/jboss/wildfly
ENV ECTN_HOME_LOG /opt/jboss/logging/ectn



USER jboss

RUN \
  cd $HOME && \
  curl http://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz | tar zx && \
  ln -s $HOME/wildfly-$WILDFLY_VERSION $HOME/wildfly
  
# Download POSTGRESQL driver, add it as a wildfly module.
ENV WILDFLY_MODULE_DIR $JBOSS_HOME/modules/org/postgres/main
#RUN mkdir -p ${WILDFLY_MODULE_DIR} && cd ${WILDFLY_MODULE_DIR} && \ 
#curl --proxy $PROXY_URL -O https://jdbc.postgresql.org/download/postgresql-$POSTGRESQL_JDBC_VERSION.jar
ADD config/postgresql-$POSTGRESQL_JDBC_VERSION.jar ${WILDFLY_MODULE_DIR}/postgresql-$POSTGRESQL_JDBC_VERSION.jar
ADD config/jboss-postgresql-module.xml ${WILDFLY_MODULE_DIR}/module.xml

# Add a custom configuration.xml file; overwrite default
ADD config/wildfly-config.xml ${JBOSS_HOME}/standalone/configuration/standalone.xml

# Since files created with ADD have UID and GID of 0 and permission 600 we should modify this
USER root
RUN chown jboss:jboss ${WILDFLY_MODULE_DIR}/module.xml
RUN chown jboss:jboss ${WILDFLY_MODULE_DIR}/postgresql-$POSTGRESQL_JDBC_VERSION.jar
RUN chown jboss:jboss ${JBOSS_HOME}/standalone/configuration/standalone.xml
#RUN chown jboss:jboss ${JBOSS_HOME}/standalone/log/server.log

USER jboss
# Add a default admin user.
RUN ${JBOSS_HOME}/bin/add-user.sh --silent admin admin

#Expose deployment and log volumes
VOLUME ["$JBOSS_HOME/standalone/deployments", "$JBOSS_HOME/standalone/log"]

USER jboss

#Expose ports of interest
EXPOSE 8080
EXPOSE 8787
EXPOSE 9990

CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement", "0.0.0.0", "--debug", "8787"]

