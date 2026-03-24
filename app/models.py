# models.py
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase


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
