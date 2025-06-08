import sys
from qris_saweria import check_paid_status

if len(sys.argv) < 2:
    print("Error: Missing transaction ID!")
    sys.exit(1)

transaction_id = sys.argv[1]

try:
    is_paid = check_paid_status(transaction_id)  # ✅ diperbaiki di sini
    if is_paid:
        print("PAID")
    else:
        print("NOT_PAID")
except Exception as e:
    print(f"ERROR: {e}")
    sys.exit(1)
