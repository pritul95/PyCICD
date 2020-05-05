# Base image
FROM python:3.8-alpine

# Copy requirements file
COPY requirements.txt /

# Install dependency
RUN pip install -r requirements.txt

# Copy exntrypoint.sh and make it executable
COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

# Set entrypoint
ENTRYPOINT ["/entrypoint.sh"]