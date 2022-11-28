import telebot
import json

API_TOKEN = 'ваш токен надо сюда вставить'

bot = telebot.TeleBot(API_TOKEN)

calc = False

films = []


def save():
    with open("films.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(films, ensure_ascii=False))
    print("Наша фильмотека была успешно сохранена в файле films.json")


def load():
    global films
    with open("films.json", "r", encoding="utf-8") as fh:
        films = json.load(fh)
    print("Фильмотека была успешно загружена")


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Готов к работе!")
    try:
        load()
        bot.send_message(message.chat.id, "Фильмотека была успешно загружена!")

    except:
        films.append("Матрица")
        films.append("Солярис")
        films.append("Властелин колец")
        films.append("Техасская резня бензопилой")
        films.append("Санта Барбара")
        bot.send_message(message.chat.id, "Фильмотека была загружена по умолчанию!")


@bot.message_handler(commands=['show'])
def show_message(message):
    bot.send_message(message.chat.id, " ".join(films))


@bot.message_handler(commands=['calc'])
def calc_message(message):
    global calc
    # eq = message.text.split()[1:]   #список из одного элемента
    # print(eq)
    calc = True
    bot.send_message(message.chat.id, "А теперь введите выражение")


@bot.message_handler(content_types='text')
def message_reply(message):
    global calc
    if 'привет' in message.text:
        bot.send_message(message.chat.id, 'и тебе привет')
    if calc:
        bot.send_message(message.chat.id, eval(message.text))
        calc = False


bot.polling()
