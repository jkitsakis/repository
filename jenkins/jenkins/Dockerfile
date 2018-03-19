FROM jenkins:latest
#1.625.3

# Set the number of executors
COPY config/executors.groovy /usr/share/jenkins/ref/init.groovy.d/executors.groovy

USER root
RUN chown -R jenkins:jenkins /var/jenkins_home
