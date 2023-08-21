python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

export FLASK_APP=main.py
flask run

pytest
