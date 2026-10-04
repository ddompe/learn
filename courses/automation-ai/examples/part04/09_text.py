"""Work with text: slicing, cleaning, f-strings, and accents."""

import unicodedata

customer = "  María García  "
print(repr(customer.strip()))
print(customer.strip().upper())
print(customer.strip().replace("García", "Garcia"))

category = "Café"
print(f"Category: {category}, length {len(category)}")


def simplify(text: str) -> str:
    """Lowercase and remove accents, so Café, cafe and café compare equal."""
    decomposed = unicodedata.normalize("NFKD", text.strip().lower())
    return "".join(ch for ch in decomposed if not unicodedata.combining(ch))


for raw in ["Café", "cafe", "café", "Sándwich", "sandwich"]:
    print(f"{raw!r} -> {simplify(raw)!r}")
