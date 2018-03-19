FROM nginx:latest



#  default conf for proxy service
COPY ./proxy.conf /etc/nginx/conf.d/proxy.conf

# NOT FOUND response
COPY ./backend-not-found.html /var/www/html/backend-not-found.html

#  Proxy and SSL configurations
COPY ./includes/ /etc/nginx/includes/

# Proxy SSL certificates
COPY ./ssl/ /etc/ssl/certs/nginx/