FROM python:3.9.16-slim-bullseye

# install chromedriver
RUN apt-get update && apt-get install -yqq unzip git bash curl wget gnupg
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/112.0.5615.28/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

RUN echo 'export PATH=$PATH:/usr/local/bin/' >> ~/.bash_profile \
RUN source ~/.bash_profile

# install google-chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

RUN wget -O /tmp/chrome.deb https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_112.0.5615.165-1_amd64.deb
RUN dpkg -i /tmp/chrome.deb

RUN mkdir /home/PoC
WORKDIR /home/PoC