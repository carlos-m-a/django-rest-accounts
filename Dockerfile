# pull official base image
FROM python:3.12 as dev

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN python -m pip install --upgrade pip
COPY ./requirements.txt .
COPY docker/dev-requirements.txt .
RUN python -m pip install -r requirements.txt
RUN python -m pip install -r dev-requirements.txt

# copy project
COPY . .

# Expose port 8000
EXPOSE 8000

# Commands to be executed when container is run
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000