.PHONY: help clean clean-eggs clean-build clean-pyc clean-test test test-student test-registration lint lint-fix install pre-commit-install pre-commit-run

help:
	@echo "Comandos disponíveis:"
	@echo "  make test              - Executa todos os testes (student + registration)"
	@echo "  make test-student      - Executa testes do student_service"
	@echo "  make test-registration - Executa testes do registration_service"
	@echo "  make lint              - Instala e executa pre-commit em todos os arquivos"
	@echo "  make lint-fix          - Executa pre-commit tentando corrigir automaticamente"
	@echo "  make pre-commit-install - Instala os hooks do pre-commit"
	@echo "  make pre-commit-run    - Executa pre-commit em todos os arquivos"
	@echo "  make clean             - Remove arquivos temporários e cache"
	@echo "  make clean-pyc         - Remove arquivos Python compilados"
	@echo "  make clean-test        - Remove arquivos de teste e cache"

clean: clean-eggs clean-build clean-pyc clean-test

clean-eggs:
	@find . -name '*.egg' -print0 | xargs -0 rm -rf --
	@rm -rf .eggs/

clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info

clean-pyc:
	@find . -iname '*.pyc' -delete
	@find . -iname '*.pyo' -delete
	@find . -iname '*~' -delete
	@find . -iname '*.swp' -delete
	@find . -iname '__pycache__' -type d -exec rm -rf {} + 2>/dev/null || true
	@find . -iname '*.py[cod]' -delete

clean-test:
	@rm -rf .pytest_cache/
	@rm -rf .coverage
	@rm -rf htmlcov/
	@rm -rf .tox/
	@rm -rf .cache
	@find . -type d -name '*.egg-info' -exec rm -rf {} + 2>/dev/null || true

test:
	@echo "Executando testes de todos os serviços..."
	@cd student_service && export PYTHONPATH=.:$$PYTHONPATH && python -m pytest tests/ -v
	@cd registration_service && export PYTHONPATH=.:$$PYTHONPATH && python -m pytest tests/ -v

test-student:
	@echo "Executando testes do student_service..."
	@cd student_service && export PYTHONPATH=.:$$PYTHONPATH && python -m pytest tests/ -v

test-registration:
	@echo "Executando testes do registration_service..."
	@cd registration_service && export PYTHONPATH=.:$$PYTHONPATH && python -m pytest tests/ -v

lint: pre-commit-install pre-commit-run

lint-fix:
	@pre-commit run --all-files --hook-stage manual || true

pre-commit-install:
	@pre-commit install

pre-commit-run:
	@pre-commit run --all-files -v

install:
	@pip install -r requirements.txt
