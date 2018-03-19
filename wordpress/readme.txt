default.conf
---------------
location /<blog>/ {
  proxy_set_header  Host               $host;
  proxy_set_header  X-Real-IP          $remote_addr;
  proxy_set_header  X-Forwarded-For    $proxy_add_x_forwarded_for;
  proxy_set_header  X-Forwarded-Proto  $scheme;
  proxy_pass http://127.0.0.1:8080/; # <-- mind the trailing slash!
}

wp-config.php
-------------------
define('WP_HOME', ''http://your.site.url:port/yourblog');
define('WP_SITEURL', ''http://your.site.url:port/yourblog');

$_SERVER['REQUEST_URI'] = str_replace("/wp-admin/", "/yourblog/wp-admin/",  $_SERVER['REQUEST_URI']);


sudo chown -R www-data:www-data ./wp