from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup

def get_series_menu():
    builder = InlineKeyboardBuilder()
    series = {
        "tropical": "🌕 Night City Calling",
        "noir": "🔎 When City Sleeps",
        "thug": "💰 Midnight SWAG",
        "og": "🏅 OG Collection"
    }
    for key, value in series.items():
        builder.button(text=value, callback_data=f"series_{key}")
    builder.adjust(2)
    return builder.as_markup()

def get_drinks_menu(series_type: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    drinks_data = {
        "tropical": {
            "tropical_burst": "🌴 Tropical Burst",
            "electric_berry": "🫐 Electric Berry",
            "cooling_watermelon": "🍉 Cooling Watermelon",
            "neon_mango": "🥭 Neon Mango"
        },
        "noir": {
            "black_coffee": "☕️ Black Coffe",
            "mysterious_blackberry": "💫 Mysterious Blackberry",
            "deep_cherry": "🍒 Deep Cherry",
            "sharp_lemon": "🍋 Sharp Lemon"
        },
        "thug": {
            "bold_grape": "🔥 Bold Grape",
            "gold_citrus": "✨ Gold Citrus",
            "rich_pineapple": "🍍 Rich Pineapple",
            "hustling_lime": "🍋‍🟩 Hustling Lime"
        },
        "og": {
            "miyagoda_rofls": "👑 Miyagoda Rofls",
        }
    }

    current_series_drinks = drinks_data.get(series_type, {})

    for drink_id, drink_name in current_series_drinks.items():
        builder.button(text=drink_name, callback_data=f"drink_{drink_id}")

    builder.button(text="🔙 Back to Series", callback_data="back_to_series")
    builder.adjust(2, 1) 
    return builder.as_markup()