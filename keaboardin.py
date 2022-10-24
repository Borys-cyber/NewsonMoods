from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from db import get_users


# btn1 = KeyboardButton('some text')
# btn2 = KeyboardButton('some text2', )
# keyboard_test = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
# keyboard_test.add(btn1, btn2)
# keyboard_test.insert(btn1)
# keyboard_test.add(btn1)
# keyboard_test.row(btn1, btn2, btn1)
# keyboard_test.row(btn1)
# keyboard_test.add(btn1, btn1, btn2)

# menu = ['in Kharkiv', 'in Ukraine', "abroad", "Europe", "interesting"]

# keyboard_menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
# for i in menu:
#     keyboard_menu.insert(i)


def get_kbrd():
    menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    for user in get_users():
        menu.insert(KeyboardButton(user[3]))
    menu.row(
        KeyboardButton('Phone', request_contact=True),
        KeyboardButton('Where are you?', request_location=True))
    return menu


# def inline_keyboard():
#     btn = InlineKeyboardButton(text='Kharkiv news', url='https://www.sq.com.ua/')
#     btn1 = InlineKeyboardButton(text='Abroad ', url='https://www.wsj.com/')
#     btn2 = InlineKeyboardButton(text='Econews', url='https://enovosty.com/')
#     btn3 = InlineKeyboardButton(text='Censor', url='https://censor.net/')
#     btn4 = InlineKeyboardButton(text='5', url='https://www.5.ua/')
#     btn5 = InlineKeyboardButton(text='Article of the day', url='https://www.5.ua/dv/life/268945')
#     btn6 = InlineKeyboardButton(text='Other',
#                                 url='https://www.5.ua/polityka/yak-u-ridnoi-mamy-vdoma-poroshenko-pryviz-u-25-tu-bryhadu-unikalnu-mobilnu-lazniu-290220.html')
#     kbrd = InlineKeyboardMarkup().add(btn, btn1, btn2, btn3, btn4, btn5, btn6)
#     return kbrd


def moodie():
    menu = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    menu.row(
        InlineKeyboardButton(text='Good', url="https://www.youtube.com/watch?v=W_vl0aH8_kg"),
        InlineKeyboardButton(text='Neutral', url="https://www.obozrevatel.com.ua"),
        InlineKeyboardButton(text='Bad', url="https://www.westwild.com.ua/2020/02/Lehkyy-humor.html")
    )
    return menu
#
# def moodie2():
#     menu = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
#     menu.row(
#         # InlineKeyboardButton(text='Good', url="https://www.youtube.com/watch?v=W_vl0aH8_kg"),
#         InlineKeyboardButton(text='Neutral', url="https://www.obozrevatel.com.ua"),
#         # InlineKeyboardButton(text='Bad', url="https://www.westwild.com.ua/2020/02/Lehkyy-humor.html")
#     )
#     return menu
#
# def moodie3():
#     menu = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
#     menu.row(
#         # InlineKeyboardButton(text='Good', url="https://www.youtube.com/watch?v=W_vl0aH8_kg"),
#         # InlineKeyboardButton(text='Neutral', url="https://www.obozrevatel.com.ua"),
#         InlineKeyboardButton(text='Bad', url="https://www.westwild.com.ua/2020/02/Lehkyy-humor.html")
#     )
#     return menu