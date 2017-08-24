all: requirements

.PHONY: requirements
requirements: requirements.txt

requirements.txt: requirements.in
	pip-compile -o requirements.txt requirements.in

