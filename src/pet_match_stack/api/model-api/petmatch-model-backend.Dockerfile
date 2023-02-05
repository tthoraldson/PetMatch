 FROM python:3.9-slim
# FROM continuumio/anaconda3:2022.05

# make dirs
RUN mkdir -p /src/app

# set working dir
WORKDIR /src

# copy requirements.txt
COPY ./requirements.txt  /src/requirements.txt

 # use cache for this build step
RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt
# RUN conda install --yes --file /src/requirements.txt

# Expose port 8087
EXPOSE 8087

# copy application code
COPY ./* /src/app/
 
# run on port 80
CMD ["uvicorn", "app.petmatch_model_backend:app", "--host", "0.0.0.0", "--port", "8087", "--reload"]
