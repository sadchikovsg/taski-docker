# This is a so-called multistage docker file.

#____________________________________________________________________
#                                Build frontend
#--------------------------------------------------------------------

FROM node:18 AS build_frontend
WORKDIR /app
COPY package.json package.json
COPY package-lock.json package-lock.json
RUN npm ci
COPY . .
RUN npm run build

#____________________________________________________________________
#                                Frontend files
#--------------------------------------------------------------------

FROM scratch
COPY --from=build_frontend /app/build ./app/build

