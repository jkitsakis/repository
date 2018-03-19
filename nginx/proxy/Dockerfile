FROM nginx:latest

ARG  SERVER_IP 
ARG  PORTAINER_PORT 
ARG  WORDPRESS_PORT 

#  default conf for proxy service
COPY proxy.conf.template /

# NOT FOUND response
COPY ./backend-not-found.html /var/www/html/backend-not-found.html

#  Proxy and SSL configurations
COPY ./includes/ /etc/nginx/includes/

# Proxy SSL certificates
COPY ./ssl/ /etc/ssl/certs/nginx/

RUN envsubst '$SERVER_IP, $PORTAINER_PORT, $WORDPRESS_PORT' < /proxy.conf.template > /etc/nginx/nginx.conf 
CMD  nginx -g 'daemon off;' 
#CMD cat /etc/nginx/nginx.conf