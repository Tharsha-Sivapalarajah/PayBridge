from app.validation.validator import validate_payment

def test_valid_payment():
    payment = {
        "paymentId": "PAY-1",
        "amount": 100,
        "currency": "USD",
        "bankAccount": "123",
        "status": "APPROVED"
    }

    assert validate_payment(payment) == []

def test_negative_amount():
    payment = {
        "paymentId": "PAY-1",
        "amount": -10,
        "currency": "USD",
        "bankAccount": "123",
        "status": "APPROVED"
    }

    errors = validate_payment(payment)
    assert "Amount must be greater than 0" in errors
