FROM python:3.5
USER root
ENV PYTHONUNBUFFERED 1
RUN mkdir /config
ENV LD_RUN_PATH=/usr/local/lib
ADD /config/requirements.pip /config/
RUN pip install -r /config/requirements.pip
RUN mkdir /src;
WORKDIR /src
