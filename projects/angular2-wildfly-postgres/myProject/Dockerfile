FROM alpine:3.4.0

ENV APP_NAME "myProject"
ENV APP_DIR /home/$APP_NAME
ENV CONFIG_TEMP_DIR=/tmp/app_config

#RUN mkdir -p  $APP_DIR 
#RUN mkdir -p  $CONFIG_TEMP_DIR 

ADD app_config/ $CONFIG_TEMP_DIR/
ADD package.json $APP_DIR/package.json
ADD src/ $APP_DIR/src/

# Add entry-point
ADD docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]

# WORKDIR $APP_DIR
# RUN npm install --global angular-cli 
##RUN npm install && npm cache clean

#EXPOSE 4200 49152
#RUN ["ng", "build"]
#CMD ["ng", "start", "--host=0.0.0.0"]