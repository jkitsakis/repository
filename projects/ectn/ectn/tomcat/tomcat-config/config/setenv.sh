#!/bin/sh
JAVA_OPTS="$JAVA_OPTS\ 
-server\
-Xms512m -Xmx1024m\
-XX:+CMSClassUnloadingEnabled\
-Dfile.encoding=UTF8\
-Duser.timezone=GMT\
-Dorg.jboss.logging.provider=log4j\
-Dorg.apache.el.parser.SKIP_IDENTIFIER_CHECK=true\
-Dorg.apache.catalina.loader.WebappClassLoader.ENABLE_CLEAR_REFERENCES=false" 
#  
# -Dcom.sun.jersey.server.impl.cdi.lookupExtensionInBeanManager=true 
#
CATALINA_OPTS="-Dbtm.root=$CATALINA_HOME\
-Dbitronix.tm.configuration=$CATALINA_HOME/conf/btm-config.properties"

