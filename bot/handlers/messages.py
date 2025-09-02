from telebot import TeleBot
from telebot.types import Message
from db.repositories.item import ItemRepository
from db.repositories.user import UserRepository
from db.session import get_db
from datetime import datetime

def register_messages(bot: TeleBot):
    @bot.message_handler(func=lambda message : "Добавить" in message.text)
    def add_message(message):
        #  добавить:
#          {название}:{количество}:{цена}
#          {название}:{количество}:{цена}
#          ... 13.12000000000000000000000000001
        with get_db() as db:
            user_repo = UserRepository(db)
            string = message.text.lower()
            item_data_list = string.split('\n')[1:]  # ['название:кол-во:цена','название:кол-во:цена', ...]

            for item_data in item_data_list:
                item_data = item_data.split(':')
                name = item_data[0]
                count = int(item_data[1])
                price = round(float(item_data[2]),2)
                item_repo = ItemRepository(db)

                user = user_repo.get_user(message.chat.id)
                if not user:
                    user_repo.create_user(message.chat.id)
                user_id = user_repo.get_user_id_by_chat_id(message.chat.id)
                print(user_id,name,price,price,datetime.today().date(),count)
                item = item_repo.add_item(
                    user_id,
                    name,
                    price,
                    price,
                    datetime.today().date(),
                    count
                )




# name: Mapped[str] = mapped_column(String(100), nullable=False)
#     purchase_price: Mapped[float] = mapped_column(Float, nullable=False)
#     current_price: Mapped[float] = mapped_column(Float, default=None)
#     purchase_date: Mapped[datetime.datetime] = mapped_column(Date, nullable=False)
#     quantity: Mapped[int] = mapped_column(Integer, nullable=False)
#     history_purchase: Mapped[list[int]] = mapped_column(ARRAY(Integer),default=list)
