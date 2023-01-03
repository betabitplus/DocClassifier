FROM python:3.7.2

WORKDIR /app
COPY /app /app

RUN apt-get update && \
    apt-get install ffmpeg libsm6 libxext6  -y

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "run.py"]
