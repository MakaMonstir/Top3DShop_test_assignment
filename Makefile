build:
	docker-compose build

run:
	docker-compose up --remove-orphans

build-run:
	docker-compose up --build --remove-orphans