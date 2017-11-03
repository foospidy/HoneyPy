install:
	pip install -r requirements.txt

lint:
	pylint Honey.pylint

clean:
	rm -f *.pyc