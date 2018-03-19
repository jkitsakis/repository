FROM openjdk:8-jre

COPY traccar-other-3.15.zip /tmp/traccar.zip

RUN set -ex && \
# curl -LSso /tmp/traccar.zip https://github.com/tananaev/traccar/releases/download/v$TRACCAR_VERSION/traccar-other-$TRACCAR_VERSION.zip && \
    unzip -qo /tmp/traccar.zip -d /opt/traccar && \
    rm /tmp/traccar.zip

EXPOSE 8082

ENTRYPOINT ["java", "-Djava.net.preferIPv4Stack=true", "-Xms512m", "-jar", "tracker-server.jar", "traccar.xml"]

#CMD ["conf/traccar.xml"]
