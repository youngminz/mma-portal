FROM python:3.8.1-buster

ENV TZ Asia/Seoul

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt \
  --index-url=http://ftp.daumkakao.com/pypi/simple \
  --trusted-host ftp.daumkakao.com

COPY . .
