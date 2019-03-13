FROM python:latest

WORKDIR /app

COPY app.py .
COPY html/* html/

RUN pip install flask\
                pymongo

ENTRYPOINT ["python"]

CMD ["app.py"]
