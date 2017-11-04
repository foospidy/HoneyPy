install:
	pip install -r requirements.txt

lint:
	pylint Honey.py
	pylint lib/honeypy_console.py
	pylint lib/honeypy_logtail.py

format:
	autopep8 --in-place --aggressive --aggressive --ignore=E501,W690 Honey.py
	autopep8 --in-place --aggressive --aggressive --ignore=E501,W690 lib/honeypy_console.py
	autopep8 --in-place --aggressive --aggressive --ignore=E501,W690 lib/honeypy_logtail.py

clean:
	rm -f *.pyc