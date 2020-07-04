FROM python:3.8.3-buster

ENV TZ Asia/Seoul
ENV DJANGO_SETTINGS_MODULE sanupchae.settings.production

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt \
  --index-url=http://ftp.daumkakao.com/pypi/simple \
  --trusted-host ftp.daumkakao.com

COPY . .

CMD ["scripts/start_django.sh"]
