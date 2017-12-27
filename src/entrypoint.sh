#!/bin/sh

# Create user
#useradd myservice

# Setup config
#sed -i "s/PASSWD/${SERVICE_PASSWORD}/g" /etc/myservice.conf

# Start service
#exec /usr/sbin/myservice "$@"

if [ ! -f $(cat config.cfg | grep ssl_certificate | cut -d= -f2 ) ]; then
    echo "Certificate not found!, try to generate one"
    mkdir -p ssl
    openssl genrsa -out ssl/myserver.key 2048
    openssl req -new -key ssl/myserver.key -subj "/CN=home_api_gateway" -out ssl/myserver.csr
    openssl x509 -req -days 1000 -in ssl/myserver.csr -signkey ssl/myserver.key -out ssl/myserver.crt
else
   echo "Certificate ok"
fi

# Setup config
echo "Configuration App ....."

sed -i -e '/username =/ s/= .*/= '${USERNAME:-admin}'/' config.cfg
sed -i -e '/password =/ s/= .*/= '${PASSWORD:-password}'/' config.cfg
sed -i -e '/port =/ s/= .*/= '${LISTENPORT:-8443}'/' config.cfg
sed -i -e '/orange_ip =/ s/= .*/= '${ORANGETVIP:-192.168.1.1}'/' config.cfg
sed -i -e '/tv_ip =/ s/= .*/= '${SAMSUNGTVIP:-192.168.1.1}'/' config.cfg
sed -i -e '/tv_model =/ s/= .*/= '${SAMSUNGTVMODEL:-UE40D6200}'/' config.cfg

echo "Starting App ....."
python ./main.py
