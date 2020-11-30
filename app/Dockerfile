FROM python:3.8

WORKDIR /app

COPY requirements.txt /app/

RUN apt-get update
RUN apt-get install -y libsm6 libxext6 libxrender-dev
RUN apt install -y libgl1-mesa-glx
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "app:app", "-c", "./gunicorn.conf.py"]