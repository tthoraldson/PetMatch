FROM node:16-alpine 

# ==== SETUP ENVS =====

ENV REACT_APP_AUTH0_DOMAIN=${REACT_APP_AUTH0_DOMAIN}
ENV REACT_APP_AUTH0_CLIENTID=${REACT_APP_AUTH0_CLIENTID}
ENV API_URL=${API_URL}

# ==== CONFIGURE =====

# create dirs
RUN mkdir -p /app/frontend

# copy files
COPY . /app/frontend

# set workdir
WORKDIR /app/frontend

# ==== BUILD =====
# Install dependencies when in production (npm ci makes sure the exact versions in the lockfile gets installed)
# RUN npm ci

# install dependencies
RUN npm install -g

# install run
RUN npm install run@1.4.0

# install react scripts
RUN npm install react-scripts@5.0.1 -g

# ==== RUN =======
# expose port
EXPOSE 3000

# serve the app
CMD ["npm","start"]
