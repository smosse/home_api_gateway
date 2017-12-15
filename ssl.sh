
mkdir -p src/ssl

openssl genrsa -out src/ssl/myserver.key 2048
openssl req -new -key src/ssl/myserver.key -subj "/CN=home_api_gateway" -out src/ssl/myserver.csr
openssl x509 -req -days 1000 -in src/ssl/myserver.csr -signkey src/ssl/myserver.key -out src/ssl/myserver.crt
