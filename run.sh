#!/bin/bash

echo 'Check if redis is running'
check=`redis-cli ping`

if [[ ${check} == "PONG" ]];
then
  echo "Redis is running"
else
  echo "Redis is not running"
  echo "Starting redis..."
  start_redis=`redis-server --daemonize yes`
  if [[ $1 -eq 1 ]];
  then
     echo "Done"
  fi
fi

export FLASK_APP=run.py
export FLASK_DEBUG=1

nohup python -u run.py > app.log &
