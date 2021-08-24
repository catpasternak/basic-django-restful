FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN mkdir /wdir
COPY . /wdir/
WORKDIR /wdir

RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "./src/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]