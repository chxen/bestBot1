from bot.loader import bot, db, dp


async def on_startup(dp):
    try:
        db.create_table_users()
    except Exception as e:
        print(e)
    db.delete_users()
    print(db.select_all_users())

if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_shutdown=on_startup)
