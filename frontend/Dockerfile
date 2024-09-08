# FROM node:18
# WORKDIR /app
#
# COPY package.json package.json
# COPY package-lock.json package-lock.json
#
# RUN npm install
#
# COPY . .
# RUN npm run build
#
# CMD ["npx", "-y", "http-server", "-p", "8000", "/app/build"]



# This is a so-called multistage docker file.

#____________________________________________________________________
#                                Build frontend
#--------------------------------------------------------------------

FROM node:18 AS build_frontend
WORKDIR /app
COPY package*.json .
# COPY package-lock.json package-lock.json
RUN npm install
COPY . .
RUN npm run build

#____________________________________________________________________
#                                Frontend files
#--------------------------------------------------------------------

FROM scratch
COPY --from=build_frontend /app/build ./app/build

