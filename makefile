install:
	pip install uv &&\
		uv sync
	python -m textblob.download_corpora

lint:
	pylint --disable=R,C hello.py

format:
	black *.py

test:
	python -m pytest -vv --cov=hello test_hello.py