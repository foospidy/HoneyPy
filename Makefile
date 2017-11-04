install:
	pip install -r requirements.txt

lint:
	pylint Honey.py
	pylint lib/honeypy_console.py

format:
	autopep8 --in-place --aggressive --aggressive --ignore=E501,W690 Honey.py
	autopep8 --in-place --aggressive --aggressive --ignore=E501,W690 lib/honeypy_console.py

clean:
	rm -f *.pyc