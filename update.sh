#!/bin/bash -e
NAME=cakemail_openapi
rm -rf /tmp/cakeapi-client
openapi-generator generate -i https://api.cakemail.dev/openapi.json -g python -o /tmp/cakeapi-client --package-name ${NAME}
rm -rf ./${NAME}
mv /tmp/cakeapi-client/${NAME} ./${NAME}
