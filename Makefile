.PHONY: install-uv install lint type test checks clean

UV_COMMAND := uv

run-server:
	mcp-uniprot

install-uv:
	@which $(UV_COMMAND) >/dev/null 2>&1 || (echo "Could not find 'uv'! Installing..."; curl -LsSf https://astral.sh/uv/install.sh | sh)

install:
	uv sync --all-extras

lint:
	uv run ruff check --fix src
	uv run ruff format src

type:
	uv run mypy src --install-types --non-interactive --show-traceback

test:
	uv run pytest tests

checks: lint type test

pre-commit:
	uv run pre-commit run --all-files

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".uv" -exec rm -rf {} +
	rm -rf .mypy_cache
	rm -rf .ruff_cache
	rm -rf .cache
	rm -rf .env
	rm -rf .env.local
	rm -rf .env.development.local
	rm -rf .env.test.local
