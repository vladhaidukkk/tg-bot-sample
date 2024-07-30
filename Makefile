default: fmt lint

run:
	python -m bot.main

fmt:
	ruff format

lint:
	ruff check

fix:
	ruff check --fix
