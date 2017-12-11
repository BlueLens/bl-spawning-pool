FROM bluelens/python:3.6
MAINTAINER bluehackmaster <master@bluehack.net>

USER root
# Creating Application Source Code Directory
RUN mkdir -p /usr/src/app

# Copying src code to Container
COPY . /usr/src/app

# Setting Home Directory for containers
WORKDIR /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

ENV PATH /usr/src/app/bin:$PATH

# Application Environment variables
ENV APP_ENV development

# Exposing Ports
EXPOSE 6379

# Running Python Application
CMD ["python3", "run.py" ]

