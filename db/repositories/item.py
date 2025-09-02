from db.models.items import Item
# item_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
# owner_id: Mapped[int] = mapped_column(Integer, nullable=False)
# name: Mapped[str] = mapped_column(String(100), nullable=False)
# purchase_price: Mapped[float] = mapped_column(Float, nullable=False)
# current_price: Mapped[float] = mapped_column(Float, default=None)
# purchase_date: Mapped[datetime.datetime] = mapped_column(Date, nullable=False)
# quantity: Mapped[int] = mapped_column(Integer, nullable=False)
# history_purchase: Mapped[list[int]] = mapped_column(ARRAY(Integer),default=list)
class ItemRepository:
    def __init__(self, db):
        self._db = db

    def add_item(self, owner_id, name, purchase_price, current_price, purchase_date, quantity):
        item = Item(
            owner_id=owner_id,
            name=name,
            purchase_price=purchase_price,
            current_price=current_price,
            purchase_date=purchase_date,
            quantity=quantity,
            # history_purchase
        )

        self._db.add(item)
        print(item.item_id)
        self._db.commit()
        print(item.item_id)
        self._db.flush()
        print(item.item_id)

        return item

    def get_item_by_item_id(self,item_id : int):
        item = self._db.query(Item).filter(Item.item_id == item_id).first()

        return item

    def get_all_item_by_owner_id(self,owner_id : int):
        item = self._db.query(Item).filter(Item.owner_id == owner_id).all()

        return item

    def patch_current_price_by_item_id(
            self,
            item_id : int,
            current_price: float | None = None
    ):
        item = self._db.query(Item).filter(Item.item_id == item_id).first()

        if current_price:
            item.current_price = current_price
            item.history_purchase += current_price

        self._db.commit()
        self._db.flush()

    def delete_item_by_item_id(self, item_id : int):
        item = self._db.query(Item).filter(Item.item_id == item_id).first()

        self._db.delete(item)
        self._db.commit()
        self._db.flush()