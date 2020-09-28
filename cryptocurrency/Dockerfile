FROM python:3.7-slim-stretch

COPY requirements.txt .
RUN pip install -r requirements.txt

ENV APP_HOME /application
WORKDIR $APP_HOME
COPY . ./
RUN chmod 777 ./*

CMD [ "python", "./cryptocurrency/get_process_data.py" ]
CMD [ "gunicorn", "--workers=5", "--threads=1", "-b 127.0.0.1:8050", "app:server "]