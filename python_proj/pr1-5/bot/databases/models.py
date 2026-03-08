import re
from typing import Optional
from sqlalchemy import BigInteger, ForeignKey, String, Integer, Float, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, validates
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine


class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(BigInteger)
    name: Mapped[Optional[str]] = mapped_column(String(100))
    phone: Mapped[Optional[str]] = mapped_column(String(20))
    email: Mapped[Optional[str]] = mapped_column(String(100), unique=True)
    points: Mapped[int] = mapped_column(default=0)

    # @validates('email')
    # def validate_email(self, key, address):
    #     if not re.match(r"[^@]+@[^@]+\.[^@]+", address):
    #         raise ValueError("Failed simple email validation")
    #     return address

    # @validates('phone')
    # def validate_phone(self, key, number):
    #     clean_number = re.sub(r"[\s\-()]", "", number)
    #     if not re.match(r"^\+?\d{10,15}$", clean_number):
    #         raise ValueError("Invalid phone number format")
    #     return clean_number

class Drink(Base):
    __tablename__ = 'drinks'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    series: Mapped[str] = mapped_column(String(50))
    price: Mapped[float] = mapped_column(Float)
    photo_id: Mapped[str] = mapped_column(String(255), nullable=True)
engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')
async_session = async_sessionmaker(engine)

async def db_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)