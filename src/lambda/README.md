# Lambda Docs (Local)

## Environment
conda
python 3.9

## Pre-reqs
- aws cli [install](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
- aws sam cli v2
- aws lambda local
- aws sam local
- Docker
- aws stepfunctions local [setup and install](https://docs.aws.amazon.com/step-functions/latest/dg/sfn-local.html)

## Packages
- See individual requirements.txt

## Usage
- Once you've installed AWS SAM LOCAL follow directions in the source document under [Invoking functions locally](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-invoke.html) and in [Running API Gateway locally](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-start-api.html).

- There are two options. You may invoke lambda functions directly via `sam local invoke` or you may send requests to the local API gateway that is run at the URL printed to stdout after running `sam local start-api`. Note: *Requests must be formatted properly if invoking through the API Gateway*
- In this stack, there are two (or more) Lambda functions. For example, `get_auth` and `hello_world`. I recommend testing `hello_world` first.
- Run the `get_auth` function with `sam local invoke "GetAuthFunction" -e ./events/event.json`

What's going on here?

| command             | description                                                                                     | docs                                                                                                                                         |   |   |
|---------------------|-------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|---|---|
| sam local start-api | creates a local API gateway                                                                     | [local APIGW](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-start-api.html)        |   |   |
| sam local invoke    | directly interact with a lambda runtime (container) referring function declared in template.yml | [Invoke lambda locally](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-invoke.html) |   |   |
| "GetAuthFunction"   | refers to the name of the ServerlessFunction resource in sam template.yml                       | ^^                                                                                                                                           |   |   |
| -e {file path}      | sends a sample event directly to the lambda runtime                                             | ^^         
                                                                                                                                  |   |   |


## Putting it all together (with Step Functions)

- [Setup Docs](https://docs.aws.amazon.com/step-functions/latest/dg/sfn-local-docker.html)
- [Local configuration docs](https://docs.aws.amazon.com/step-functions/latest/dg/sfn-local-config-options.html)
- [Testing Step Functions local docs](https://docs.aws.amazon.com/step-functions/latest/dg/sfn-local-lambda.html) (most likely you need Step 5)

```
    # Running step functions local
    docker run -p 8083:8083 --env-file aws-stepfunctions-local-credentials.txt amazon/aws-stepfunctions-local
```