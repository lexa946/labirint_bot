from functools import wraps

from aiogram.types import CallbackQuery, Message

from app.dao.main import UserDAO
from app.keyboards.game import ways_keyboard


def check_game_over(func):
    @wraps(func)
    async def wrapper(data: CallbackQuery | Message):

        user = await UserDAO.find_one_or_none(telegram_id=data.from_user.id)

        if user.hero.has_died:
            text = "Твой герой погиб💀\nТебе придется начать новую игру!😔"
            reply_kb = ways_keyboard([])
            if isinstance(data, CallbackQuery):
                await data.message.edit_text(text, reply_markup=reply_kb)
                return
            else:
                await data.answer(text, reply_markup=reply_kb)
                return
        func(data)

    return wrapper
