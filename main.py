from integration.client import fetch_approved_payments
from integration.validator import validate_payment
from integration.transformer import transform_payment
from integration.file_writer import write_payments_to_csv


def run_integration():
    payments = fetch_approved_payments()

    valid_transformed = []

    for payment in payments:
        errors = validate_payment(payment)

        if errors:
            print(f"Validation failed for {payment['paymentId']}: {errors}")
            continue

        transformed = transform_payment(payment)
        valid_transformed.append(transformed)

    write_payments_to_csv(valid_transformed)


if __name__ == "__main__":
    run_integration()
