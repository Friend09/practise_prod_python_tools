compile:
	uv pip compile requirements.in -o requirements.txt

dev: install
	uv pip install -r dev-requirements.txt

install:
	uv pip install --python 3.12 --upgrade pip && \
	uv pip install --python 3.12 -r requirements.txt ; \
	clear

clean:
	rm -rf .pytest_cache .ruff_cache

all: clean compile install

help:
	@echo "Available commands:"
	@echo "  compile  - updates requirements.txt based on requirements.in document"
	@echo "  install  - Upgrade pip and install packages from requirements.txt"
	@echo "  clean    - Remove .pytest_cache and .ruff_cache directories"
	@echo "  dev      - Run install and then install dev dependencies from dev-requirements.txt"
	@echo "  help     - Show this help message"
