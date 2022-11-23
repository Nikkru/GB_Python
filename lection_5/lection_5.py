from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging
from bot_commands import *


TOKEN = '5725232496:AAFZIIWs1Pd9GJE0CE-pr_iIqnRlbIEnsQY'

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(update, context):
    # `bot.send_message` это метод Telegram API
    # `update.effective_chat.id` - определяем `id` чата,
    # откуда прилетело сообщение
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="I'm a bot, please talk to me!")
# говорим обработчику, если увидишь команду `/start`,
# то вызови функцию `start()`
start_handler = CommandHandler('start', start)
# добавляем этот обработчик в `dispatcher`
# dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('chao', chao_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
print('server start')
# говорим экземпляру `Updater`,
# слушай сервера Telegram.
updater.start_polling()
updater.idle()

