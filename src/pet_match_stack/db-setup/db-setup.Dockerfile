# interfaces with local dynamo db with aws cli, creates its a database during build
FROM amazon/aws-cli:2.9.4 as base
# grab linux 2, run other script

# expose port 8002
EXPOSE 8002:8002

ENV dynamo='dynamo'

# setup mock configuration
RUN aws configure set aws_access_key_id dummyid && \
    aws configure set aws_secret_access_key dummykey && \
    aws configure set default.region us-west-2 

# move database setup script and others into root
COPY . /


# use aws linux 2 as next build stage
FROM amazonlinux:2

RUN yum install -y python3 which tree nano iputils net-tools jq curl python-pip

# install boto3
RUN pip3 install boto3 pandas

# create an app folder to hold data
RUN mkdir -p /app/

# move python script into place
COPY ./loadData.py /

# run python script
# RUN python3 ./loadData.py

# retain all the stuff from base
COPY --from=base / ./

# run shell script to create database and 
ENTRYPOINT ["sh","/setup.sh"]

# keep alive for debugging
# ENTRYPOINT ["tail", "-f", "/dev/null"]