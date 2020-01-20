#!/bin/bash

set -ex

aws ssm get-parameter --name /mma_portal/secrets --query 'Parameter.Value' --output text --region ap-northeast-2 > .env
gunicorn mma_portal.wsgi --access-logfile -
