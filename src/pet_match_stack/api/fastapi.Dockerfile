 FROM amazonlinux:devel-with-sources as base

# make dirs
RUN mkdir -p /src/app

# set working dir
WORKDIR /src

RUN yum install -y  python3 gcc python3-devel ncurses which nano tree && ln -sf python3 /usr/bin/python

# ensure python pip
RUN python3 -m ensurepip

# setup tools, utils for numpy/sci-kit surprise
RUN pip3 install --upgrade pip setuptools 
RUN pip3 install pendulum service_identity

# upgrade pip
RUN pip3 install --no-cache --upgrade pip 

# install numpy and surprise
RUN pip3 install numpy
RUN pip3 install scikit-surprise 
 
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

# create models dir
RUN mkdir -p /src/app/models/

# move models into place
COPY ./models /src/app/models/

# move shared vars into place
COPY ./config.py /src/
 
# run on port 80, set reload dir explicitly
CMD ["uvicorn", "app.petmatch_backend:app", "--host", "0.0.0.0", "--port", "8086","--reload","--reload-dir","/src/app"]

# keep alive when debugging 
ENTRYPOINT ["tail", "-f", "/dev/null"]

# uvicorn app.petmatch_backend:app --host 0.0.0.0 --port 8086 --reload --reload-dir /src/app