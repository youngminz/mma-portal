#!/bin/bash

set -ex

aws ssm get-parameter --name /sanupchae/secrets --query 'Parameter.Value' --output text --region ap-northeast-2 > .env
celery worker -A sanupchae -l info
