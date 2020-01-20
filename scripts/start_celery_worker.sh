#!/bin/bash

set -ex

aws ssm get-parameter --name /mma_portal/secrets --query 'Parameter.Value' --output text --region ap-northeast-2 > .env
celery worker -A mma_portal -l info
