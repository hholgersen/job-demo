FROM python:3.9

RUN pip install kubernetes

COPY main.py /main.py


ENTRYPOINT ["python", "main.py"]
