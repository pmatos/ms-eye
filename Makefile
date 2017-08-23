all: requirements

.PHONY: requirements
requirements: requirements.txt

requirements.txt: requirements.in
	pip-compile -o requirements.in requirements.txt

