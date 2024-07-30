default: fmt lint

fmt:
	ruff format

lint:
	ruff check

fix:
	ruff check --fix
