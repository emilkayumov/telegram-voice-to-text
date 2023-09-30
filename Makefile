init:
	pip install -r requirements.txt

run:
	python src/main.py

docker-build:
	docker build -t telegram-voice-to-text .

docker-run:
	docker run -it telegram-voice-to-text

docker-run-daemon:
	docker run -d telegram-voice-to-text

.PHONY: init run docker-build docker-run docker-run-daemon
