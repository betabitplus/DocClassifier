DOCKER_USERNAME ?= avramenko
APPLICATION_NAME ?= document-classifier
GIT_HASH ?= $(shell git log --format="%h" -n 1)
PORT := 5000


build:
	docker build --tag ${DOCKER_USERNAME}/${APPLICATION_NAME}:${GIT_HASH} .

run: build
	docker run -itd -p $(PORT):$(PORT) ${DOCKER_USERNAME}/${APPLICATION_NAME}:${GIT_HASH}

open:
	open 'http://localhost:'$(PORT)

push:
	docker push ${DOCKER_USERNAME}/${APPLICATION_NAME}:${GIT_HASH}

release:
	docker pull ${DOCKER_USERNAME}/${APPLICATION_NAME}:${GIT_HASH}
	docker tag  ${DOCKER_USERNAME}/${APPLICATION_NAME}:${GIT_HASH} ${DOCKER_USERNAME}/${APPLICATION_NAME}:latest
	docker push ${DOCKER_USERNAME}/${APPLICATION_NAME}:latest