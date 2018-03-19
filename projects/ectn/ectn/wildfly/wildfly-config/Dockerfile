FROM jboss/wildfly:10.1.0.Final

ENV POSTGRESQL_JDBC_VERSION 42.0.0
ENV WILDFLY_HOME /opt/jboss/wildfly
ENV WILDFLY_MODULE_DIR ${WILDFLY_HOME}/modules/org/postgres/main
ENV RUN_USER jboss
ENV RUN_GROUP jboss

RUN ${WILDFLY_HOME}/bin/add-user.sh admin admin --silent

ADD config/postgresql-${POSTGRESQL_JDBC_VERSION}.jar ${WILDFLY_MODULE_DIR}/postgresql-${POSTGRESQL_JDBC_VERSION}.jar
ADD config/jboss-postgresql-module.xml ${WILDFLY_MODULE_DIR}/module.xml
ADD config/wildfly-config.xml ${WILDFLY_HOME}/standalone/configuration/standalone.xml
ADD config/server.log ${WILDFLY_HOME}/standalone/log/server.log

CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement", "0.0.0.0", "--debug", "8787"]

