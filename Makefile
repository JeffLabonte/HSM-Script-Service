SHELL := /usr/bin/env bash

install: venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -r requirements.txt

venv:
	@if [ ! -d .venv ]; then\
		echo "[-] Creating venv";\
		python3 -m venv .venv;\
	else\
		echo "[-] venv already exists";\
	fi


