# Django Base Template
A basic django template that registers a custom user model and has a basic code structure setup to start with.

## User Model
The registered user model does nothing except removing the "email" field requirement for superuser creation.

## Code structure
This project houses all apps in an `apps/` subdirectory to keep the root of the project cleaner. 
It also houses all static files and templates in designated directories, and configures these in the settings.

## Libraries
This project has a few basic libraries saved to `requirements.txt`

* black - the best python formatter around
* django-environ - best django environment manager around

## Local Development
This project comes with a `compose.yaml` with a postgres:13.10 database ready to run with docker. The project settings are configured to via `.env/.local.env` to connect to this database.
Simply run `python manage.py makemigrations && python manage.py migrate`, and then `python manage.py createsuperuser` and finally `python manage.py runserver`.
