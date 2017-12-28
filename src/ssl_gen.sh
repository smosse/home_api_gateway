#!/bin/sh
if [ ! -f $(cat config.cfg | grep ssl_certificate | cut -d= -f2 ) ]; then
    echo "Certificate not found!, try to generate one"
    mkdir -p ssl
    openssl genrsa -out ssl/myserver.key 2048
    openssl req -new -key ssl/myserver.key -subj "/CN=home_api_gateway" -out ssl/myserver.csr
    openssl x509 -req -days 1000 -in ssl/myserver.csr -signkey ssl/myserver.key -out ssl/myserver.crt
else
   echo "Certificate ok"
fi
