# visualization/dynamo.Dockerfile
FROM amazon/dynamodb-local:1.20.0

# expose port 8001
EXPOSE 8001

# run dynamodb
CMD ["-jar", "DynamoDBLocal.jar", "-sharedDb", "-delayTransientStatuses", "-cors", "*", "-dbPath" ,"./data", "-port", "8001"]


