# base image docker
FROM ubuntu

# Update aptitude with new repo
RUN apt-get update

# Install software
RUN apt-get install -y git
RUN apt-get install -y python3
RUN apt-get install -y mc
RUN apt-get install -y pip

# Install requirements
COPY requirements.txt /home/requirements.txt
WORKDIR /home/
RUN pip install -r requirements.txt
COPY . /home/

# Set timezone
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install tzdata && \
    ln -fs /usr/share/zoneinfo/Europe/Moscow /etc/localtime