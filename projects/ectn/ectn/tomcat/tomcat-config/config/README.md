Tomcat 8.5 configuration for ECTN
=================================
 
Contents
========
In folder
$CATALINA_HOME/conf/
 - btm-config.properties
 - context.xml
 - resources.properties
 - server.xml
  
$CATALINA_HOME/bin/
 - setenv.sh
 
$CATALINA_HOME/lib/
 - logging (slf4j - log4j)
 - jee (jms, jta(bitronix), jstl, mail)
 - jdbc (postgres)
 - ectn shared lib (commons io/fileupload ...)
 
  
security (server.xml)
=====================

 - SSO	
 <Valve className="org.apache.catalina.authenticator.SingleSignOn" />
 
 - authenticator 
   	<Realm className="org.apache.catalina.realm.DataSourceRealm"
             dataSourceName="usersDS"
             userTable="mng_users" userNameCol="user_id" userCredCol="password"
             userRoleTable="user_roles_vw" roleNameCol="profile_name"/>

              
JDBC
====

 
JMS
=== 
   http://activemq.apache.org/download.html 
   activemq start/stop/restart ...
       
JTA
===

Applications
============
 - agent-app.war
 - ectn-agent.war
 - ectn-login.war
 - ectn-mng.war
 - ectn-sub.war
 - mng-app.war
 - sub-app.war

