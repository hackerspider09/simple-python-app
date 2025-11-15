# Stage 1: Build Stage
FROM python:3.11-slim AS builder

# create work dir
WORKDIR /app

# Copy requirements file
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Production Stage
FROM python:3.11-slim

WORKDIR /app

# Copy virtual environment from the builder stage
COPY --from=builder /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
COPY . .

# Default command to run python server it can be override to run tests 
# by pytest tests.py
CMD [ "python3", "app.py" ]
