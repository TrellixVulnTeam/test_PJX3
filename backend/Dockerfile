FROM ubuntu:14.04
RUN apt-get update && apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib -y
RUN su - postgres
RUN service postgresql start
CMD psql
