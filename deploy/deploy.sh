#!/bin/bash
if [ $# -eq 0 ]; then
    echo 'Must provide the action of docker-compose as input'
    echo 'Usually : up -d or down'
    exit
fi

ACTION="$*"

echo "Starting alpine llama 3.2"
docker-compose -f "dc.alpine_llama" ${ACTION}
exit
