FROM postgres:9.6
#ENV POSTGRESQL_HOME /var/lib/postgresql/
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

# Initialize ECTN DB
#ADD ectn/000_init-db.sql ${INIT_DB}
#ADD ectn/001_tables.sql ${INIT_DB}
#ADD ectn/002_applicationParameters.sql ${INIT_DB}
#ADD ectn/003_countries.sql ${INIT_DB}
#ADD ectn/004_crewDuties.sql ${INIT_DB}
#ADD ectn/005_mng_mid.sql ${INIT_DB}
#ADD ectn/006_permissions.sql ${INIT_DB}
#ADD ectn/007_initUser.sql ${INIT_DB}
#ADD ectn/008_ships.sql ${INIT_DB}
#ADD ectn/009_mng_epc_message_contents.sql ${INIT_DB}
#ADD ectn/010_locations.sql ${INIT_DB}
#ADD ectn/011_finalDestinations.sql ${INIT_DB}
#ADD ectn/012_shipTypes.sql ${INIT_DB}

