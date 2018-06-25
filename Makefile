PUBLISH_VERSION=$(shell echo ${NEW_VERSION} | sed 's/inner-999/1/g')


build:
	docker build --tag rookout/tutorial-python:latest --tag rookout/tutorial-python:${PUBLISH_VERSION} .


upload-no-latest:
	docker push rookout/tutorial-python:${PUBLISH_VERSION}


upload: upload-no-latest
	@if [ ${CIRCLE_BRANCH} = "master" ]; then \
		docker push rookout/tutorial-python:latest; \
	fi

build-and-upload: build upload