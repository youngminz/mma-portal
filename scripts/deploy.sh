#!/bin/bash

set -ex

$(aws ecr get-login --no-include-email --region ap-northeast-2)
docker build -t mma_portal/django .
docker tag mma_portal/django:latest "$(aws sts get-caller-identity --output text --query 'Account')".dkr.ecr.ap-northeast-2.amazonaws.com/mma_portal/django:latest
docker push "$(aws sts get-caller-identity --output text --query 'Account')".dkr.ecr.ap-northeast-2.amazonaws.com/mma_portal/django:latest

aws ecs update-service --region ap-northeast-2 --cluster ECSCluster --service mma-portal --force-new-deployment
