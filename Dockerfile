FROM python:3.12
LABEL maintainer = 'jmhman'

ENV PYTHONUNBUFFERED 1

RUN python -m venv /py

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app

WORKDIR /app
EXPOSE 8000

ARG DEV=false
RUN /py/bin/pip install --upgrade pip && \
  /py/bin/pip install -r /tmp/requirements.txt && \
  apt-get update && \
  apt-get install -y postgresql-client build-essential libpq-dev && \
  if [ "$DEV" = "true" ] ; \
    then echo "===THIS IS DEVELOPMENT BUILD===" && \
    /py/bin/pip install -r /tmp/requirements.dev.txt ; \
  fi && \
  apt-get remove -y --purge build-essential libpq-dev && \
  apt-get clean && \
  rm -rf /tmp && \
  adduser \
    --disabled-password \
    --no-create-home \ 
    django-user

ENV PATH="/py/bin/:$PATH"

USER django-user

