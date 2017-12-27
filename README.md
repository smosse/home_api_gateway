# Docker image for [Home Api Gateway](https://github.com/jfpucheu/home_api_gateway - Home Api Gateway for Connected Objects

[![Build Status](https://travis-ci.org/jfpucheu/home_api_gateway.svg?branch=master)](https://travis-ci.org/jfpucheu/home_api_gateway)
[![Docker Automated build](https://img.shields.io/docker/automated/jfpucheu/home_api_gateway.svg)](https://hub.docker.com/r/jfpucheu/home_api_gateway/)
[![Docker Stars](https://img.shields.io/docker/stars/jfpucheu/home_api_gateway.svg)](https://hub.docker.com/r/jfpucheu/home_api_gateway/)
[![Docker Pulls](https://img.shields.io/docker/pulls/jfpucheu/home_api_gateway.svg)](https://hub.docker.com/r/jfpucheu/home_api_gateway/)

The image is based on [Alpine Linux](https://alpinelinux.org/) and built daily.

## Supported tags

- `latest` [(latest/Dockerfile)](latest/Dockerfile)

### Prerequisities


In order to run this container you'll need docker installed.

* [Windows](https://docs.docker.com/windows/started)
* [OS X](https://docs.docker.com/mac/started/)
* [Linux](https://docs.docker.com/linux/started/)

## How to use this image

### Install

Install the container:

```shell
docker pull jfpucheu/home_api_gateway
```

Alternatively, pull a specific version:

```shell
docker pull jfpucheu/home_api_gateway:latest
```

### Usage

```shell
docker run -d -p 8443:8443 jfpucheu/home-api-gateway -e USERNAME=admin -e  PASSWORD=toto
```

#### Environment Variables

* `USERNAME` - Username for API Gateway (default: admin)
* `PASSWORD` - Password for API Gateway (default: password)
* `LISTENPORT` - Listen port for API Gateway (default: 8443)
* `ORANGETVIP` - Orange TV Decoder Ip Address (default: 192.168.1.1)
* `SAMSUNGTVIP` - Samsung TV Ip Address (default: 192.168.1.1)
* `SAMSUNGTVMODEL` - Samsung TV Model (default: UE40D6200)

#### Supported requests OrangeTV:

Start Orange Decoder:

```shell
curl --insecure --user 'admin':'password' -H "Content-Type: application/json" -X POST -d '{"state":"ON"}' https://127.0.0.1:8443/orange/tv/
```

Select à Channel on Orange Decoder:

```shell
curl --insecure --user 'admin':'password' -H "Content-Type: application/json" -X POST -d '{"channel":"4"}' https://127.0.0.1:8443/orange/tv/
```

or:

```shell
curl --insecure --user 'admin':'password' -H "Content-Type: application/json" -X POST -d '{"channel":"CH+"}' https://127.0.0.1:8443/orange/tv/
```

Switch OFF Orange Decoder:

```shell
curl --insecure --user 'admin':'password' -H "Content-Type: application/json" -X POST -d '{"state":"OFF"}' https://127.0.0.1:8443/orange/tv/
```

#### Supported requests: SamsunTV:

Key Action:

```shell
curl -v --insecure --user 'admin':'password!' -H "Content-Type: application/json" -X POST -d '{"key":"KEY_POWEROFF"}' https://127.0.0.1:8443/samsung/tv/
```

Key List:

#'KEY_0', # --TOUCHE 0
#'KEY_1', # --TOUCHE 1
#'KEY_2', # --TOUCHE 2
#'KEY_3', # --TOUCHE 3
#'KEY_4', # --TOUCHE 4
#'KEY_5', # --TOUCHE 5
#'KEY_6', # --TOUCHE 6
#'KEY_7', # --TOUCHE 7
#'KEY_8', # --TOUCHE 8
#'KEY_9', # --TOUCHE 9
#'KEY_UP', # --CROIX HAUT
#'KEY_DOWN', # --CROIX BAS
#'KEY_LEFT', # --CROIX GAUCHE
#'KEY_RIGHT', # --CROIX DROITE
#'KEY_MENU', # --TOUCHE MENU
#'KEY_PRECH', # --TOUCHE PRE-CH
#'KEY_GUIDE', # --TOUCHE GUIDE
#'KEY_INFO', # --TOUCHE INFO
#'KEY_RETURN', # --TOUCHE RETURN
#'KEY_CH_LIST', # --TOUCHE CH LIST
#'KEY_EXIT', # --TOUCHE EXIT
#'KEY_ENTER', # --CROIX ENTER
#'KEY_SOURCE', # --TOUCHE SOURCE
#'KEY_AD'
#'KEY_PLAY', # --TOUCHE PLAY
#'KEY_PAUSE', # --TOUCHE PAUSE
#'KEY_MUTE', # --TOUCHE MUTE
#'KEY_PICTURE_SIZE', # --
#'KEY_VOLUP', # --TOUCHE VOL +
#'KEY_VOLDOWN', # --TOUCHE VOL -
#'KEY_TOOLS', # --TOUCHE TOOLS
#'KEY_POWEROFF', # --TOUCHE POWEROFF
#'KEY_CHUP', # --TOUCHE PROG +
#'KEY_CHDOWN', # --TOUCHE PROG -
#'KEY_CONTENTS', # --TOUCHE SMART HUB
#'KEY_W_LINK', # --TOUCHE Media P
#'KEY_RSS', # --TOUCHE Internet
#'KEY_MTS', # --TOUCHE Dual
#'KEY_CAPTION', # --TOUCHE Subt
#'KEY_REWIND', # --TOUCHE <>
#'KEY_REC',
#'KEY_STOP' ]) # --TOUCHE STOP

## Authors

* **Jean-François PUCHEU** - *Initial work* - [jfpucheu](https://github.com/jfpucheu)

## License

This project is licensed under the Apache 2 License - see the [LICENSE.md](LICENSE.md) file for details.
