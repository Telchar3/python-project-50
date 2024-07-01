install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=getdiff --cov-report xml

lint:
	poetry run flake8 getdiff

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build


publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user dist/*.whl --force

.PHONY: install test lint selfcheck check build publish
