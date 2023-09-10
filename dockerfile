FROM pypy:latest
WORKDIR /app
COPY . /app
CMD ["python" , "manage.py" , "runserver", "0.0.0.0:8000"]

