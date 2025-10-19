build-servers:
	@cd ./servers && cargo build --release -p axum-server -p actixw-server

docker-up: build-servers
	docker compose up -d --build

docker-down:
	docker compose down

docker-restart:
	docker compose restart

docker-rebuild: docker-down build-servers
	docker compose up -d --build