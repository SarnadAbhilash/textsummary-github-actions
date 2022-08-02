install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py --line-length 79

all: install format lint test
