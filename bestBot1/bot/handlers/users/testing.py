from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from bot.loader import dp
from aiogram import types

from bot.states import Test


@dp.message_handler(Command("test"))
async def enter_test(message: types.Message):
    await message.answer("Вы начали тестирование.\n"
                         "Вопрос №1. \n\n"
                         "С помощью какой библиотеки был создан этот бот?")
    await Test.Q1.set()


@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer=answer)
    await message.answer("Вопрос №2\n"
                         "С каких слов начинается ассинхранная функция?")
    await Test.Q2.set()


@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get("answer")
    answer2 = message.text

    await message.answer("Спасибо за ваши ответы.")
    await message.answer(f"Ответ 1: {answer1}")
    await message.answer(f"Ответ 2: {answer2}")

    await state.finish()