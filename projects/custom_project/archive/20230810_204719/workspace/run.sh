python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python -m main add 1 2

pytest
