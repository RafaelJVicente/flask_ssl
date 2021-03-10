#!/bin/bash

# Generate CA certificate (no password)
openssl genrsa -out root_ca.key 2048
openssl req -x509 -new -nodes -key root_ca.key -sha256 -days 1024 -out root_ca.crt -subj "/C=ES/ST=Madrid/L=Madrid/O=Company/OU=Department/emailAddress=info@example.com/CN=CA"

# Generate client request and sign it by the CA
openssl genrsa -out client.key 2048
openssl req -new -key client.key -out client.csr -subj "/C=ES/ST=Madrid/L=Madrid/O=Company/OU=Department/emailAddress=info@example.com/CN=localhost" -addext "subjectAltName=DNS:localhost,IP:127.0.0.1"  # CN=Client
openssl x509 -req -in client.csr -CA root_ca.crt -CAkey root_ca.key -CAcreateserial -out client.crt -days 1024 -sha256

# Define the PEM files for CA and client
cat root_ca.crt root_ca.key > root_ca.pem
cat client.crt client.key > client.pem

# Generate server request
#openssl genrsa -out server.key 2048
#openssl req -x509 -new -nodes -key server.key -sha256 -days 1024 -out server.crt -subj "/C=ES/ST=Madrid/L=Madrid/O=Company/OU=Department/emailAddress=info@example.com/CN=Server"
#cat server.crt server.key > server.pem
