# models.py
from datetime import datetime
from typing import List, Optional
from sqlalchemy import ForeignKey, String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase


class Base(DeclarativeBase):
    pass


class Part(Base):
    __tablename__ = "parts"

    id: Mapped[int] = mapped_column(primary_key=True)
    sku: Mapped[str] = mapped_column(
        String(70), unique=True, index=True, nullable=False
    )
    vendor_sku: Mapped[Optional[str]] = mapped_column(
        String(70), index=True, nullable=True
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)

    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))

    category: Mapped["Category"] = relationship(back_populates="parts")
    stock: Mapped["Stock"] = relationship(back_populates="part")
    movements: Mapped[List["StockMovement"]] = relationship(back_populates="part")

    def __repr__(self):
        return f"Part(sku={self.sku!r}, name={self.name!r})"


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(
        String(50), unique=True, index=True, nullable=False
    )
    parts: Mapped[List["Part"]] = relationship(back_populates="category")

    def __repr__(self):
        return f"categories(id={self.id!r}, name={self.name!r})"


class Stock(Base):
    __tablename__ = "stock"

    id: Mapped[int] = mapped_column(primary_key=True)
    quantity: Mapped[int] = mapped_column(nullable=False, default=0)

    part_id: Mapped[int] = mapped_column(ForeignKey("parts.id"), unique=True)

    part: Mapped["Part"] = relationship(back_populates="stock")

    def __repr__(self):
        return f"Stock(part_id={self.part_id!r}, quantity={self.quantity!r})"


class Supplier(Base):
    __tablename__ = "suppliers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    contact_info: Mapped[Optional[str]] = mapped_column(String(255))

    movements: Mapped[List["StockMovement"]] = relationship(back_populates="supplier")


class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    movements: Mapped[List["StockMovement"]] = relationship(back_populates="customer")


class StockMovement(Base):
    __tablename__ = "stock_movements"

    id: Mapped[int] = mapped_column(primary_key=True)
    part_id: Mapped[int] = mapped_column(ForeignKey("parts.id"), index=True)

    quantity: Mapped[int] = mapped_column(nullable=False)

    movement_type: Mapped[str] = mapped_column(String(20))
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    supplier_id: Mapped[Optional[int]] = mapped_column(ForeignKey("suppliers.id"))
    customer_id: Mapped[Optional[int]] = mapped_column(ForeignKey("customers.id"))

    note: Mapped[Optional[str]] = mapped_column(String(255))

    part: Mapped["Part"] = relationship(back_populates="movements")
    supplier: Mapped["Supplier"] = relationship(back_populates="movements")
    customer: Mapped["Customer"] = relationship(back_populates="movements")
