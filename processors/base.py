from __future__ import annotations

import csv
from abc import ABC, abstractmethod

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import Base


class BaseProcessor(ABC):
    """
    Base class for all file processors.

    Subclasses declare:
      - model_class: the SQLAlchemy model they produce
      - row_to_model: how to map one CSV row (dict of strings) to a model instance

    The run() method handles everything else: opening the file, managing the
    DB session, and committing the transaction.
    """

    @property
    @abstractmethod
    def model_class(self):
        ...

    @abstractmethod
    def row_to_model(self, row: dict) -> object:
        ...

    def run(self, filepath: str, dsn: str) -> int:
        engine = create_engine(dsn)

        # Create the table if it doesn't exist yet (idempotent)
        Base.metadata.create_all(engine)

        with open(filepath, newline="") as f:
            rows = list(csv.DictReader(f))

        print(f"Read {len(rows)} rows from {filepath}")

        with Session(engine) as session:
            objects = [self.row_to_model(row) for row in rows]
            session.add_all(objects)
            session.commit()

        return len(objects)