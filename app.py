from flask import Flask, jsonify
import requests

app = Flask(__name__)

NPS_API_BASE_URL = "https://developer.nps.gov/api/v1"
NPS_API_KEY = "QyyfdqI2VZOk6kbUGx2YuvEg6N1cIdPm6WeAg4NS"

@app.route('/api/park_info', methods=['GET'])
def get_park_info():
    response = requests.get(f"{NPS_API_BASE_URL}/parks?api_key={NPS_API_KEY}")
    if response.status_code == 200:
        park_data = response.json()
        return jsonify(park_data)
    else:
        return jsonify({"error": "Failed to retrieve park information"}), response.status_code
    
if __name__ == '__main__':
    app.run(debug=True)