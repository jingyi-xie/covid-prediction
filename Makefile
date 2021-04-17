setup:
	python3 -m venv ~/.covid_venv

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	hadolint Dockerfile 
	pylint --disable=R,C,W1203 app.py

all: install lint