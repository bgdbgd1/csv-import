from __future__ import annotations

from models import Customer
from processors.base import BaseProcessor


class CustomersProcessor(BaseProcessor):
    model_class = Customer

    def row_to_model(self, row: dict) -> Customer:
        return Customer(
            id=row.get("id"),
            name=row.get("name"),
            email=row.get("email"),
            created_at=row.get("created_at") or None,
        )