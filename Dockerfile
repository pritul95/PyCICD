# Base image
FROM python:3.8-alpine

LABEL "com.github.actions.name" "PyCICD GitHub Action"
LABEL "com.github.actions.description" "All in one Github Actions CICD library - written in Python"

LABEL "com.github.actions.icon" "activity"
LABEL "com.github.actions.color" "black"

# Copy requirements file
COPY requirements.txt /

# Install dependencies
RUN pip install -r requirements.txt

ADD entrypoint.sh /entrypoint.sh
ADD main.py /main.py

ENTRYPOINT ["/entrypoint.sh"]