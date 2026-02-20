import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from aiogram.filters.command import CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder

bot_token = '8038249268:AAHosbt5zuaBC54KFrnjV-LLJ9zkFSMT0IQ'
bot = Bot(token= bot_token)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    kb = [
        [types.KeyboardButton(text='⚡️ Get Fueled')]
        [types.KeyboardButton(text='💎 Drop a Code')]
        [types.KeyboardButton(text='📦 Grab a Pack')]
        [types.KeyboardButton(text='🏆 My Stats')]
        [types.KeyboardButton(text='📍 Find Omega')]
        [types.KeyboardButton(text='❓ The Formula')]
        [types.KeyboardButton(text='🎧 Vibe Check')]
    ]
    await message.answer('Welcome to the Omega Realm, [User Name]! ⚡️ Ready to crush your goals or just need a massive recharge? Pick your fuel below.')

@dp.message()
async def echo(message):
    await message.send_copy(chat_id=message.from_user.id)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        import asyncio
        asyncio.run(main())
    except KeyboardInterrupt:
        pass