# FROM python:3.9
#
# WORKDIR /app
#
# RUN pip install gunicorn==20.1.0
#
# COPY requirements.txt .
#
# RUN pip install -r requirements.txt --no-cache-dir
#
# COPY . .
#
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi"]

# This is a so-called multistage docker file.

#____________________________________________________________________
#                                Build backend
#--------------------------------------------------------------------
FROM python:3.9 AS builder
WORKDIR /app
# RUN pip install gunicorn==20.1.0
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt


#____________________________________________________________________
#                                Backend files
#--------------------------------------------------------------------
FROM python:3.9-slim
WORKDIR /app
COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .
RUN pip install --no-cache /wheels/*
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi"]
