help:
	@echo "Usage:"
	@echo "make help           -- display this help"
	@echo "make test           -- run the tests"
	@echo "make runserver      -- run the server"


test:
	coverage run manage.py test --keepdb --verbosity=1
	coverage report -m

runserver:
	python manage.py runserver