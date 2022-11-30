import telebot
import data_model as dm
import requests
import json
from client_kb import kb_client
from constants import TOKEN

API_URL_WIKI = "https://7012.deeppavlov.ai/model"
API_URL_ARTNEWS = "https://daily.afisha.ru/news/"
API_URL_NUMBERS = "http://numbersapi.com/"

# API_TOKEN = 'Апи ключ, который вы получили у BotFather'
API_TOKEN = TOKEN
bot = telebot.TeleBot(API_TOKEN)

keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row('привет!', 'Hi!')
keyboard.row('see you later')

def send(id, text):
    bot.send_message(id, text, reply_markup=keyboard)


# декоратор
@bot.message_handler(commands=['загрузить_афишу_ноября'])
def load_bill(message):
    dm.load('bill_november.json')
    send(message.chat.id, "Ноябрьская афиша загружена")


@bot.message_handler(commands=['загрузить_афишу_декабря'])
def load_bill(message):
    dm.load('bill_december.json.json')
    send(message.chat.id, "Декабрьская афиша загружена")


@bot.message_handler(commands=['показать_афишу'])
def show_bill(message):
    send(message.chat.id, "Наша афиша: ")
    send(message.chat.id, ", ".join(dm.data_))


@bot.message_handler(commands=['start'])
def start_message(message):
    send(message.chat.id, 'Я в деле')


@bot.message_handler(commands=['wiki'])
def wiki(message):
    quest = message.text.split()[1:]
    # print(message)message
    data = {'question_raw': quest}
    res = requests.post(API_URL_WIKI, json=data, verify=False).json()
    send(message.chat.id, res)


@bot.message_handler(commands=['number'])
def number(message):
    quest = message.text.split()[1:]
    print(quest)
    data = {'text': quest}
    res = requests.get(API_URL_NUMBERS, json=data, verify=False).json()
    send(message.chat.id, res)


@bot.message_handler(regexp='[0-9]+')
def numbers(message):
    # quest = message.text.split()[1:]
    # data = {'text': quest}
    answer = requests.get(f'http://numbersapi.com/{message.text}?json')
    # res = requests.get(f'http://numbersapi.com/{message.text}?json', json=data, verify=False).json()
    # bot.send_message(message.chat.id, res)
    send(message.chat.id, json.loads(answer.text)['text'])


@bot.message_handler(content_types=['text'])
def main(message):
    id = message.chat.id
    msg = message.text

    if msg == 'привет!':
        send(id, 'И тебе привет!')
    elif msg == 'see you later':
        send(id, 'not a while')
    elif msg == 'Hi!':
        send(id, "What's up?")
    else: send(id, 'What are you mind?')

bot.polling()