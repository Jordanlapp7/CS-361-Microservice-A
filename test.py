import requests

def test_get_park_info():
    response = requests.get('http://127.0.0.1:5000/api/park_info')
    if response.status_code == 200:
        print("Park Info Retrieved Successfully")
        print(response.json())
    else:
        print("Failed to retrieve park info")

if __name__ == '__main__':
    test_get_park_info()