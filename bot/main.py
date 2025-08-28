import telebot
from bot.config import settings
from bot.handlers import commands, messages

bot = telebot.TeleBot(settings.BOT_TOKEN)

commands.register_commands(bot)
messages.register_messages(bot)

if __name__ == '__main__':
    bot.infinity_polling()
