from aiogram import Bot, Dispatcher, executor, types
import os
import db
import keaboardin
import keaboardin as kb

from aiogram.types import user

TOKEN = os.environ['token']
# print(TOKEN)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

users = {}


@dp.message_handler(content_types=['contact', 'location'])
async def ph(message: types.Message):
    print('--')
    print(message)


# @dp.message_handler()
# async def echo(message: types.Message):
#     print(message)
#     print(message.from_user.id, ' - ', message.from_user.first_name, ' - ', message.text)
#     user = {
#         'id_telegram': message.from_user.id,
#         'username': message.from_user.username,
#         'name': message.from_user.first_name
#     }
#     if len(db.get_user(message.from_user.id)) == 0:
#         db.add_user(user)
#
#     users.update({message.from_user.id: message.from_user.first_name})
#     # keyboard = kb.keyboard_menu
#     if message.text == 'Новини України та зарубіжжя':
#         keyboard = kb.inline_keyboard()
#     else:
#         keyboard = kb.get_kbrd()
#         keyboard.add(types.KeyboardButton('Новини України та зарубіжжя'))
#
#     await message.answer(message.text, reply_markup=keyboard)
# await message.reply(message.text)

# text = f'Пользователь {message.from_user.first_name} написал {message.text}'
# for i in users.keys():
#     if i != message.from_user.id:
#         await bot.send_message(chat_id=i,
#                                text=text)


@dp.callback_query_handler()
async def call_echo(callback_q: types.CallbackQuery):
    print(callback_q)
    await bot.answer_callback_query(callback_q.id)
    await bot.send_message(chat_id=callback_q.from_user.id, text=callback_q.data)


mood_users = {}
mood = ''
g = ""
n = ''
b = ''


class Mood:
    moods = [
        'mood menu',
        'enter Good',
        'enter Neutral',
        'enter Bad',
    ]
    data = {
        'g': 'G',
        'n': 'N',
        'b': 'B',
    }
    mood = ''

    def __init__(self):
        self.mood = self.moods[0]

    def __str__(self):
        return f'\n{self.data}\n{self.mood}\n'

print(Mood().moods[2])
print(Mood())


@dp.message_handler()
async def mood_meter(message: types.Message):
    chat_id = message.from_user.id
    # global mood, n, b, g
    if mood_users.get(chat_id) is None:
        mood_users.update({chat_id: Mood()})
    if message.text == 'Good':
        mood_users[chat_id].mood = Mood().moods[1]
        text = 'Enter Good'
    elif message.text == 'Neutral':
        mood_users[chat_id].mood = Mood().moods[2]
        text = 'Enter Neutral'
    elif message.text == 'Bad':
        mood_users[chat_id].mood = Mood().moods[3]
        text = 'Enter Bad'
    else:
        if mood_users[chat_id].mood == Mood().moods[1]:
            mood_users[chat_id].data['g'] = message.text
        elif mood_users[chat_id].mood == Mood().moods[2]:
            mood_users[chat_id].data['n'] = message.text
        elif mood_users[chat_id].mood == Mood().moods[3]:
            mood_users[chat_id].data['b'] = message.text
        mood_users[chat_id].mood = Mood().moods[0]
        text = f'{mood_users[chat_id].data["g"]} {mood_users[chat_id].data["n"]} {mood_users[chat_id].data["b"]}'
    await bot.send_message(chat_id, text, reply_markup=kb.moodie())

    print(f'{chat_id}-{message.from_user.username}', mood_users[chat_id])

if __name__ == '__main__':
    executor.start_polling(dp)
