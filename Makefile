api:
	docker compose exec api bash
db:
	docker compose exec db bash
lint:
	docker compose run --rm --no-deps api flake8 . &
	docker compose run --rm --no-deps api isort --check --diff . &
	docker compose run --rm --no-deps api black --check .
format:
	docker compose run --rm --no-deps api isort . &
	docker compose run --rm --no-deps api black .