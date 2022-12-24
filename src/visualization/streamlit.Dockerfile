# visualization/streamlit.Dockerfile
FROM python:3.9-slim

# expose port 8501
EXPOSE 8501

# mkdir app/data
RUN mkdir -p /app/data

# mkdir rankings directory
RUN mkdir -p /app/data/rankings

# mkdir app/pages
RUN mkdir -p /app/pages

# work from app
WORKDIR /app


RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# copy all files to app
COPY ./* /app/

# ensure pages are copied to location
COPY ./pages/* /app/pages/

# TODO 
# copy rankings to location

# install python packages
RUN pip3 install -r requirements.txt

# go
ENTRYPOINT ["streamlit", "run", "petmatch.py", "--server.port=8501", "--server.address=0.0.0.0"]