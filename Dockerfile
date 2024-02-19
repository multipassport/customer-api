FROM python:3.12-slim

WORKDIR /customer_api

RUN apt-get update \
    && apt-get install -y apt-utils

COPY requirements.txt requirements.txt
RUN pip install --no-cache -r requirements.txt

COPY . /customer_api

CMD [ "./run.sh" ]
