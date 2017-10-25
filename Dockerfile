FROM python:3.6
MAINTAINER XenonStack

# Creating Application Source Code Directory
RUN mkdir -p /usr/src/app

# Setting Home Directory for containers
WORKDIR /usr/src/app

#RUN apk add --update python bash

# Installing python dependencies
COPY requirements.txt /usr/src/app/

RUN pip install --no-cache-dir -r requirements.txt

ENV PATH /usr/src/app/bin:$PATH

# Copying src code to Container
COPY . /usr/src/app

# Application Environment variables
ENV APP_ENV development

# Exposing Ports
EXPOSE 6379

# Running Python Application
CMD ["python", "main.py" ]


#FROM jfloff/alpine-python:3.4-onbuild
#MAINTAINER XenonStack
#
## Creating Application Source Code Directory
#RUN mkdir -p /usr/src/app
#
## Setting Home Directory for containers
#WORKDIR /usr/src/app
#
#RUN apk add --update bash
#
## Installing python dependencies
#COPY requirements.txt /usr/src/app/
#
#RUN pip install --no-cache-dir -r requirements.txt
#
#ENV PATH /usr/src/app/bin:$PATH
#
## Copying src code to Container
#COPY . /usr/src/app
#
## Application Environment variables
#ENV APP_ENV development
#
## Exposing Ports
#EXPOSE 6379
#
## Running Python Application
#CMD ["python", "main.py" ]