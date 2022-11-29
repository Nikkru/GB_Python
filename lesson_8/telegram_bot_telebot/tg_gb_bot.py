import telebot
import bot_commands as bc
import data_model as dm
import requests

API_URL = "https://7012.deeppavlov.ai/model"

API_TOKEN = '5725232496:AAFZIIWs1Pd9GJE0CE-pr_iIqnRlbIEnsQY'
bot = telebot.TeleBot(API_TOKEN)

# декоратор
@bot.message_handler(commands=['загрузить_афишу_ноября'])
def load_bill(message):
    dm.load('bill_november.json')
    bot.send_message(message.chat.id, "Ноябрьская афиша загружена")


@bot.message_handler(commands=['загрузить_афишу_декабря'])
def load_bill(message):
    dm.load('bill_december.json.json')
    bot.send_message(message.chat.id, "Декабрьская афиша загружена")


@bot.message_handler(commands=['показать_афишу'])
def show_bill(message):
    bot.send_message(message.chat.id, "Наша афиша: ")
    bot.send_message(message.chat.id, ", ".join(dm.data_))


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я в деле')


@bot.message_handler(commands=['wiki'])
def wiki(message):
    quest = message.text.split()[1:]
    # print(message)message
    data = {'question_raw': quest}
    res = requests.post(API_URL, json=data, verify=False).json()
    bot.send_message(message.chat.id, res)

bot.polling()