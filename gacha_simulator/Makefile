.PHONY: init-db
init-db:
	@docker pull mysql:latest
	@docker run -p 3308:3306 --name=gs_mysql -v /home/mysql/gs/conf:/etc/myql/conf.d \
	-v /home/mysql/gs/data:/var/lib/mysql -v /home/mysql/gs/logs:/logs -e MYSQL_ROOT_PASSWORD=123456 -d mysql

.PHONY: build
build:
	@docker build --rm=true -f deploy/Dockerfile -t gacha_simulator .

.PHONY: install
install:
	@docker run --name gacha_simulator1 -p 8001:80 -d gacha_simulator