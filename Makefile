TAG_NAME = dmitry/mysite1

run:
	python3 manage.py runserver

mami:
	python3 manage.py makemigrations

mi:
	python3 manage.py migrate

usedb:
	psql mysite1_db;