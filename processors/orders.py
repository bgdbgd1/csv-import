from __future__ import annotations

from models import Order
from processors.base import BaseProcessor


class OrdersProcessor(BaseProcessor):
    model_class = Order

    def row_to_model(self, row: dict) -> Order:
        return Order(
            id=row.get("id"),
            customer_id=row.get("customer_id"),
            amount=row.get("amount") or None,
            created_at=row.get("created_at") or None,
        )