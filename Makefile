PUBLISH_VERSION=$(shell echo ${NEW_VERSION} | sed 's/inner-999/1/g')

GIT_COMMIT=$(shell git rev-parse HEAD)
GIT_ORIGIN=$(shell git config --get remote.origin.url)

build:
	docker build --tag rookout/tutorial-python:latest --tag rookout/tutorial-python:${PUBLISH_VERSION} --build-arg GIT_COMMIT=${GIT_COMMIT} --build-arg GIT_ORIGIN=${GIT_ORIGIN} .


upload-no-latest:
	docker push rookout/tutorial-python:${PUBLISH_VERSION}


upload: upload-no-latest
	@if [ ${CIRCLE_BRANCH} = "master" ]; then \
		docker push rookout/tutorial-python:latest; \
	fi

build-and-upload: build upload