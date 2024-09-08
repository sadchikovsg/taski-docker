# This is a so-called multistage docker file.

#____________________________________________________________________
#                                Build backend
#--------------------------------------------------------------------
FROM python:3.9 AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

#____________________________________________________________________
#                                Backend files
#--------------------------------------------------------------------
FROM python:3.9-slim
WORKDIR /app
COPY --from=builder /app/wheels /wheels
RUN pip install --no-cache /wheels/*
COPY api/. ./api
COPY backend/. ./backend
COPY manage.py ./manage.py
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi"]
