import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from bot.config import config
from bot.handlers import start_handler
from bot.handlers import promo_handler
from bot.handlers import catalog_handler

async def main():
    logging.basicConfig(level=logging.DEBUG)

    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher()

    dp.include_router(start_handler.router)
    dp.include_router(promo_handler.router)
    dp.include_router(catalog_handler.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    try:
        import asyncio
        asyncio.run(main())
    except KeyboardInterrupt:
        pass