VENV=venv

.PHONY: serve
serve: venv
	"$(VENV)/bin/jupyter-notebook" results.ipynb

.PHONY: build
build: index.html

index.html: results.ipynb venv
	"$(VENV)/bin/jupyter-nbconvert" results.ipynb --to html --output $@

venv:
	python3 -m venv "$(VENV)"
	"$(VENV)/bin/pip" install itables notebook pandas
