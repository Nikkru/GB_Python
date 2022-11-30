from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/показать_афишу')
b2 = KeyboardButton('/wiki')

kb_client = ReplyKeyboardMarkup()

kb_client.add(b1).add(b2)


