#!/usr/bin/env sh

# This script is used to setup the dynamodb database for the pet_match_stack project.

tables=(
    "users-table-definition.json"
    "rankings-table-definition.json"
    "user-feedback-table-definition.json"
)

for table in "${tables[@]}"; do
    aws dynamodb create-table --cli-input-json file:///schemas/$table --endpoint-url "http://${dynamo}:8001" || true
done




# create tables
# aws dynamodb create-table --cli-input-json file:///schemas/users-table-definition.json --endpoint-url "http://${dynamo}:8001" || true

# aws dynamodb create-table --cli-inputjson file:///schemas/rankings-table-definition.json --endpoint-url "http://${dynamo}:8001" || true

# aws dynamodb create-table --cli-inputjson file:///schemas/user-feedback-table-definition.json --endpoint-url "http://${dynamo}:8001" || true
