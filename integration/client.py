import requests

ERP_BASE_URL = "http://localhost:5000"

def fetch_approved_payments():
    try:
        response = requests.get(f"{ERP_BASE_URL}/payments?status=APPROVED")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching payments: {e}")
        return []
