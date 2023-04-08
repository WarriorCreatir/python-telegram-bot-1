import openai
import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# инициализация API OpenAI
openai.api_key = os.environ.get('OPENAI_API_KEY')

# инициализация бота
bot = Bot(token=os.environ.get('BOT_TOKEN'))
dp = Dispatcher(bot)

# функция, которая будет вызвана при команде /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Привет! Я телеграмм бот.")

# функция, которая будет вызвана при любом сообщении
@dp.message_handler()
async def echo_message(message: types.Message):
    # получаем ответ от OpenAI API
    response = openai.Completion.create(
        engine="davinci", prompt=message.text, max_tokens=100
    )

    # отправляем ответ от OpenAI API пользователю
    await message.reply(response.choices[0].text)

# функция для запуска бота
def main():
    executor.start_polling(dp, skip_updates=True)

if __name__ == '__main__':
    main()