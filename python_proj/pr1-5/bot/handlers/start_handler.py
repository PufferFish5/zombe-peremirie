from aiogram import Router, types
from aiogram.filters import CommandStart
from bot.keyboards.reply import get_main_menu

router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        f"Welcome to the Omega Realm, {message.from_user.first_name}! ⚡️\n"
        "Ready to crush your goals?",
        reply_markup=get_main_menu()
    )