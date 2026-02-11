def transform_payment(payment):
    return {
        "PaymentID": payment["paymentId"],
        "Beneficiary": payment["vendor"],
        "Amount": payment["amount"],
        "Currency": payment["currency"],
        "Account": payment["bankAccount"],
        "BankCode": payment["bankCode"]
    }
