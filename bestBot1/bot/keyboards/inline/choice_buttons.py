from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from bot.keyboards.inline.callback_datas import group_callback

# Клавиатура с выбором группы
choice = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Первая группа", callback_data=group_callback.new(group="first", week_day="none")),
     InlineKeyboardButton(text="Вторая группа", callback_data=group_callback.new(group="second", week_day="none"))],
    [InlineKeyboardButton(text="Третья группа", callback_data=group_callback.new(group="third", week_day="none")),
     InlineKeyboardButton(text="Четвертая группа", callback_data=group_callback.new(group="fourth", week_day="none"))],
    [InlineKeyboardButton(text="Пятая группа", callback_data=group_callback.new(group="fifth", week_day="none")),
     InlineKeyboardButton(text="Шестая группа", callback_data=group_callback.new(group="sixth", week_day="none"))]
])

# Клавиатура с выбором дня недели для первой группы
first_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Понедельник", callback_data=group_callback.new(group="first", week_day="monday")),
     InlineKeyboardButton(text="Вторник", callback_data=group_callback.new(group="first", week_day="tuesday")),
     InlineKeyboardButton(text="Среда", callback_data=group_callback.new(group="first", week_day="wednesday"))],
    [InlineKeyboardButton(text="Четверг", callback_data=group_callback.new(group="first", week_day="thursday")),
     InlineKeyboardButton(text="Пятница", callback_data=group_callback.new(group="first", week_day="friday")),
     InlineKeyboardButton(text="Суббота", callback_data=group_callback.new(group="first", week_day="saturday"))],
    [InlineKeyboardButton(text="Воскресенье", callback_data=group_callback.new(group="first", week_day="sunday"))]
])

# Клавиатура с выбором дня недели для второй группы
second_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Понедельник", callback_data=group_callback.new(group="second", week_day="monday")),
     InlineKeyboardButton(text="Вторник", callback_data=group_callback.new(group="second", week_day="tuesday")),
     InlineKeyboardButton(text="Среда", callback_data=group_callback.new(group="second", week_day="wednesday"))],
    [InlineKeyboardButton(text="Четверг", callback_data=group_callback.new(group="second", week_day="thursday")),
     InlineKeyboardButton(text="Пятница", callback_data=group_callback.new(group="second", week_day="friday")),
     InlineKeyboardButton(text="Суббота", callback_data=group_callback.new(group="second", week_day="saturday"))],
    [InlineKeyboardButton(text="Воскресенье", callback_data=group_callback.new(group="second", week_day="sunday"))]
])

# Клавиатура с выбором дня недели для третьей группы
third_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Понедельник", callback_data=group_callback.new(group="third", week_day="monday")),
     InlineKeyboardButton(text="Вторник", callback_data=group_callback.new(group="third", week_day="tuesday")),
     InlineKeyboardButton(text="Среда", callback_data=group_callback.new(group="third", week_day="wednesday"))],
    [InlineKeyboardButton(text="Четверг", callback_data=group_callback.new(group="third", week_day="thursday")),
     InlineKeyboardButton(text="Пятница", callback_data=group_callback.new(group="third", week_day="friday")),
     InlineKeyboardButton(text="Суббота", callback_data=group_callback.new(group="third", week_day="saturday"))],
    [InlineKeyboardButton(text="Воскресенье", callback_data=group_callback.new(group="third", week_day="sunday"))]
])

# Клавиатура с выбором дня недели для четвертой группы
fourth_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Понедельник", callback_data=group_callback.new(group="fourth", week_day="monday")),
     InlineKeyboardButton(text="Вторник", callback_data=group_callback.new(group="fourth", week_day="tuesday")),
     InlineKeyboardButton(text="Среда", callback_data=group_callback.new(group="fourth", week_day="wednesday"))],
    [InlineKeyboardButton(text="Четверг", callback_data=group_callback.new(group="fourth", week_day="thursday")),
     InlineKeyboardButton(text="Пятница", callback_data=group_callback.new(group="fourth", week_day="friday")),
     InlineKeyboardButton(text="Суббота", callback_data=group_callback.new(group="fourth", week_day="saturday"))],
    [InlineKeyboardButton(text="Воскресенье", callback_data=group_callback.new(group="fourth", week_day="sunday"))]
])

# Клавиатура с выбором дня недели для пятой группы
fifth_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Понедельник", callback_data=group_callback.new(group="fifth", week_day="monday")),
     InlineKeyboardButton(text="Вторник", callback_data=group_callback.new(group="fifth", week_day="tuesday")),
     InlineKeyboardButton(text="Среда", callback_data=group_callback.new(group="fifth", week_day="wednesday"))],
    [InlineKeyboardButton(text="Четверг", callback_data=group_callback.new(group="fifth", week_day="thursday")),
     InlineKeyboardButton(text="Пятница", callback_data=group_callback.new(group="fifth", week_day="friday")),
     InlineKeyboardButton(text="Суббота", callback_data=group_callback.new(group="fifth", week_day="saturday"))],
    [InlineKeyboardButton(text="Воскресенье", callback_data=group_callback.new(group="fifth", week_day="sunday"))]
])

# Клавиатура с выбором дня недели для шестой группы
sixth_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Понедельник", callback_data=group_callback.new(group="sixth", week_day="monday")),
     InlineKeyboardButton(text="Вторник", callback_data=group_callback.new(group="sixth", week_day="tuesday")),
     InlineKeyboardButton(text="Среда", callback_data=group_callback.new(group="sixth", week_day="wednesday"))],
    [InlineKeyboardButton(text="Четверг", callback_data=group_callback.new(group="sixth", week_day="thursday")),
     InlineKeyboardButton(text="Пятница", callback_data=group_callback.new(group="sixth", week_day="friday")),
     InlineKeyboardButton(text="Суббота", callback_data=group_callback.new(group="sixth", week_day="saturday"))],
    [InlineKeyboardButton(text="Воскресенье", callback_data=group_callback.new(group="sixth", week_day="sunday"))]
])
