# interfaces with local dynamo db with aws cli, creates its a database during build
FROM amazon/aws-cli:2.9.4

# expose port 8002
EXPOSE 8002:8002

ENV dynamo='dynamo'

# setup mock configuration
RUN aws configure set aws_access_key_id dummyid && \
    aws configure set aws_secret_access_key dummykey && \
    aws configure set default.region us-west-2 

# move database setup script into place
COPY ./setup.sh /setup.sh

# install tools to edit text, debug, network, curl, etc
RUN yum install -y which tree nano iputils net-tools

# keep alive
ENTRYPOINT ["sh","/setup.sh"]