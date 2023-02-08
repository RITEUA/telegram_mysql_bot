from aiogram import Bot, Dispatcher, executor, types
import logging
from select_data import get_data

TOKEN = "ТОКЕН ВАШОГО БОТА"  # СКОПІЮЙТЕ ЙОГО У @BotFather
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def starting(message: types.Message):
    # Перше, що буде надіслано користувачу, після натиску кнопки start, або команди /start
    await message.answer("Надішли команду /get, для перегляду столиць країн")


@dp.message_handler(commands="get")
async def starting(message: types.Message):
    """ Надсилає повідомлення, у якому містяться країни: столиці,
        отримані з файлу select_data_from_mysql_table.py """
    await message.answer(get_data())


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
