from qris_saweria import create_payment_qr
import sys
import json

try:
    saweria_username = sys.argv[1]
    amount = int(sys.argv[2])
    email = sys.argv[3]

    qr_string, transaction_id, _ = create_payment_qr(saweria_username, amount, email)

    print(json.dumps({
        "qr_string": qr_string,
        "transaction_id": transaction_id
    }))

except Exception as e:
    print(json.dumps({"error": str(e)}))
