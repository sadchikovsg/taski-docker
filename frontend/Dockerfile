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

FROM busybox:uclibc
COPY --from=build_frontend /app/build/. /frontend_static
CMD ["echo", "The frontend files have been copied."]
