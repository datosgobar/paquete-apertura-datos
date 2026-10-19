.PHONY: help install serve build pdf specs clean
.DEFAULT_GOAL := help

GUIAS := guia-abiertos guia-interoperables guia-metadatos guia-apn guia-subnacionales perfil-metadatos

help: ## muestra esta ayuda
	@grep -hE '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-12s %s\n", $$1, $$2}'

install: ## instala las dependencias del sitio (Node) y de los scripts (Python)
	npm ci
	pip install -r requirements.txt

serve: ## levanta el sitio en local con recarga automatica
	npm run dev

build: ## construye el sitio estatico en dist/
	npm run build

clean: ## borra el sitio construido
	rm -rf dist/ .astro/

pdf: ## genera los PDF de las guias en public/pdf/ (requiere wkhtmltopdf)
	for g in $(GUIAS); do python scripts/md2pdf.py src/content/docs/$$g.md public/pdf/$$g.pdf; done

specs: ## regenera una especificacion de dataset. uso: make specs SPECS_NAME=salud
	python scripts/dataset_specs.py $(SPECS_NAME)
