# WildFly Administration Console require a user in administration realm. 

FROM jboss/wildfly:latest

# Run command to create a  new user with credentials admin/password 
RUN /opt/jboss/wildfly/bin/add-user.sh admin admin --silent

CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement", "0.0.0.0"]
