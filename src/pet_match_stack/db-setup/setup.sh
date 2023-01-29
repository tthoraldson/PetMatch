#!/usr/bin/env sh

# This script is used to setup the dynamodb database for the pet_match_stack project.

# create tables
aws dynamodb create-table --cli-input-json file:///schemas/users-table-definition.json --endpoint-url "http://${dynamo}:8001"

aws dynamodb create-table --cli-inputjson file:///schemas/rankings-table-definition.json --endpoint-url "http://${dynamo}:8001"

# TODO
# finish table setup with secondary indexes, etc