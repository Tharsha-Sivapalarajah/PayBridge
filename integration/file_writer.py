import csv
from datetime import datetime

def write_payments_to_csv(payments):
    if not payments:
        print("No valid payments to write.")
        return

    filename = f"BANK_PAYMENTS_{datetime.now().strftime('%Y%m%d')}.csv"

    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=payments[0].keys())
        writer.writeheader()
        writer.writerows(payments)

    print(f"File generated: {filename}")
