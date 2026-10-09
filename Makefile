PYTHON := .venv/bin/python
BOOTSTRAP_PYTHON ?= python3.12

.PHONY: setup report test lint all clean

setup:
	$(BOOTSTRAP_PYTHON) -m venv .venv
	$(PYTHON) -m pip install -q --upgrade pip
	$(PYTHON) -m pip install -q -r requirements.txt

report:
	$(PYTHON) scripts/build_report.py > /dev/null
	@echo "Wrote reports/summary.md, reports/tables/, reports/figures/"

test:
	$(PYTHON) -m pytest -q

lint:
	$(PYTHON) -m ruff check .
	$(PYTHON) -m ruff format --check .

all: lint test report

clean:
	rm -rf .venv .pytest_cache .ruff_cache **/__pycache__
