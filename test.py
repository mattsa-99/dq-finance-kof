import requests

BASE_URL = "https://fa-dq-finance-c5gshna0gnb9hdhz.eastus2-01.azurewebsites.net/api/dq_finance"

def test_get_request():
    """Prueba con parámetro en query string"""
    params = {"name": "Kevin"}
    response = requests.get(BASE_URL, params=params)
    print("🔹 GET Response:")
    print(f"Status: {response.status_code}")
    print(f"Body: {response.text}\n")

def test_post_request():
    """Prueba con JSON en el body"""
    payload = {"name": "Kevin"}
    headers = {"Content-Type": "application/json"}
    response = requests.post(BASE_URL, json=payload, headers=headers)
    print("🔹 POST Response:")
    print(f"Status: {response.status_code}")
    print(f"Body: {response.text}\n")

if __name__ == "__main__":
    print("=== Testing Azure Function locally ===\n")
    test_get_request()
    test_post_request()
