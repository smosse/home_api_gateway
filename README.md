# Home Api Gateway

Home Api Gateway is an Python Program to simplify and Secure Home Devices APIs.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Supported Devices

- Orange TV decoders
- SamsungTV

### Prerequisites

- Python 2.7 with Openssl

OR

- Docker

For docker Deployment please see https://hub.docker.com/r/jfpucheu/home_api_gateway/
### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```shell
cd src
```

Install requirements:

```shell
pip install -r requirements.txt
```

Configure the gateway:

```shell
vim config.cfg
```

Generate SSL Certificates if Needed:

```shell
./ssl_gen.sh
```

Start the program:
```shell
./main.py
```


The programme Should start and display the current config

## Examples:

### Orange TV Decoder

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

### Samsung TV


## Authors

* **Jean-François PUCHEU** - *Initial work* - [jfpucheu](https://github.com/jfpucheu)

## License

This project is licensed under the Apache 2 License - see the [LICENSE.md](LICENSE.md) file for details.
