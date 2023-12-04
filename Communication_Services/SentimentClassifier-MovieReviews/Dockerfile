FROM python:3.8.13 as base

ARG UID
ARG GID

# Install some packages
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    ffmpeg \
    libsm6 \
    libxext6 \
    vim \
    nano \
    wget \
    curl

# Add a non-root user
RUN addgroup --gid $GID app
RUN adduser --disabled-login --geco '' --uid $UID --gid $GID app

USER app

# Setup some paths
ENV PYTHONPATH=/home/app/.local/lib/python3.8/site-packages:/home/app/project
ENV PATH=$PATH:/home/app/.local/bin

# Install the python packages for this new user
ADD requirements.txt .
RUN pip3 install -r requirements.txt \
    && python3 -m spacy download en_core_web_sm 

WORKDIR /home/app
