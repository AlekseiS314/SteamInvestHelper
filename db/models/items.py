from db.base import Base
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import String, Integer,Float,Date,ARRAY
import datetime
import uuid

class Item(Base):
    __tablename__ = 'items'
    item_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    owner_id: Mapped[int] = mapped_column(Integer, nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    purchase_price: Mapped[float] = mapped_column(Float, nullable=False)
    current_price: Mapped[float] = mapped_column(Float, default=None)
    purchase_date: Mapped[datetime.datetime] = mapped_column(Date, nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    # history_purchase: Mapped[list[int]] = mapped_column(ARRAY(Integer),default=list)