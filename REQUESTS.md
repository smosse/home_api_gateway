```shell
#[Orange TV Decoder]
# zapper sur la 2:
curl --insecure --user 'admin':'password' -H "Content-Type: application/json" -X POST -d '{"channel":"2"}' https://127.0.0.1:8443/orange/tv/

# chaine +1:
curl --insecure --user 'admin':'password' -H "Content-Type: application/json" -X POST -d '{"channel":"CH+"}' https://127.0.0.1:8443/orange/tv

# chaine -1:
curl --insecure --user 'admin':'password' -H "Content-Type: application/json" -X POST -d '{"channel":"CH-"}' https://127.0.0.1:8443/orange/tv

# Allumer le decoder:
curl --insecure --user 'admin':'password' -H "Content-Type: application/json" -X POST -d '{"state":"ON"}' https://127.0.0.1:8443/orange/tv

# Eteindre le decoder:
curl --insecure --user 'admin':'password' -H "Content-Type: application/json" -X POST -d '{"state":"OFF"}' https://127.0.0.1:8443/orange/tv

# Volume + :
curl --insecure --user 'admin':'password' -H "Content-Type: application/json" -X POST -d '{"volume":"VOL+"}' https://127.0.0.1:8443/orange/tv

# Volume - :
curl --insecure --user 'admin':'password' -H "Content-Type: application/json" -X POST -d '{"volume":"VOL-"}' https://127.0.0.1:8443/orange/tv

```
