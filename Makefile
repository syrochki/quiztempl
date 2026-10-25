.PHONY: help rundev daphne-build daphne-up daphne-logs daphne-bu daphne-d lf lint format

help: ## Show this help
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-14s\033[0m %s\n", $$1, $$2}'

rundev: ## Run Django development server
	uv run quiztempl runserver

daphne-build: ## Build development Docker images (compose.dev.yaml)
	docker compose -f compose.dev.yaml build

daphne-up: ## Start development containers in background
	docker compose -f compose.dev.yaml up -d

daphne-logs: ## Follow development container logs
	docker compose -f compose.dev.yaml logs -f

daphne-bu: ## Build and start development containers in background
	docker compose -f compose.dev.yaml up --build -d

daphne-d: ## Build, start, and follow logs of development containers
	docker compose -f compose.dev.yaml up --build -d && docker compose -f compose.dev.yaml logs -f

lf: ## Lint and format (ruff + mypy)
	uv run ruff format .
	uv run ruff check . --fix
	uv run mypy .

lint: ## Type-check with mypy
	uv run mypy .

format: ## Format and autofix with ruff
	uv run ruff format .
	uv run ruff check . --fix