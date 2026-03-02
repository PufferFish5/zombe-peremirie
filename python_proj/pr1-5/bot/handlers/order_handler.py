from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from bot.states.order_state import OrderStates
from bot.keyboards.reply import get_main_menu, get_cancel_menu, get_phone_keyboard

router = Router()

@router.message(OrderStates.waiting_for_name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(OrderStates.waiting_for_phone)
    await message.answer("Got it! Now, please share your phone number so we can confirm the delivery.", reply_markup=get_phone_keyboard())

@router.message(OrderStates.waiting_for_phone)
async def process_phone(message: types.Message, state: FSMContext):
    if message.contact:
        phone = message.contact.phone_number
    else:
        phone = message.text
        if not phone.replace('+', '').isdigit():
            await message.answer("That doesn't look like a phone number. Please try again or use the button!")
            return
    await state.update_data(phone=phone)
    await state.set_state(OrderStates.waiting_for_address)
    
    await message.answer(
        "Perfect. Now, where should we ship your fuel? (City and Post Office)",
        reply_markup=types.ReplyKeyboardRemove() 
    )
@router.message(OrderStates.waiting_for_address)
async def process_address(message: types.Message, state: FSMContext):
    await state.update_data(address=message.text)
    data = await state.get_data()
    summary = (
        "📊 **Order Summary:**\n\n"
        f"🥤 Drink ID: {data['chosen_drink_id']}\n"
        f"👤 Name: {data['name']}\n"
        f"📞 Phone: {data['phone']}\n"
        f"📍 Shipping: {data['address']}\n\n"
        "Everything correct? Type **'Confirm'** to finish."
    )
    
    await state.set_state(OrderStates.confirm_order)
    await message.answer(summary, parse_mode="Markdown")

@router.message(OrderStates.confirm_order, F.text.casefold() == "confirm")
async def finish_order(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Mission accomplished! 🚀 Your Omega Energy is on the way.\n"
        "We'll contact you shortly for payment.",
        reply_markup=get_main_menu()
    )