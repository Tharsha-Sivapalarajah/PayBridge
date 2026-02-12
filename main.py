import logging

from integration.client import fetch_approved_payments
from integration.validator import validate_payment
from integration.transformer import transform_payment
from integration.file_writer import write_payments_to_csv
from integration.logger_config import setup_logging

from persistence.repository import (
    init_db,
    is_payment_processed,
    mark_payment_processed
)


def run_integration():
    setup_logging()
    logging.info("Starting PayBridge integration process...")

    try:
        init_db()

        payments = fetch_approved_payments()

        if not payments:
            logging.warning("No payments retrieved from ERP.")
            return

        valid_transformed = []

        for payment in payments:
            payment_id = payment["paymentId"]

            if is_payment_processed(payment_id):
                logging.info(f"Skipping already processed payment: {payment_id}")
                continue

            errors = validate_payment(payment)

            if errors:
                logging.warning(
                    f"Validation failed for {payment_id}: {errors}"
                )
                continue

            transformed = transform_payment(payment)
            valid_transformed.append(transformed)

            mark_payment_processed(payment_id)
            logging.info(f"Payment marked as processed: {payment_id}")

        write_payments_to_csv(valid_transformed)

        logging.info("Integration completed successfully.")

    except Exception as e:
        logging.error(f"Critical integration failure: {e}")


if __name__ == "__main__":
    run_integration()
