.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help
define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT
BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts


clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

lint: ## check style with pylint
	pylint pydatajson

test: ## run tests quickly with nose
	nosetests

test-all: ## run tests on every Python version with tox
	tox

coverage: ## check code coverage quickly with the default Python

		coverage run --source pydatajson setup.py test

		coverage report -m
		coverage html
		$(BROWSER) htmlcov/index.html

docs: ## generate Sphinx HTML documentation, including API docs
	sphinx-apidoc -o docs/ docs/
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	rm -f docs/conf.rst
	rm -f docs/modules.rst
	# $(BROWSER) docs/_build/html/index.html

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

release: clean ## package and upload a release
	python setup.py sdist upload
	python setup.py bdist_wheel upload

dist: clean ## builds source and wheel package
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

install: clean ## install the package to the active Python's site-packages
	python setup.py install

pypi: ## register the package to PyPi get travis ready to deploy to pip
	make dist
	twine upload dist/*
	python travis_pypi_setup.py

doctoc: ## generate table of contents, doctoc command line tool required
        ## https://github.com/thlorenz/doctoc
	doctoc --maxlevel 3 --gitlab --title "## Indice" docs/
	find docs/ -name "*.md" -exec bash fix_github_links.sh {} \;

serve:
	mkdocs serve

# make specs
# make specs SPECS_NAME=contrataciones-publicas
specs:
	python scripts/dataset_specs.py $(SPECS_NAME)

build:
	mkdocs build
	rsync -vau --remove-source-files site/ docs/
	rm -rf site
	rm -rf docs/guia_abiertos
	rm -rf docs/guia_interoperables
	rm -rf docs/guia_metadatos
	rm -rf docs/guia_apn
	rm -rf docs/guia_subnacionales
	rm -rf docs/perfil_metadatos
	cp -rf docs/guia-abiertos docs/guia_abiertos
	cp -rf docs/guia-interoperables docs/guia_interoperables
	cp -rf docs/guia-metadatos docs/guia_metadatos
	cp -rf docs/guia-apn docs/guia_apn
	cp -rf docs/guia-subnacionales docs/guia_subnacionales
	cp -rf docs/perfil-metadatos docs/perfil_metadatos

pdf:
	mkdocs_datosgobar md2pdf docs/src/guia-abiertos.md docs/pdf/guia-abiertos.pdf
	mkdocs_datosgobar md2pdf docs/src/guia-interoperables.md docs/pdf/guia-interoperables.pdf
	mkdocs_datosgobar md2pdf docs/src/guia-metadatos.md docs/pdf/guia-metadatos.pdf
	mkdocs_datosgobar md2pdf docs/src/guia-apn.md docs/pdf/guia-apn.pdf
	mkdocs_datosgobar md2pdf docs/src/guia-subnacionales.md docs/pdf/guia-subnacionales.pdf
	mkdocs_datosgobar md2pdf docs/src/perfil-metadatos.md docs/pdf/perfil-metadatos.pdf
