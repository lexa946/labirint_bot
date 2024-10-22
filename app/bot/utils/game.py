from functools import wraps

from aiogram.types import CallbackQuery, Message

from app.bot.models import User, Hero
from app.dao.main import UserDAO, HeroDAO
from app.keyboards.game import ways_keyboard

def get_user(func):
    @wraps(func)
    async def wrapper(data: CallbackQuery | Message):
        user = await UserDAO.find_one_or_none(telegram_id=data.from_user.id)
        if not user:
            user = await UserDAO.add(telegram_id=data.from_user.id,
                                     first_name=data.from_user.first_name,
                                     username=data.from_user.username,
                                     )
        return await func(data, user)
    return wrapper


def check_game_over(func):
    @wraps(func)
    async def wrapper(data: CallbackQuery | Message, user: User):
        text = "Твой герой погиб💀\nТебе придется начать новую игру!😔"
        reply_kb = ways_keyboard([], user.hero)
        if user.hero.has_died:
            if isinstance(data, CallbackQuery):
                await data.message.edit_text(text, reply_markup=reply_kb)
                return
            else:
                await data.answer(text, reply_markup=reply_kb)
                return
        await func(data, user)
        if not user.hero.current_stamina:
            await HeroDAO.patch(user.hero, has_died=True)

            if isinstance(data, CallbackQuery):
                await data.message.edit_reply_markup(reply_markup=None)
                await data.message.answer(text, reply_markup=reply_kb)

    return wrapper



