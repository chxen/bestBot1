import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from bot.loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    db.create_table_users()
    name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id, name=name)
    except sqlite3.IntegrityError as err:
        print(err)

    count_users = db.count_users()[0]
    await message.answer(
        "\n".join([
            f'Добро пожаловать в бот расписаний, <b>{message.from_user.full_name}</b>!',
            'Твой аккаунт был занесен в базу данных студентов.',
            f'В базе <b>{count_users}</b> пользователей.\n',
            '\n'
            '<b>Бот знает такие команды:</b>\n'
            'Узнать расписание занятий: /timetable',
            'Отправить боту свою почту: /email',
            'Пройти тест: /test\n'
        ]),
    )
    photo_url = "https://i04.fotocdn.net/s119/3783f5d9a1f160ec/public_pin_m/2726896431.jpg"
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=photo_url)

