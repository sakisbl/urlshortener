# Django URL Shortener

URL Shortener is a url shortener app made in django for fun.

## Prerequisities
* Python 3
* Django 1.11
* pip

## Installation Instructions
1. Clone the repository
2. Navigate into the urlshortener directory
3. Rename the file urlshortener/settings_secret.py.template to urlshortener/settings_secret.py and fill the DJANGO_KEY variable
4. pip install -r requirements.txt
5. python manage.py makemigrations
6. python manage.py migrate
7. python manage.py createsuperuser
8. python manage.py runserver

You can access the home page by visiting http://localhost:8000
