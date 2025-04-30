install:
	uv pip install --upgrade pip && \
	uv pip install -r requirements.txt

clean:
	rm -rf .pytest_cache .ruff_cache

dev: install
	uv pip install -r dev-requirements.txt

help:
	@echo "Available commands:"
	@echo "  install  - Upgrade pip and install packages from requirements.txt"
	@echo "  clean    - Remove .pytest_cache and .ruff_cache directories"
	@echo "  dev      - Run install and then install dev dependencies from dev-requirements.txt"
	@echo "  help     - Show this help message"
