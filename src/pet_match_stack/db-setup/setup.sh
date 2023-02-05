#!/usr/bin/env sh

# This script is used to setup the dynamodb database for the pet_match_stack project.

tables=(
    "users-table-definition.json"
    "rankings-table-definition.json"
    "user-feedback-table-definition.json"
    "cats-adoptable-table-definition.json"
    "dogs-adoptable-master-table-definition.json"
    "dogs-adoptable-contentbased-table-definition.json"
)

for table in "${tables[@]}"; do
    aws dynamodb create-table --cli-input-json file:///schemas/$table --endpoint-url "http://dynamo:8001" || true
done


python3 ./loadData.py