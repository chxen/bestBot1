import logging
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.utils.markdown import hbold, hlink
from bot.keyboards.inline.callback_datas import group_callback
from bot.keyboards.inline.choice_buttons import choice, first_keyboard, second_keyboard, third_keyboard, \
    fourth_keyboard, fifth_keyboard, sixth_keyboard
from bot.loader import dp, bot


# Вывод клавиатуры с выбором группы
@dp.message_handler(Command("timetable"))
async def show_items(message: Message):
    await message.answer(text=hbold("Пожалуйста, выберите свою группу.\n")
                              + "Таблица с расписанием доступна по " + hlink("ссылке",
                                                                             "https://docs.google.com/spreadsheets/d/1VV22ct7O_NBqAAwMor2WMoV0Z6Xil-ER8QKd_B-_1DI"
                                                                             "/edit#gid=1481080409"),
                         disable_web_page_preview=True,
                         reply_markup=choice)


# Вывод клавиатуры с выбором дня недели для первой группы
@dp.callback_query_handler(group_callback.filter(group="first", week_day="none"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer("Вы выбрали 1 группу. Какой сегодня день недели?",
                              reply_markup=first_keyboard)


# Вывод клавиатуры с выбором дня недели для второй группы
@dp.callback_query_handler(group_callback.filter(group="second", week_day="none"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer("Вы выбрали 2 группу. Какой сегодня день недели?",
                              reply_markup=second_keyboard)


# Вывод клавиатуры с выбором дня недели для третьей группы
@dp.callback_query_handler(group_callback.filter(group="third", week_day="none"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Вы выбрали 3 группу. Какой сегодня день недели?", reply_markup=third_keyboard)


# Вывод клавиатуры с выбором дня недели для четвертой группы
@dp.callback_query_handler(group_callback.filter(group="fourth", week_day="none"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Вы выбрали 4 группу. Какой сегодня день недели?", reply_markup=fourth_keyboard)


# Вывод клавиатуры с выбором дня недели для пятой группы
@dp.callback_query_handler(group_callback.filter(group="fifth", week_day="none"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Вы выбрали 5 группу. Какой сегодня день недели?", reply_markup=fifth_keyboard)


# Вывод клавиатуры с выбором дня недели для шестой группы
@dp.callback_query_handler(group_callback.filter(group="sixth", week_day="none"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Вы выбрали 6 группу. Какой сегодня день недели?", reply_markup=sixth_keyboard)
