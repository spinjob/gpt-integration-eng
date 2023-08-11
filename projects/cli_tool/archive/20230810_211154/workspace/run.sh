# a) Install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# b) Run all necessary parts of the codebase
# Install the package
pip install .

# Run the application
string-reverser "hello"

# Run the tests
pytest
