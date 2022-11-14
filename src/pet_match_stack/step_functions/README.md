# Using local Step Functions

## Setup:
- At last read, there is not a way to define step functions locally within AWS SAM. The SAM local tool will not launch or create the step functions automatically. 
- So in this case, we'll run the following command(s) to initiate step functions environment instance that can be used to create, or "store", step functions as they're defined within the stack.
- Note: `cd` to the directory where the step function is defined.

Run:
1. `definition=$(cat sfnx.asl.json)`
2. `aws stepfunctions --endpoint http://localhost:8083 create-state-machine --definition $definition --name "PetfinderApiSfxn" --role-arn "arn:aws:iam::012345678901:role/DummyRole"`
3. ```
    Expected output >>
    {
        "stateMachineArn": "arn:aws:states:us-east-1:123456789012:stateMachine:PetfinderApiSfxn",
        "creationDate": "2022-11-13T19:25:17.896000-05:00"
    }
```

## Usage
- Now the step function(s) can be invoked at http://localhost:8083/${function_name}


i.e.
aws stepfunctions --endpoint http://localhost:8083 start-execution --state-machine arn:aws:states:us-east-1:123456789012:stateMachine:PetfinderApiSfxn