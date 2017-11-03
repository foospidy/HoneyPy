install:
	pip install -r requirements.txt

lint:
	pylint Honey.py

format:
	autopep8 --in-place --aggressive --aggressive --ignore=E501,W690 Honey.py
clean:
	rm -f *.pyc