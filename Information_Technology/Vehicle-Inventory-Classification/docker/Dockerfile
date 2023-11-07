FROM python:3.8.13 as base

ARG USER_ID
ARG GROUP_ID

# Install some packages
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    ffmpeg \
    libsm6 \
    libxext6 \
    vim \
    wget \
    curl

# Add a non-root user
RUN addgroup --gid $GROUP_ID app
RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID app
USER app

# Setup some paths
ENV PYTHONPATH=/home/app/.local/lib/python3.8/site-packages:/home/app/src
ENV PATH=$PATH:/home/app/.local/bin

# Install the python packages for this new user
ADD requirements.txt .
RUN pip3 install -r requirements.txt

WORKDIR /home/app
