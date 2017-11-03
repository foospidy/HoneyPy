install:
	pip install -r requirements.txt

lint:
	pylint Honey.py

clean:
	rm -f *.pyc