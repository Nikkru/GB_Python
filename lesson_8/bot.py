import telebot
from telebot import types
import json
from config import TOKEN

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
key = {}
key[0] = types.KeyboardButton("Показать все контакты")
key[1] = types.KeyboardButton("Найти контакт")
key[2] = types.KeyboardButton("Добавить контакт")
key[3] = types.KeyboardButton("Удалить контакт")
keyboard.row(key[0], key[1])
keyboard.row(key[2], key[3])

# keyboard.row('/show_all', 'Hi!')
# keyboard.row('see you later')

API_TOKEN = TOKEN

bot = telebot.TeleBot(API_TOKEN)

calc = False


def send(id, text):
    bot.send_message(id, text, reply_markup=keyboard)

films = []
phonebook_dict = {}


def save():
    with open("films.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(films, ensure_ascii=False))
    print("Наша фильмотека была успешно сохранена в файле films.json")


def load():
    global films
    with open("phonebook.json", "r", encoding="utf-8") as fh:
        global phonebook_dict
        phonebook_dict = json.load(fh)
    print("Фильмотека была успешно загружена")

def show_name(message):
    global phonebook_dict
    quest = message.text
    bot.send_message(message.chat.id, f'{quest}: {phonebook_dict.get(quest)}')
    if phonebook_dict.get(quest)==None:
        bot.send_message(message.chat.id, 'Такого контакта нет в телефонном справочнике!')


def show_number(message):
    quest = int(message.text)
    key = search_contact(quest)
    bot.send_message(message.chat.id, f'{key}: {quest}')
    if key == None:
        bot.send_message(message.chat.id, 'Такого номера нет в телефонном справочнике!')


def add_new_contact(message):
    global phonebook_dict
    quest = message.text.split()
    if quest == [] or len(quest) < 2:
        bot.send_message(message.chat.id, 'Информация введена не полностью. Попробуйте еще раз!')
    else:
        if len(quest) > 2:
            phonebook_dict[quest[0]] = []
            for i in range(len(quest)):
                if i > 0:
                    phonebook_dict[quest[0]].append(int(quest[i]))
            save()
            bot.send_message(message.chat.id, 'Контакт добавлен в телефонную книгу!')


def del_contact(message):
    global phonebook_dict
    quest = message.text
    del phonebook_dict[quest]
    save()
    bot.send_message(message.chat.id, 'Запись удалена!')


def del_num_contact(message):
    global phonebook_dict
    quest = int(message.text)
    for key, value in phonebook_dict.items():
        for k in value:
            if k == quest:
                phonebook_dict[key].remove(k)
    save()
    bot.send_message(message.chat.id, 'Номер телефона удалён!')


@bot.message_handler(commands=['start'])
def start_message(message):
    send(message.chat.id, "Добро пожаловать в телефонную книгу!")
    try:
        load()
        bot.send_message(message.chat.id, "Информация успешно загружена!")

    except:
        bot.send_message(message.chat.id, "Упс! Телефонная книга пуста!")

@bot.message_handler(func=lambda message: True)
def menu(message):
     if message.text == "Показать все контакты":
         print(phonebook_dict)
         for x, y in phonebook_dict.items():
             bot.send_message(message.chat.id, f'{x}: {y}')
     elif message.text == "Найти контакт":
         markup_1 = types.InlineKeyboardMarkup(row_width=1)
         but1 = types.InlineKeyboardButton("Найти по фамилии", callback_data='text1')
         but2 = types.InlineKeyboardButton("Найти по номеру телефона", callback_data='text2')
         markup_1.add(but1, but2)
         bot.send_message(chat_id=message.chat.id, text="Выбери, каким способом искать:", reply_markup=markup_1)
     elif message.text == "Добавить контакт":
        markup_2 = types.InlineKeyboardMarkup(row_width=1)
        but1 = types.InlineKeyboardButton("Добавить данные", callback_data='new')
        markup_2.add(but1)
        bot.send_message(chat_id=message.chat.id, text="Введите данные нового контакта:", reply_markup=markup_2)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
            if call.data == 'text1':
                msg = bot.send_message(call.message.chat.id, "Введите фамилию: ")
                bot.register_next_step_handler(msg, show_name)
            elif call.data == 'text2':
                msg = bot.send_message(call.message.chat.id, "Введите номер телефона: ")
                bot.register_next_step_handler(msg, show_number)
            elif call.data == 'new':
                msg = bot.send_message(call.message.chat.id, "Укажите фамилию и номера телефонов через пробел!")
                bot.register_next_step_handler(msg, add_new_contact)
            elif call.data == 'del':
                msg = bot.send_message(call.message.chat.id, "Укажите фамилию контакта:")
                bot.register_next_step_handler(msg, del_contact)
            elif call.data == 'del_num':
                msg = bot.send_message(call.message.chat.id, "Укажите номер контакта:")
                bot.register_next_step_handler(msg, del_num_contact)


@bot.message_handler(commands=['show_all'])
def show_message(message):
    print(phonebook_dict)
    for x, y in phonebook_dict.items():
        bot.send_message(message.chat.id, f'{x}: {y}')
    # bot.send_message(message.chat.id, " ".join(phonebook_dict))


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
