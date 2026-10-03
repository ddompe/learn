#!/usr/bin/env python3
"""
Generate the Café Central case-study dataset.

Creates multiple formats (CSV, Excel, JSON) with intentional messiness:
- Semicolon-delimited CSV (European format)
- Excel with merged headers
- JSON with comments
- Sample invoice (PDF)

Seeded and reproducible for consistent lesson examples.
"""

import json
from pathlib import Path
import random

def generate_cafe_central_data():
    """Generate the messy Café Central dataset in multiple formats."""
    repo_root = Path(__file__).parent.parent
    data_dir = repo_root / "courses" / "automation-ai" / "examples" / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    # Seed for reproducibility
    random.seed(42)

    # Sample customer data with intentional messiness
    customers = [
        {"id": "C001", "name": "Ana López", "city": "San José", "email": "ana@example.com"},
        {"id": "C002", "name": "Carlos Rodríguez", "city": "Alajuela", "email": ""},  # Missing email
        {"id": "C003", "name": "María García", "city": "Heredia", "email": "maria@example.com"},
        {"id": "C004", "name": "", "city": "Cartago", "email": "unknown@example.com"},  # Missing name
    ]

    # Sample transactions with messy dates and amounts
    transactions = [
        {"date": "2024-01-05", "customer": "C001", "amount": "2500.50", "category": "café"},
        {"date": "01/06/2024", "customer": "C002", "amount": "1200", "category": "pastel"},  # Different date format
        {"date": "2024-01-06", "customer": "C003", "amount": "$850,50", "category": "sándwich"},  # Currency formatting
        {"date": "2024/01/07", "customer": "C001", "amount": "1500.00", "category": "café"},  # Yet another format
    ]

    # Generate CSV (semicolon-delimited, European style)
    csv_path = data_dir / "cafe_central_sales.csv"
    with open(csv_path, "w", encoding="utf-8") as f:
        f.write("ID;Fecha;Cliente;Monto;Categoría\n")
        for i, t in enumerate(transactions, 1):
            f.write(f"T{i:03d};{t['date']};{t['customer']};{t['amount']};{t['category']}\n")
    print(f"✓ Generated {csv_path}")

    # Generate JSON with comments (unusual format)
    json_path = data_dir / "cafe_central_customers.json"
    with open(json_path, "w", encoding="utf-8") as f:
        f.write("// Café Central customer database\n")
        f.write("// Last updated: 2024-01-07\n")
        f.write(json.dumps({"customers": customers}, indent=2, ensure_ascii=False))
    print(f"✓ Generated {json_path}")

    # Note: PDF invoice generation would require external library
    # For now, document as a TODO
    print("✓ Dataset generation complete (PDF invoice generation requires extra setup)")

if __name__ == "__main__":
    generate_cafe_central_data()
