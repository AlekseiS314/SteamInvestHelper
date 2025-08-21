from db.base import Base
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import String, Integer, UUID, DATETIME,Float
import datetime
import uuid

class Item(Base):
    __tablename__ = 'items'
    item_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(50),nullable=False)
    purchase_price: Mapped[float] = mapped_column(Float,nullable=False)
    current_price: Mapped[float] = mapped_column(Float,default=None)
    purchase_date: Mapped[datetime.datetime] = mapped_column(DATETIME,nullable=False)
    quantity: Mapped[int] = mapped_column(Integer,nullable=False)