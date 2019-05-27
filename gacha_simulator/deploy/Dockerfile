FROM python:3.6-slim

ADD ./requirements.pip /app/requirements.pip
WORKDIR /app

RUN /usr/local/bin/pip3 install --upgrade pip setuptools

RUN apt-get update -yqq && \
    apt-get install -yqq --force-yes --no-install-recommends build-essential default-libmysqlclient-dev  wget xz-utils libfontconfig1 libxrender1 libxtst6 && \
    /usr/local/bin/pip3 --no-cache-dir install -r requirements.pip && \
    apt-get purge -yqq --force-yes build-essential && \
    apt-get autoremove -yqq --force-yes

RUN /usr/local/bin/pip3 --no-cache-dir install gunicorn

ADD . /app

EXPOSE 80
ENTRYPOINT ["/app/deploy/entrypoint.sh"]
