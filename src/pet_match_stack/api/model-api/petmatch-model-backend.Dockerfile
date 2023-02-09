 FROM amazonlinux:devel-with-sources

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

# copy requirements.txt
COPY ./requirements.txt  /src/requirements.txt

# use cache for this build step, ensure install based on reqs
RUN pip3 install --no-cache-dir --upgrade -r /src/requirements.txt

# Expose port 8087
EXPOSE 8087

# copy application code
COPY ./* /src/app/
 
# run on port 80
CMD ["uvicorn", "app.petmatch_model_backend:app", "--host", "0.0.0.0", "--port", "8087", "--reload"]

# uvicorn app.petmatch_model_backend:app --host 0.0.0.0 --port 8087 --reload
