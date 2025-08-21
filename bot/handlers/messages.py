from telebot import Telebot


def register_messages(bot: Telebot):
    @bot.message_handler(commands=["start"])
    def start_message(message: Message):
        bot.send_message(message.chat.id, "Привет!")