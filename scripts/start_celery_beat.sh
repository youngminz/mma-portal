#!/bin/bash

set -ex

aws ssm get-parameter --name /sanupchae/secrets --query 'Parameter.Value' --output text --region ap-northeast-2 > .env
python manage.py migrate
celery beat -A sanupchae -l info
