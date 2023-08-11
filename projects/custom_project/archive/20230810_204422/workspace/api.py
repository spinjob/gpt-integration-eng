import requests
import json

def fetch_data():
    # Fetch data from API
    response = requests.get('https://api.example.com/data')
    
    # Parse the JSON data
    data = json.loads(response.text)
    
    return data
