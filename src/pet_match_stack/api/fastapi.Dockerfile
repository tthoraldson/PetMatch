 FROM python:3.9-slim
 
# set working dir
WORKDIR /src

# copy requirements.txt
COPY ./requirements.txt  /src/requirements.txt
 
 # use cache for this build step
RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

# Expose port 8086
EXPOSE 8086

# copy application code
COPY ./app /src/app
 
# run on port 80
CMD ["uvicorn", "app.petmatch_backend:app", "--host", "0.0.0.0", "--port", "8086", "--reload"]