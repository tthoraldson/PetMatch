#!/usr/bin/env sh

# This script is used to setup the dynamodb database for the pet_match_stack project.
aws dynamodb create-table \
    --table-name users_table  \
    --attribute-definitions AttributeName=userId,AttributeType=N  \
    --key-schema AttributeName=userId,KeyType=HASH  \
    --billing-mode PAY_PER_REQUEST  \
    --endpoint-url "http://${dynamo}:8001"