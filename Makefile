docker-build:
	docker-compose build

run: docker-build
	docker-compose up app

run-interactive:
	docker-compose run app bash
