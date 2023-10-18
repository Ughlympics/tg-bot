from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Подивитися_прайс')
b2 = KeyboardButton('/Оформити_замовлення')


kb_client = ReplyKeyboardMarkup()

kb_client.row(b1, b2)