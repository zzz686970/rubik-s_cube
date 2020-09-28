FROM python:3.7-slim-stretch
RUN mkdir cryptocurrency
WORKDIR cryptocurrency

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . ./
RUN chmod 777 ./*

#CMD [ "python", "./cryptocurrency/get_process_data.py" ]
CMD [ "gunicorn", "--workers=5", "--threads=1", "-b 0.0.0.0:8050", "app:server"]
