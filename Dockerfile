# base image docker
FROM ubuntu

# Update aptitude with new repo
RUN apt-get update

# Install software
RUN apt-get install -y git
RUN apt-get install -y python3
RUN apt-get install -y mc

# Set timezone
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install tzdata && \
    ln -fs /usr/share/zoneinfo/Europe/Moscow /etc/localtime