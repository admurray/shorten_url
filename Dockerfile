FROM python:3.11

RUN apt-get update && apt-get install -y supervisor python3-sqlalchemy

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt


COPY conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY . .

RUN python bin/db_setup.py

EXPOSE 8888

CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]