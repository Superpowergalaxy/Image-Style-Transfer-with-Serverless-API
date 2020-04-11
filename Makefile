setup:
	python3 -m venv ~/.myvenv
	source ~/.myvenv/bin/activate


install:
	pip install --upgrade pip
	# pip install -r requirements.txt
	sudo wget -O /bin/hadolint https://github.com/hadolint/hadolint/releases/download/v1.17.5/hadolint-Linux-x86_64
	sudo chmod +x /bin/hadolint


lint:
	hadolint Dockerfile 
	# pylint --disable=R,C,W1203 app.py


build:
	docker build --tag=create_music . 


upload:
	bash docker-push.sh


all: install lint build