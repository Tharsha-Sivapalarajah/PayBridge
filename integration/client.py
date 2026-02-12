import requests
import time
import logging

ERP_BASE_URL = "http://localhost:5000"
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds


def fetch_approved_payments():
    attempt = 0

    while attempt < MAX_RETRIES:
        try:
            response = requests.get(
                f"{ERP_BASE_URL}/payments?status=APPROVED",
                timeout=5
            )
            response.raise_for_status()

            logging.info("Successfully fetched payments from ERP.")
            return response.json()

        except requests.exceptions.RequestException as e:
            attempt += 1
            logging.warning(
                f"ERP fetch failed (attempt {attempt}/{MAX_RETRIES}): {e}"
            )

            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY)

    logging.error("Failed to fetch payments after maximum retries.")
    return []
