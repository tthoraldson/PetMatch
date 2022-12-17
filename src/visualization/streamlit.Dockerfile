# visualization/streamlit.Dockerfile
FROM python:3.9-slim

# expose port 8501
EXPOSE 8501

# mkdir app/data
RUN mkdir -p /app/data

# work from app
WORKDIR /app


RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# copy all files to app
COPY ./* /app/

# install python packages
RUN pip3 install -r requirements.txt

# go
ENTRYPOINT ["streamlit", "run", "streamlit.py", "--server.port=8501", "--server.address=0.0.0.0"]