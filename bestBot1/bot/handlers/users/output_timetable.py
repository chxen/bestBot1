import logging
from os import sep

from aiogram.types import Message, CallbackQuery
from aiogram.utils.markdown import hbold

from bot.keyboards.inline.callback_datas import group_callback
from bot.loader import dp, bot
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

CREDENTIALS_FILE = "C:\\Users\\Zver\\PycharmProject\\bestBot1\\bot\\handlers\\users\\creeds.json"
spreadsheet_id = '1VV22ct7O_NBqAAwMor2WMoV0Z6Xil-ER8QKd_B-_1DI'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

'''
values = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range='A1:A1',
    majorDimension='ROWS'
).execute()
print(values)

values = service.spreadsheets().values().batchUpdate(
    spreadsheetId=spreadsheet_id,
    body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "B3:C4",
             "majorDimension": "ROWS",
             "values": [["This is B3", "This is C3"], ["This is B4", "This is C4"]]},
            {"range": "D5:E6",
             "majorDimension": "COLUMNS",
             "values": [["This is D5", "This is D6"], ["This is E5", "=5+5"]]}
        ]
    }
).execute()
'''


#  Для первой группы, понедельник
@dp.callback_query_handler(group_callback.filter(group="first", week_day="monday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B3:B9',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание для первой группы в понедельник:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для первой группы, вторник
@dp.callback_query_handler(group_callback.filter(group="first", week_day="tuesday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='C3:C9',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание для первой группы во вторник:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для первой группы, среда
@dp.callback_query_handler(group_callback.filter(group="first", week_day="wednesday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='D3:D9',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание для первой группы в среду:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для первой группы, четверг
@dp.callback_query_handler(group_callback.filter(group="first", week_day="thursday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='E3:E9',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание для первой группы в четверг:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для первой группы, пятница
@dp.callback_query_handler(group_callback.filter(group="first", week_day="friday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='F3:F9',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание для первой группы в пятницу:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для первой группы, суббота
@dp.callback_query_handler(group_callback.filter(group="first", week_day="saturday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='G3:G9',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание для первой группы в субботу:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для первой группы, воскресенье
@dp.callback_query_handler(group_callback.filter(group="first", week_day="sunday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='H3:H9',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание для первой группы в воскресенье:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для второй группы, понедельник
@dp.callback_query_handler(group_callback.filter(group="second", week_day="monday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B13:B19',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание для второй группы в понедельник:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для второй группы, вторник
@dp.callback_query_handler(group_callback.filter(group="second", week_day="tuesday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='C13:C19',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание для второй группы во вторник:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для второй группы, среда
@dp.callback_query_handler(group_callback.filter(group="second", week_day="wednesday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='D13:D19',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание для второй группы в среду:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для второй группы, четверг
@dp.callback_query_handler(group_callback.filter(group="second", week_day="thursday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='E13:E19',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание для второй группы в четверг:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для второй группы, пятница
@dp.callback_query_handler(group_callback.filter(group="second", week_day="friday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='F13:F19',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание для второй группы в пятницу:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для второй группы, суббота
@dp.callback_query_handler(group_callback.filter(group="second", week_day="saturday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='G13:G19',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание для второй группы в субботу:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для второй группы, воскресенье
@dp.callback_query_handler(group_callback.filter(group="second", week_day="sunday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='H13:H19',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание для второй группы в воскресенье:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для третьей группы, понедельник
@dp.callback_query_handler(group_callback.filter(group="third", week_day="monday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B23:B29',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание для третьей группы в понедельник:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для третьей группы, вторник
@dp.callback_query_handler(group_callback.filter(group="third", week_day="tuesday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='C23:C29',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание для третьей группы во вторник:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для третьей группы, среда
@dp.callback_query_handler(group_callback.filter(group="third", week_day="wednesday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='D23:D29',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание для третьей группы в среду:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для третьей группы, четверг
@dp.callback_query_handler(group_callback.filter(group="third", week_day="thursday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='E23:E29',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание для третьей группы в четверг:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для третьей группы, пятница
@dp.callback_query_handler(group_callback.filter(group="third", week_day="friday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='F23:F29',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание для третьей группы в пятницу:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для третьей группы, суббота
@dp.callback_query_handler(group_callback.filter(group="third", week_day="saturday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='G23:G29',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание для третьей группы в субботу:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для третьей группы, воскресенье
@dp.callback_query_handler(group_callback.filter(group="third", week_day="sunday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='H23:H29',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание для третьей группы в воскресенье:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для четвертой группы, понедельник
@dp.callback_query_handler(group_callback.filter(group="fourth", week_day="monday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B33:B39',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание для четвертой группы в понедельник:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для четвертой группы, вторник
@dp.callback_query_handler(group_callback.filter(group="fourth", week_day="tuesday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='С33:С39',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание для четвертой группы во вторник:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для четвертой группы, среда
@dp.callback_query_handler(group_callback.filter(group="fourth", week_day="wednesday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='D33:D39',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание для четвертой группы в среду:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для четвертой группы, четверг
@dp.callback_query_handler(group_callback.filter(group="fourth", week_day="thursday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='E33:E39',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание для четвертой группы в четверг:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для четвертой группы, пятница
@dp.callback_query_handler(group_callback.filter(group="fourth", week_day="friday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='F33:F39',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание для четвертой группы в пятницу:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для четвертой группы, суббота
@dp.callback_query_handler(group_callback.filter(group="fourth", week_day="saturday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='G33:G39',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание для четвертой группы в субботу:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для четвертой группы, воскресенье
@dp.callback_query_handler(group_callback.filter(group="fourth", week_day="sunday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='H33:H39',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание для четвертой группы в воскресенье:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для пятой группы, понедельник
@dp.callback_query_handler(group_callback.filter(group="fifth", week_day="monday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B43:B49',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание пятой группы в понедельник:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для пятой группы, вторник
@dp.callback_query_handler(group_callback.filter(group="fifth", week_day="tuesday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='C43:C49',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание пятой группы во вторник:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для пятой группы, среда
@dp.callback_query_handler(group_callback.filter(group="fifth", week_day="wednesday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='D43:D49',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание пятой группы в среду:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для пятой группы, четверг
@dp.callback_query_handler(group_callback.filter(group="fifth", week_day="thursday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='E43:E49',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание пятой группы в четверг:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для пятой группы, пятница
@dp.callback_query_handler(group_callback.filter(group="fifth", week_day="friday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='F43:F49',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание пятой группы в пятницу:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для пятой группы, суббота
@dp.callback_query_handler(group_callback.filter(group="fifth", week_day="saturday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='G43:G49',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание пятой группы в субботу:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для пятой группы, воскресенье
@dp.callback_query_handler(group_callback.filter(group="fifth", week_day="sunday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='H43:H49',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание пятой группы в воскресенье:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для шестой группы, понедельник
@dp.callback_query_handler(group_callback.filter(group="sixth", week_day="monday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B53:B59',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание шестой группы в понедельник:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для шестой группы, вторник
@dp.callback_query_handler(group_callback.filter(group="sixth", week_day="tuesday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='C53:C59',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание шестой группы во вторник:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для шестой группы, среда
@dp.callback_query_handler(group_callback.filter(group="sixth", week_day="wednesday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='D53:D59',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание шестой группы в среду:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для шестой группы, четверг
@dp.callback_query_handler(group_callback.filter(group="sixth", week_day="thursday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='E53:E59',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание шестой группы в четверг:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для шестой группы, пятница
@dp.callback_query_handler(group_callback.filter(group="sixth", week_day="friday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='F53:F59',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание шестой группы в пятницу:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для шестой группы, суббота
@dp.callback_query_handler(group_callback.filter(group="sixth", week_day="saturday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='G53:G59',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание шестой группы в субботу:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )


#  Для шестой группы, воскресенье
@dp.callback_query_handler(group_callback.filter(group="sixth", week_day="sunday"))
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    otvet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='H53:H59',
        majorDimension='ROWS'
    ).execute()
    logging.info(f"{callback_data=}")
    await call.message.answer(hbold("Расписание шестой группы в воскресенье:\n") +
                              f"09:30 - 10:50 {otvet['values'][0][0]}\n" +
                              f"11:10 - 12:30 {otvet['values'][1][0]}\n" +
                              f"13:00 - 14:20 {otvet['values'][2][0]}\n" +
                              f"14:40 - 16:00 {otvet['values'][3][0]}\n" +
                              f"16:20 - 17:40 {otvet['values'][4][0]}\n" +
                              f"18:10 - 19: 30 {otvet['values'][5][0]}\n" +
                              f"19:40 - 21:00 {otvet['values'][6][0]}"
                              )
