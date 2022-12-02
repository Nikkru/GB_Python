import telebot
from telebot import types
import json
from config import TOKEN

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
key = {0: types.KeyboardButton("Показать все контакты"),
       1: types.KeyboardButton("Найти контакт"),
       2: types.KeyboardButton("Добавить контакт"),
       3: types.KeyboardButton("Удалить контакт")}
keyboard.row(key[0], key[1])
keyboard.row(key[2], key[3])

API_TOKEN = TOKEN

bot = telebot.TeleBot(API_TOKEN)
phonebook_dict = {}
db_is_loaded = False


def send(id_, text):
    bot.send_message(id_, text, reply_markup=keyboard)


def save():
    global phonebook_dict
    global db_is_loaded
    if db_is_loaded:
        with open("phonebook.json", "w", encoding="utf-8") as fh:
            fh.write(json.dumps(phonebook_dict, ensure_ascii=False))
        print("Файл phonebook.json обновлен.")
    else:
        temp_dict_without_bd = {}
        temp_dict_without_bd.update(phonebook_dict)
        with open("phonebook.json", "r", encoding="utf-8") as fh:
            temp_dict = json.load(fh)
        phonebook_dict.update(temp_dict)
        with open("phonebook.json", "w", encoding="utf-8") as fh:
            fh.write(json.dumps(phonebook_dict, ensure_ascii=False))
        print("Файл phonebook.json обновлен.")
        print(phonebook_dict)
        phonebook_dict = temp_dict_without_bd
        print(phonebook_dict)


def load():
    global phonebook_dict
    global db_is_loaded
    with open("phonebook.json", "r", encoding="utf-8") as fh:
        dict_temp = json.load(fh)
    phonebook_dict.update(dict_temp)
    db_is_loaded = True


def search_contact(phone_num: int):
    global phonebook_dict
    with open("book.json", "r", encoding="utf-8") as fh:
        for key, value in phonebook_dict.items():
            for k in value:
                if k == phone_num:
                    return key


def show_name(message):
    global phonebook_dict
    quest = message.text
    bot.send_message(message.chat.id, f'{quest}: {phonebook_dict.get(quest)}')
    if phonebook_dict.get(quest) == None:
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
    print(quest)
    if quest == [] or len(quest) < 2:
        bot.send_message(message.chat.id, 'Информация введена не полностью. Попробуйте еще раз!')
    else:
        if len(quest) > 1:
            phonebook_dict[quest[0]] = []
            for i in range(len(quest)):
                if i > 0:
                    phonebook_dict.update({quest[0]: int(quest[i])})
                    print(phonebook_dict)
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
        keys_phonebook = sorted(phonebook_dict)
        print(keys_phonebook)
        for x in keys_phonebook:
            bot.send_message(message.chat.id, f'{x}: {phonebook_dict[x]}')
    elif message.text == "Найти контакт":
        markup_1 = types.InlineKeyboardMarkup(row_width=1)
        but1 = types.InlineKeyboardButton("Найти по фамилии", callback_data='text1')
        but2 = types.InlineKeyboardButton("Найти по номеру телефона", callback_data='text2')
        markup_1.add(but1, but2)
        bot.send_message(chat_id=message.chat.id,
                         text="Выбери, каким способом искать:",
                         reply_markup=markup_1)
    elif message.text == "Добавить контакт":
        markup_2 = types.InlineKeyboardMarkup(row_width=1)
        but1 = types.InlineKeyboardButton("Добавить данные", callback_data='new')
        markup_2.add(but1)
        bot.send_message(chat_id=message.chat.id,
                         text="Введите данные нового контакта:",
                         reply_markup=markup_2)
    elif message.text == "Удалить контакт":
        markup_3 = types.InlineKeyboardMarkup(row_width=1)
        but1 = types.InlineKeyboardButton("Удалить все данные контакта", callback_data='del')
        but2 = types.InlineKeyboardButton("Удалить номер телефона контакта", callback_data='del_num')
        markup_3.add(but1, but2)
        bot.send_message(chat_id=message.chat.id,
                         text="Выберите какие данные нужно удалить:",
                         reply_markup=markup_3)


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

def get_key(dictonary_):
    keys = sorted(dictonary_)
    n = 0
    print('\n')
    for key in keys:
        n += 1
        print(f'{n}. {key}')


@bot.message_handler(commands=['show_all'])
def show_message(message):
    print(phonebook_dict)
    keys_phonebook = sorted(phonebook_dict)
    print(keys_phonebook)
    for x in keys_phonebook:
        bot.send_message(message.chat.id, f'{x}: {phonebook_dict[x]}')


bot.polling()
