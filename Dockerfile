FROM python:3.9-buster
LABEL maintainer="Jeff Labonte <grimsleepless@protonmail.com>"

WORKDIR /opt

COPY src/ /opt/
COPY requirements.txt /opt/
COPY docker-entrypoint.sh /opt/

RUN pip install -r requirements.txt

ENTRYPOINT [ "./docker-entrypoint.sh" ]
