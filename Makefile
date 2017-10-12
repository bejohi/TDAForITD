run:
	python3 scripts/main/main.py

test:
	python3 -m unittest discover -s . -p '*_test.py'

release: test run