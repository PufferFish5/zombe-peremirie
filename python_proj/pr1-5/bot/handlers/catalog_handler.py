from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from bot.states.catalog_state import CatalogStates
from bot.keyboards.reply import get_main_menu, get_cancel_menu
from bot.keyboards.inline import get_series_menu, get_drinks_menu

router = Router()

@router.message(F.text == "⚡️ Get Fueled")
async def catalogue_series(message: types.Message, state: FSMContext):
    await state.set_state(CatalogStates.series_choice)
    await message.answer(
        "Check out our elite lineup. Which vibe are you feeling today?",
        reply_markup=get_series_menu())
    
# @router.message(Command("test"))
# async def catalogue_series(message: types.Message, state: FSMContext):
#     await state.set_state(CatalogStates.series_choice)
#     await message.answer(
#         "Check out our elite lineup. Which vibe are you feeling today?",
#         reply_markup=get_cancel_menu())
    
@router.message(F.text == "🔙 Back to Menu")
async def cancel_handler(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Back to the main hub. What's next, champ?",
        reply_markup=get_main_menu()
    )

@router.callback_query(F.data.startwith("series_"))
async def show_series(callback: types.CallbackQuery):
    series_type = callback.data.split("_")[1]
    series_content = {
        "tropical": {"text": "Welcome to the neon jungle...", "photo": ""},
        "noir": {"text": "Solve the mystery of low energy...", "photo": ""},
        "thug": "",
        "og": ""
    }

    content = series_content.get(series_type)
    await callback.message.edit_media(
        media=types.InputMediaPhoto(
            media=content["photo"],
            caption=content["text"]
        ),
        reply_markup=get_drinks_menu(series_type)
    )
    await callback.answer()

@router.callback_query(F.data == "back_to_series")
async def go_back_to_series(callback: types.CallbackQuery):
    await callback.message.edit_media(
        media=types.InputMediaPhoto(
            media="",
            caption="Pick your vibe again, champ!"
        ),
        reply_markup=get_series_menu()
    )
    await callback.answer()