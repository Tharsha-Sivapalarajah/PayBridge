from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock ERP payment data
PAYMENTS = [
    {
        "paymentId": "PAY-1001",
        "vendor": "ABC Suppliers",
        "amount": 250000.00,
        "currency": "LKR",
        "bankAccount": "1234567890",
        "bankCode": "7010",
        "status": "APPROVED"
    },
    {
        "paymentId": "PAY-1002",
        "vendor": "XYZ Traders",
        "amount": -5000.00,  # Invalid (negative)
        "currency": "USD",
        "bankAccount": "9876543210",
        "bankCode": "7050",
        "status": "APPROVED"
    },
    {
        "paymentId": "PAY-1003",
        "vendor": "LMN Corp",
        "amount": 15000.00,
        "currency": "EUR",
        "bankAccount": "",
        "bankCode": "7090",
        "status": "APPROVED"
    },
    {
        "paymentId": "PAY-1004",
        "vendor": "Test Company",
        "amount": 30000.00,
        "currency": "USD",
        "bankAccount": "222333444",
        "bankCode": "7020",
        "status": "PENDING"
    }
]

@app.route("/payments", methods=["GET"])
def get_payments():
    status = request.args.get("status")
    if status:
        filtered = [p for p in PAYMENTS if p["status"] == status]
        return jsonify(filtered)
    return jsonify(PAYMENTS)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
