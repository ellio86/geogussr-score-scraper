run: venv/bin/activate 
	./venv/bin/python3 score-scraper.py

setup:
	pip install -r requirements.txt

clean:
	rm -rf __pycache__
	rm -rf venv

venv/bin/activate: requirements.txt
 python3 -m venv venv
 ./venv/bin/pip install -r requirements.txt
