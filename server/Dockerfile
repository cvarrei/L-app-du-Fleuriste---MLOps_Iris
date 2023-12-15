FROM python:3.9-slim

COPY requirements.txt /app/requirements.txt
WORKDIR /app 

RUN pip install -r requirements.txt

COPY model.joblib model.joblib
COPY app.py app.py

CMD ["uvicorn", "--host", "0.0.0.0", "app:app"]