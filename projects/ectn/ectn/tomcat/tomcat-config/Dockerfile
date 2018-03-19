FROM openjdk:8-jre

# Tomcat Version
ENV TOMCAT_VERSION_MAJOR 8
ENV TOMCAT_VERSION_FULL  8.5.12
ENV CATALINA_HOME /opt/tomcat
ENV JAVA_OPTS  -server -Xdebug -Xnoagent -Djava.compiler=NONE -Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=8000 -Xms512m -Xmx1024m -XX:+CMSClassUnloadingEnabled -Dfile.encoding=UTF8 -Duser.timezone=GMT -Dorg.jboss.logging.provider=log4j -Dorg.apache.el.parser.SKIP_IDENTIFIER_CHECK=true -Dorg.apache.catalina.loader.WebappClassLoader.ENABLE_CLEAR_REFERENCES=false
ENV CATALINA_OPTS -Dbtm.root=$CATALINA_HOME -Dbitronix.tm.configuration=$CATALINA_HOME/conf/btm-config.properties


# Download and install
RUN cd $HOME &&\
  curl -LO https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_VERSION_MAJOR}/v${TOMCAT_VERSION_FULL}/bin/apache-tomcat-${TOMCAT_VERSION_FULL}.tar.gz &&\
  curl -LO https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_VERSION_MAJOR}/v${TOMCAT_VERSION_FULL}/bin/apache-tomcat-${TOMCAT_VERSION_FULL}.tar.gz.md5 &&\
  gunzip -c $HOME/apache-tomcat-${TOMCAT_VERSION_FULL}.tar.gz | tar -xf - -C /opt &&\  
  ln -s /opt/apache-tomcat-${TOMCAT_VERSION_FULL} /opt/tomcat &&\
  rm -rf /opt/tomcat/webapps/examples &&\
  rm -rf /opt/tomcat/webapps/docs  &&\
  rm -f $HOME/apache-tomcat-${TOMCAT_VERSION_FULL}.tar.gz  &&\
  rm -f $HOME/apache-tomcat-${TOMCAT_VERSION_FULL}.tar.gz.md5 
  

# Configuration
ADD config/lib/*.jar ${CATALINA_HOME}/lib/
ADD config/context.xml ${CATALINA_HOME}/conf/context.xml
ADD config/resources.properties ${CATALINA_HOME}/conf/resources.properties
ADD config/server.xml ${CATALINA_HOME}/conf/server.xml
ADD config/settings.xml ${CATALINA_HOME}/conf/settings.xml
ADD config/tomcat-users.xml ${CATALINA_HOME}/conf/tomcat-users.xml
ADD config/btm-config.properties ${CATALINA_HOME}/conf/btm-config.properties
ADD config/web.xml ${CATALINA_HOME}/conf/web.xml

#ADD config/setenv.sh ${CATALINA_HOME}/bin/setenv.sh

ADD config/manager/context.xml ${CATALINA_HOME}/webapps/manager/META-INF/context.xml
ADD config/host-manager/context.xml ${CATALINA_HOME}/webapps/host-manager/META-INF/context.xml


# Launch Tomcat on startup
CMD ${CATALINA_HOME}/bin/catalina.sh  run
#CMD ["catalina.sh", "jpda", "run"]