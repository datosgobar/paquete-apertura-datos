.PHONY: help serve build pdf specs doctoc clean
.DEFAULT_GOAL := help

help: ## muestra esta ayuda
	@grep -hE '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-12s %s\n", $$1, $$2}'

serve: ## levanta el sitio en local con recarga automatica
	mkdocs serve

build: ## construye el sitio estatico en site/
	mkdocs build

clean: ## borra el sitio construido
	rm -rf site/

pdf: ## genera los PDF de las guias en docs/pdf/
	mkdocs_datosgobar md2pdf docs/guia-abiertos.md docs/pdf/guia-abiertos.pdf
	mkdocs_datosgobar md2pdf docs/guia-interoperables.md docs/pdf/guia-interoperables.pdf
	mkdocs_datosgobar md2pdf docs/guia-metadatos.md docs/pdf/guia-metadatos.pdf
	mkdocs_datosgobar md2pdf docs/guia-apn.md docs/pdf/guia-apn.pdf
	mkdocs_datosgobar md2pdf docs/guia-subnacionales.md docs/pdf/guia-subnacionales.pdf
	mkdocs_datosgobar md2pdf docs/perfil-metadatos.md docs/pdf/perfil-metadatos.pdf

specs: ## regenera una especificacion de dataset. uso: make specs SPECS_NAME=salud
	python scripts/dataset_specs.py $(SPECS_NAME)

doctoc: ## regenera los indices de los .md (requiere doctoc)
	doctoc --maxlevel 3 --gitlab --title "## Indice" docs/
	find docs/ -name "*.md" -exec bash scripts/fix_github_links.sh {} \;
