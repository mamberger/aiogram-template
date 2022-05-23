import mysql.connector
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import start_text
from data.connector import connection
from keyboards.default.buttons import markup
from loader import dp, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    writer_id = message.from_user.id
    writer_name = message.from_user.full_name

    await bot.send_photo(chat_id=writer_id, photo='https://ibb.co/R0TXCkH',
                         reply_markup=markup)
    await bot.send_message(chat_id=writer_id, text=start_text)

    conn = connection()
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM users_table WHERE user_id = {writer_id}")
    resault = cursor.fetchone()

    if resault is None:
        cursor.execute(f"INSERT INTO users_table(user_id, user_name, user_level) VALUES('{writer_id}', '{writer_name}', '1')")
        conn.commit()
    else:
        pass
    print(writer_id)
    conn.close()
