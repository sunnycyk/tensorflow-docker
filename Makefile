SERVICE=tensor-flow

all: clean build run_bare_bash shell

clean:
	-docker rm -f ${SERVICE}

build:
	docker build -t ${SERVICE} .

run_bare_bash:
	docker run --name ${SERVICE} \
	    -p 6006:6006 \
		-v "${PWD}":/usr/src/app \
		-it -d ${SERVICE} bash 

shell:
	docker exec -it ${SERVICE} bash
 