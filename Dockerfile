FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install flask pytest

EXPOSE 5000

CMD ["python", "src/app.py"]
