def validate_payment(payment):
    errors = []

    if payment["amount"] <= 0:
        errors.append("Amount must be greater than 0")

    if not payment["bankAccount"]:
        errors.append("Bank account is missing")

    return errors
