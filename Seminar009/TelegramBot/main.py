from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ContextTypes
from telegram import Update
import logging
TOKEN = '5640178135:AAHr3PBZzgGDAIpAQ1o49ay9pHF7cP-X1z8'
# получаем экземпляр `Updater`
updater = Updater(token=TOKEN, use_context=True)
# получаем экземпляр `Dispatcher`
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(update, context):
    # `bot.send_message` это метод Telegram API
    # `update.effective_chat.id` - определяем `id` чата,
    # откуда прилетело сообщение
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Привет! Я бот. Рад знакомству.")


def help(update, context):
    # `bot.send_message` это метод Telegram API
    # `update.effective_chat.id` - определяем `id` чата,
    # откуда прилетело сообщение
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Здесь будут инструкции по командам, которые я умею выполнять")


start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', help)
# добавляем этот обработчик в `dispatcher`
dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)


def echo(update, context):
    # добавим в начало полученного сообщения строку 'ECHO: '
    if update.message.text == 'Привет':
        text = 'ECHO: ' + update.message.text
    else:
        text = 'Культурные люди сначала здороваются'
    # `update.effective_chat.id` - определяем `id` чата,
    # откуда прилетело сообщение
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=text)


updater.start_polling()

# импортируем обработчик `MessageHandler` и класс с фильтрами
# говорим обработчику `MessageHandler`, если увидишь текстовое
# сообщение (фильтр `Filters.text`)  и это будет не команда
# (фильтр ~Filters.command), то вызови функцию `echo()`
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
# регистрируем обработчик `echo_handler` в экземпляре `dispatcher`
dispatcher.add_handler(echo_handler)
