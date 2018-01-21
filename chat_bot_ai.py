from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from bot_settings import BOT_TOKEN


updater = Updater(token=BOT_TOKEN) # place your token here
dispatcher = updater.dispatcher


# realise a behavior
def start_command(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Hello! Lets speak!')


def text_message(bot, update):
    response = "Received message" + update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=response)


# register behavior
start_command_handler = CommandHandler('start', start_command)
text_message_handler = MessageHandler(Filters.text, text_message)
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)

# startup the bot
updater.start_polling(clean=True)
updater.idle()