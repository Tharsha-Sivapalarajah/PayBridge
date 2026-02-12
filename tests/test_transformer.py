from app.transformation.transformer import transform_payment

def test_transformation_structure():
    payment = {
        "paymentId": "PAY-1",
        "vendor": "ABC",
        "amount": 100,
        "currency": "USD",
        "bankAccount": "123",
        "bankCode": "7010"
    }

    transformed = transform_payment(payment)

    assert transformed["PaymentID"] == "PAY-1"
    assert transformed["Beneficiary"] == "ABC"
