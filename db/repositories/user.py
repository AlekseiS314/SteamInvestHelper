from db.models.user import User
# user_id: Mapped[str] = mapped_column(Integer, primary_key=True, autoincrement=True)
# chat_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
class UserRepository:
    def __init__(self, db):
        self._db = db

    def create_user(self,chat_id : int):
        user = User(chat_id)

        self._db.add(user)
        self._db.commit()
        self._db.flesh()

    def delete_user_by_chat_id(self,chat_id: int):
        user = self._db.query(User).filter(User.chat_id == chat_id).first()
        self._db.delete(user)
        self._db.commit()
        self._db.flesh()

    def get_user_id_by_chat_id(self,chat_id: int):
        user = self._db.query(User).filter(User.chat_id == chat_id).first()
        return user.user_id


