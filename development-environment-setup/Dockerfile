FROM ubuntu:16.04

ENV USERNAME developer

RUN adduser --disabled-password --quiet --gecos '' $USERNAME
ARG USER_HOME_DIR="/home/"$USERNAME
# Install Oracle Java 8
RUN apt-get update && apt-get install --assume-yes apt-utils
RUN apt-get install -y software-properties-common curl 
RUN apt-add-repository -y ppa:webupd8team/java 
RUN apt-get update \
   && echo "oracle-java8-installer shared/accepted-oracle-license-v1-1  select true" |  debconf-set-selections
RUN apt-get install -y oracle-java8-set-default 

# Set Oracle Java as the default Java
RUN update-java-alternatives -s java-8-oracle
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle
# Clean Up APT when finished
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install MAVEN
RUN apt-get install -y wget
RUN wget --no-verbose -O /tmp/apache-maven-3.3.9-bin.tar.gz http://www-eu.apache.org/dist/maven/maven-3/3.3.9/binaries/apache-maven-3.3.9-bin.tar.gz

# Install maven
RUN tar xzf /tmp/apache-maven-3.3.9-bin.tar.gz -C /opt/
RUN ln -s /opt/apache-maven-3.3.9 /opt/maven
RUN ln -s /opt/maven/bin/mvn /usr/local/bin
RUN rm -f /tmp/apache-maven-3.3.9-bin.tar.gz

ENV MAVEN_HOME /opt/maven
ENV M2_HOME "$USER_HOME_DIR/.m2"
EXPOSE 80 443
VOLUME "$USER_HOME_DIR/.m2"

# Install Eclipse 
ENV DOWNLOAD_URL http://download.eclipse.org/technology/epp/downloads/release/neon/R/eclipse-jee-neon-R-linux-gtk-x86_64.tar.gz
ENV INSTALLATION_DIR /usr/local

RUN apt-get update && apt-get install --assume-yes apt-utils
RUN apt-get install -y curl libgtk2.0-0 libxtst6 
RUN curl -fsSL "$DOWNLOAD_URL" | tar vxz -C $INSTALLATION_DIR 
RUN apt-get --purge autoremove -y software-properties-common curl 
RUN apt-get clean

COPY ./eclipse.ini $INSTALLATION_DIR/eclipse/eclipse.ini
RUN chown -R root:developer $INSTALLATION_DIR/eclipse
RUN chmod -R 775 $INSTALLATION_DIR/eclipse

USER developer
ENTRYPOINT $INSTALLATION_DIR/eclipse/eclipse

