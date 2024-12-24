migrations:
	python manage.py makemigrations
mutation:
	python manage.py makemigrations
	python manage.py migrate
superuser:
	python manage.py createsuperuser
server:
	python manage.py runserver 0.0.0.0:8000
static:
	python manage.py collectstatic --no-input
shell:
	python manage.py shell
cache:
	python manage.py createcachetable
dev-backup:
	python manage.py dumpdata --natural-foreign --natural-primary --indent 2 > fixtures/full-db.json
dev-restore:
	python manage.py loaddata full-db