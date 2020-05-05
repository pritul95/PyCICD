# Base image
FROM python:3.8-alpine

LABEL "com.github.actions.name" "PyCICD GitHub Action for pytest"
LABEL "com.github.actions.description" "Run pytest commands"

LABEL "com.github.actions.icon" "activity"
LABEL "com.github.actions.color" "black"

# Copy requirements file
COPY requirements.txt /

# Install dependency
RUN pip install -r requirements.txt

ADD entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh", "pytest"]