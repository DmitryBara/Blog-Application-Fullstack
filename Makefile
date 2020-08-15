TAG_NAME = dmitry/mysite1

run:
	python3 manage.py runserver

mami:
	python3 manage.py makemigrations

mi:
	python3 manage.py migrate

db:
	psql mysite1_db;





1:
	git add -A
2:
	git commit -m "dev"
3:
	git push heroku master