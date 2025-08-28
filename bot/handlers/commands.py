from telebot import TeleBot
from telebot.types import Message
import os

# file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'texts', 'start.md')

def register_commands(bot: TeleBot):
    @bot.message_handler(commands=["start"])
    def start_command(message):
        start_text = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'texts', 'start.md'),encoding='utf-8').read()
        bot.send_message(message.chat.id,start_text)

    @bot.message_handler(commands=["help"])
    def help_command(message):
        with open('texts/help.md','r',encoding='utf-8') as f:
            help_text = f.read()
        bot.send_message(message.chat.id,help_text)

    @bot.message_handler(commands=["add"])
    def add_command(message):
        with open('texts/add.md','r',encoding='utf-8') as f:
            add_text = f.read()
        bot.send_message(message.chat.id,add_text)

    @bot.message_handler(commands=["remove"])
    def remove_command(message):
        ...

    @bot.message_handler(commands=["sell"])
    def sell_command(message):
        ...

    # @bot.message_handler(commands=["check"])
    # def check_command(message):
    #     ...