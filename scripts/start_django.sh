#!/bin/bash

set -ex

aws ssm get-parameter --name /sanupchae/secrets --query 'Parameter.Value' --output text --region ap-northeast-2 > .env
gunicorn sanupchae.wsgi --access-logfile -
