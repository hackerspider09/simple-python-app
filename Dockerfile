# Base image
FROM python:3.11-slim

# create work dir
WORKDIR /app

# Copy all content 
COPY . .

# Install requirements
RUN pip3 install -r requirements.txt

# Default command to run python server it can be override to run tests 
# by pytest tests.py
CMD [ "python3", "app.py" ]
