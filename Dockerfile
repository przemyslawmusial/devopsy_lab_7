FROM python:3

WORKDIR /src/app

COPY ./app ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "server:app", "--port", "8000", "--host", "0.0.0.0", "--reload"]
