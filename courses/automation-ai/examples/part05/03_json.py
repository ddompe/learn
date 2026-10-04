"""JSON: objects, arrays, nesting, and a file with comments (which is not strict JSON)."""

import json
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
raw = (DATA / "cafe_central_customers.json").read_text(encoding="utf-8")

try:
    json.loads(raw)
except json.JSONDecodeError as error:
    print("Strict JSON fails:", error.msg)

body = "\n".join(line for line in raw.splitlines() if not line.lstrip().startswith("//"))
customers = json.loads(body)["customers"]
print("Customers:", len(customers))
print("First customer:", customers[0])

missing_name = [c["id"] for c in customers if not c["name"]]
missing_email = [c["id"] for c in customers if not c["email"]]
print("Without a name:", missing_name)
print("Without an email:", missing_email)

record = {"id": "C009", "name": "Daniela Mora", "email": None, "tags": ["frecuente", "san josé"]}
print(json.dumps(record, ensure_ascii=False))
print(json.dumps(record))
