import logging

from app.erp.client import fetch_approved_payments
from app.validation.validator import validate_payment
from app.transformation.transformer import transform_payment
from app.file_handling.file_writer import write_payments_to_csv
from app.persistence.repository import (
    init_db,
    is_payment_processed,
    mark_payment_processed,
)

def run():
    logging.info("Starting PayBridge integration job")

    init_db()

    payments = fetch_approved_payments()

    if not payments:
        logging.warning("No payments retrieved.")
        return

    processed_batch = []

    for payment in payments:
        payment_id = payment["paymentId"]

        if is_payment_processed(payment_id):
            logging.info(f"Skipping duplicate payment {payment_id}")
            continue

        errors = validate_payment(payment)

        if errors:
            logging.warning(f"Validation failed for {payment_id}: {errors}")
            continue

        transformed = transform_payment(payment)
        processed_batch.append(transformed)

        mark_payment_processed(payment_id)

    write_payments_to_csv(processed_batch)

    logging.info("Integration job completed")
