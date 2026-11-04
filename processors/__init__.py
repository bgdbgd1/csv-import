from __future__ import annotations

from pathlib import Path

from processors.customers import CustomersProcessor
from processors.orders import OrdersProcessor

# Map filename prefix → processor class.
# To add a new import job: add a model in models.py, a processor class,
# and register it here.
_REGISTRY: dict[str, type] = {
    "orders":    OrdersProcessor,
    "customers": CustomersProcessor,
}


def get_processor(filepath: str) -> object:
    """
    Select the right processor based on the filename.

    The stem of the filename (everything before the first underscore or dot)
    is matched against the registry keys.

    Examples:
      orders.csv            → OrdersProcessor
      orders_20261104.csv   → OrdersProcessor
      customers_nov.csv     → CustomersProcessor
    """
    stem = Path(filepath).stem.lower()          # e.g. "orders_20261104"
    base = stem.split("_")[0]                   # e.g. "orders"

    if base not in _REGISTRY:
        known = list(_REGISTRY)
        raise ValueError(
            f"No processor for '{Path(filepath).name}'. "
            f"Filename must start with one of: {known}"
        )

    return _REGISTRY[base]()