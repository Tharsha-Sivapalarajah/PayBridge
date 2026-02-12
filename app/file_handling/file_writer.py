import csv
import os
from datetime import datetime
import logging


def write_payments_to_csv(payments):
    if not payments:
        logging.info("No valid payments to write.")
        return

    filename = f"BANK_PAYMENTS_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    temp_filename = f"{filename}.tmp"

    try:
        with open(temp_filename, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=payments[0].keys())
            writer.writeheader()
            writer.writerows(payments)

        os.replace(temp_filename, filename)

        logging.info(f"File generated successfully: {filename}")

    except Exception as e:
        logging.error(f"Error writing payment file: {e}")
        if os.path.exists(temp_filename):
            os.remove(temp_filename)
