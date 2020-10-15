FROM python:3.8
WORKDIR /usr/src/app

COPY Pipfile.lock Pipfile ./

RUN pip install --upgrade pip &&\
    pip install pipenv && \
    pipenv install &&\
    pipenv install gunicorn

COPY . .

EXPOSE 80
CMD ["pipenv", "run", "gunicorn", "-b", "0.0.0.0:8000", "--chdir", "./api", "api:app"]

