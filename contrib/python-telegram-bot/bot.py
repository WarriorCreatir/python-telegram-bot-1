import telegram
from telegram.ext import Updater, CommandHandler

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я бот")

updater = Updater(token='6189637119:AAFQ-aByjvgEKM7uass1oo629-dMIPS6WRA', use_context=True)
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()