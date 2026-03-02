from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.types import FSInputFile
from bot.states.catalog_state import CatalogStates
from bot.states.order_state import OrderStates
from bot.keyboards.reply import get_main_menu, get_cancel_menu
from bot.keyboards.inline import get_series_menu, get_drinks_menu
import bot.databases.requests as rq
router = Router()

@router.message(F.text == "⚡️ Get Fueled")
async def catalogue_series(message: types.Message, state: FSMContext):
    await state.set_state(CatalogStates.series_choice)
    await message.answer_photo(
        photo=FSInputFile("bot/media/news1.jpg"),
        caption="Check out our elite lineup. Which vibe are you feeling today?",
        reply_markup=get_series_menu())
    
# @router.message(Command("test"))
# async def catalogue_series(message: types.Message, state: FSMContext):
#     await state.set_state(CatalogStates.series_choice)
#     await message.answer(
#         "Check out our elite lineup. Which vibe are you feeling today?",
#         reply_markup=get_cancel_menu())
    
# @router.message(F.text == "🔙 Back to Menu")
# async def cancel_handler(message: types.Message, state: FSMContext):
#     await state.clear()
#     await message.answer(
#         "Back to the main hub. What's next, champ?",
#         reply_markup=get_main_menu()
#     )

@router.callback_query(F.data.startswith("series_"))
async def show_series(callback: types.CallbackQuery):
    series_type = callback.data.split("_")[1]
    drinks = await rq.get_drinks_by_series(series_type)
    series_content = {
        "tropical": {"text": "Neon lights and retro vibes", "photo": "bot/media/series1_back_text.png"},
        "noir": {"text": "Classic taste for deep thinkers.", "photo": "bot/media/series2_back_text.png"},
        "thug": {"text": "Powerful punch for the bold.", "photo": "bot/media/series3_back_text.png"},
        "og": {"text": "Where it all started.", "photo": "bot/media/ex_drink1_render.png"}
    }

    content = series_content.get(series_type)
    await callback.message.edit_media(
        media=types.InputMediaPhoto(
            media=FSInputFile(content["photo"]),
            caption=content["text"]
        ),
        reply_markup=get_drinks_menu(drinks)
    )
    await callback.answer()

@router.callback_query(F.data.startswith("drink_"))
async def start_order(callback: types.CallbackQuery, state: FSMContext):
    drink_id = callback.data.split("_")[1]
    
    await state.update_data(chosen_drink_id=drink_id)
    await state.set_state(OrderStates.waiting_for_name)
    
    await callback.message.answer(
        "⚡️ Great choice! Let's get your fuel ready.\n"
        "First, **what's your name?**",
        reply_markup=get_cancel_menu(),
        parse_mode="Markdown"
    )
    await callback.answer()

@router.callback_query(F.data == "back_to_series")
async def go_back_to_series(callback: types.CallbackQuery):
    await callback.message.edit_media(
        media=types.InputMediaPhoto(
            media=FSInputFile("bot/media/news1.jpg"),
            caption="Pick your vibe again, champ!"
        ),
        reply_markup=get_series_menu()
    )
    await callback.answer()
#ZAPUSK NA POTOM DLYA ID
@router.message(F.photo)
async def get_photo_file_id(message: types.Message):
    photo_id = message.photo[-1].file_id
    await message.reply(photo_id, parse_mode="HTML")