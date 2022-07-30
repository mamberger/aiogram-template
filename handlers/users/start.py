from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://jtele2.ru/wp-content/uploads/2019/03/tele2.jpg')
