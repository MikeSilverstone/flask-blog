up:
	FLASK_APP=main.py FLASK_DEBUG=1 python -m flask run

build:
	pip install flask
	pip install flask-sqlalchemy
	easy_install flask-wtf

init_db:
	FLASK_APP=main.py FLASK_DEBUG=1 python -m flask db init