FROM python:3.10

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
RUN python /app/src/prepare_model.py

CMD ["python", "/app/src/main.py"]
