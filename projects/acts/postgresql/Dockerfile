FROM postgres:9.6
# ENV POSTGRESQL_HOME /var/lib/postgresql/
ENV INIT_DB /docker-entrypoint-initdb.d/

#chmod in order postgres data to be accessible from wildfly and tomcat
#RUN chmod -R 775 ${POSTGRESQL_HOME}
RUN chmod -R 775 ${INIT_DB}

# Enable remote connections
ADD setupRemoteConnections.sh ${INIT_DB}
RUN chmod +x ${INIT_DB}/setupRemoteConnections.sh

ADD setMaxPreparedTransactions.sh ${INIT_DB}
RUN chmod +x ${INIT_DB}/setMaxPreparedTransactions.sh

# Initialize ACTS DB
ADD acts/acts-init.sql ${INIT_DB}
