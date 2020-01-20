#!/bin/bash

set -ex

export DJANGO_SETTINGS_MODULE=mma_portal.settings.production
aws ssm get-parameter --name /mma_portal/secrets --query 'Parameter.Value' --output text --region ap-northeast-2 > .env
gunicorn mma_portal.wsgi --access-logfile -
