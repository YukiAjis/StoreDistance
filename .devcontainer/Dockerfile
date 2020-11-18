FROM python:3.8-slim

WORKDIR /tmp/work

COPY requirements.txt ${PWD}
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
