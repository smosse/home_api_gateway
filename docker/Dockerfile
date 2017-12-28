FROM python:2.7-alpine3.6

MAINTAINER jfpucheu@gmail.com

WORKDIR /usr/src/app

COPY ../src/requirements.txt .

# Install packages
RUN apk --update add --no-cache \
        curl \
        gcc \
        musl-dev \
        python-dev \
        libffi-dev \
        openssl-dev \
        openssl \
    && rm -rf /var/cache/apk/* \
    && rm -rf /usr/src/app/ssl/* \
    && pip install --no-cache-dir -r requirements.txt

COPY ../src/ .
COPY entrypoint.sh .

RUN rm -rf /usr/src/app/ssl/*

EXPOSE 80 443
CMD [ "./entrypoint.sh" ]
