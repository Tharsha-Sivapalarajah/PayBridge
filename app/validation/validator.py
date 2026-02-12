ALLOWED_CURRENCIES = ["USD", "LKR", "EUR"]


def validate_payment(payment):
    errors = []

    if payment["amount"] <= 0:
        errors.append("Amount must be greater than 0")

    if payment["currency"] not in ALLOWED_CURRENCIES:
        errors.append("Unsupported currency")

    if not payment["bankAccount"]:
        errors.append("Bank account is missing")

    if payment["status"] != "APPROVED":
        errors.append("Payment not approved")

    return errors
