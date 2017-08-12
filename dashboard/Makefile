
install:
	python manage.py migrate

test:
	coverage run manage.py test --keepdb --verbosity=1
	coverage report -m

runserver:
	python manage.py runserver