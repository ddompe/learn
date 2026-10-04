"""Read a secret from the environment instead of writing it in the code."""

import os

api_key = os.environ.get("CAFE_API_KEY")

if api_key is None:
    print("CAFE_API_KEY is not set. Ask the owner for a key and put it in .env.")
else:
    print(f"Key found, {len(api_key)} characters long (the key itself is never printed).")
