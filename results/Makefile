VENV=venv

.PHONY: serve
serve: venv
	"$(VENV)/bin/jupyter-notebook" results.ipynb

venv:
	python3 -m venv "$(VENV)"
	"$(VENV)/bin/pip" install notebook pandas
