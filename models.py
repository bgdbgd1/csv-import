from __future__ import annotations

from datetime import date
from decimal import Decimal

from sqlalchemy import Date, Numeric, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Order(Base):
    __tablename__ = "orders"

    id:          Mapped[str]            = mapped_column(Text, primary_key=True)
    customer_id: Mapped[str | None]     = mapped_column(Text)
    amount:      Mapped[Decimal | None] = mapped_column(Numeric)
    created_at:  Mapped[date | None]    = mapped_column(Date)


class Customer(Base):
    __tablename__ = "customers"

    id:         Mapped[str]           = mapped_column(Text, primary_key=True)
    name:       Mapped[str | None]    = mapped_column(Text)
    email:      Mapped[str | None]    = mapped_column(Text)
    created_at: Mapped[date | None]   = mapped_column(Date)