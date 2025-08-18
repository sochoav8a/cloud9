install:
	pip install uv &&\
		uv sync
	python -m textblob.download_corpora

lint:
	pylint --disable=R,C *.py nlplogic/*.py

format:
	black *.py nlplogic/*.py

test:
	python -m pytest -vv --cov=wikiphrases --cov =nlplogic test_core_nlp.py