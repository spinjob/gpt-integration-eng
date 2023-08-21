python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

python main.py &
python api.py &
python auth.py &
python workflow.py &
python data_mapping.py &
