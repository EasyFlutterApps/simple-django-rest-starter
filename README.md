# Simple Django Rest Starter  [🔗](https://brickhub.dev/bricks/simple_django_starter/0.1.0+2)

<div align="center">
  <img width="650" height="250" style="background:white;" src="https://soshace.com/wp-content/uploads/2021/01/879-png-3.png" alt="Django logo">
</div>

This is ready to deploy Django Starter Template for backend development which set up all the basic requirements and api routes for a Django project.

[![Powered by Mason](https://img.shields.io/endpoint?url=https%3A%2F%2Ftinyurl.com%2Fmason-badge)](https://github.com/felangel/mason) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)

## 🚀 Features

- Django 4.0 & Python 3.8
- Ready to deploy on Heroku
- SendGrid SMTP support
- Django Rest Framework
- Django Allauth
- Custom Email Based Authentication
- Custom Admin Interface
- CORS Support

## Usage 🚀

```
mason make simple_django_rest_starter
```

## Variables ✨

| variable           | description                  | default | type      |
| ------------------ | ---------------------------- | ------- | --------- |
| `name`     | project name          | Simple Project   | `string`  |
| `email`     | email address         | example@mail.com   | `string`  |
| `password`     | email password          | Null   | `string`  |


## Prerequisites 💬

System Requirements:
- Python 3.8+
- Django 4.0+
- SendGrid API Key

## API Documentation 📚
https://documenter.getpostman.com/view/11585991/UzBjsneE


## Virtual Environment ⚡️

### Windows

- Using Virtualenv: `pip install virtualenv`
```bash
virtualenv venv
cd venv/Scripts
activate
```

### Linux & MacOS
- Using Virtualenv: `pip install virtualenv`
```bash
virtualenv venv
source venv/bin/activate
```

## Installation 📦

### Install requirements

    pip install -r requirements.txt

### Migrations

    python manage.py makemigrations
    python manage.py migrate

### Static files

    python manage.py collectstatic

### Create superuser

    python manage.py createsuperuser

### SMTP email

    EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
    FROM_EMAIL = os.environ['SEND_VERIFY_EMAIL']
    DEFAULT_FROM_EMAIL = os.environ['SEND_VERIFY_EMAIL']
    SENDGRID_ECHO_TO_STDOUT = True
    SENDGRID_API_KEY = os.environ['SEND_GRID_API_KEY']
    SENDGRID_SANDBOX_MODE_IN_DEBUG = False

### Email Verified Redirect URL

    ACCOUNT_CONFIRM_EMAIL_ON_GET = True
    LOGIN_URL = 'http://localhost:8000/email-verified/'

## Deployment 🚀

### Heroku

    heroku login
    heroku config:set DISABLE_COLLECTSTATIC=1 --app <your-app-name>

## Run Locally 🏃

    python manage.py runserver

## Issues 🐛

Here is a list of all the issues I have faced while developing this project. At the end of the development, I fixed all the problems, but I am still working on the issues I have not fixed yet. Some problems arise again, so we can have that issue as soon as possible while working on the projects.

### 1. CircularDependencyError (Filer Package)
Solution: https://github.com/django-cms/django-filer/issues/1296