#!/usr/bin/env sh

# This script is used to setup the dynamodb database for the pet_match_stack project.

# cat the json file for the attribute definitions
# cat the json file for the key schema
attri_def=$(cat ./users-table-schema.json | jq -c .Attribute-definitions)
key_schema=$(cat ./users-table-schema.json | jq -c .key-schema)


# cat the json file for the rankings table attribute definitions
# cat the json file for the rankings table key schema
rankings_attri_def=$(cat ./rankings-table-schema.json | jq -c .Attribute-definitions)
rankings_key_schema=$(cat ./rankings-table-schema.json | jq -c .key-schema)

# create tables
aws dynamodb create-table \
    --table-name users_table  \
    # --attribute-definitions AttributeName=userId,AttributeType=N  \
    # --key-schema AttributeName=userId,KeyType=HASH  \
    --attribute-definitions $attri_def \
    --key-schema $key_schema \
    --billing-mode PAY_PER_REQUEST  \
    --endpoint-url "http://${dynamo}:8001"


aws dynamodb create-table \
    --table-name rankings_table  \
    # --attribute-definitions AttributeName=  \
    # --key-schema AttributeName=  \
    --attribute-definitions $attri_def \
    --key-schema $key_schema \
    --billing-mode PAY_PER_REQUEST  \
    --endpoint-url "http://${dynamo}:8001"