Reverse Proxy for ECTN : http://ectn.vm

- Based On : http://linoxide.com/containers/setup-nginx-reverse-proxy-docker/

- Edit windows Host file ( C:\Windows\System32\drivers\etc )

- ssh VM : cd iac/proxy/ssl/
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ectn.key -out ectn.crt