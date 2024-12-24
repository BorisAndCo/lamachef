#!/bin/bash
if [ $# -eq 0 ]; then
    echo 'Must provide the action of docker-compose as input'
    echo 'Usually : up -d or down'
    exit
fi

ACTION="$*"

echo "Starting genuine llama3"
docker compose -f "dc.genuine_llama3.yaml" ${ACTION}
exit
