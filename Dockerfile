FROM python:3.7-slim-stretch

WORKDIR app/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY cryptocurrency/ ./cryptocurrency/
RUN chmod 777 ./cryptocurrency/*

CMD [ "python", "./cryptocurrency/get_process_data.py" ]