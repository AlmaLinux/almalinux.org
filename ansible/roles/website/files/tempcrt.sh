#!/bin/bash

openssl req -x509 -nodes -days 398 -newkey rsa:2048 \
    -keyout /etc/ssl/selfsigned.key \
    -out /etc/ssl/selfsigned.crt \
    -subj '/C=ES/ST=Moon/L=Moon/O=Acme Inc./OU=IT Department/CN=localhost'
