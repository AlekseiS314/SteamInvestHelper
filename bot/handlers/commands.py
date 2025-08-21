from telebot import Telebot
def register_commands(bot: Telebot):

    @bot.message_handler(commands=["start"])
    def start_command(message: Message):
        bot.send_message(message.chat.id,"Привет!")