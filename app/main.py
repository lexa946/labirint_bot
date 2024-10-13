from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.config import settings
from app.bot.routers import control, game, tutorial


bot = Bot(settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
dp.include_router(control.router)
dp.include_router(tutorial.router)
dp.include_router(game.router)


async def bot_start():
    await bot.send_message(settings.ADMIN_ID,  'Я запущен🥳.')
    await dp.start_polling(bot)

