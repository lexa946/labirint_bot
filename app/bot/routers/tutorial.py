from aiogram import Router, F
from aiogram.types import CallbackQuery

from app.bot.models import User
from app.bot.models.hero import PotionEnum
from app.bot.utils.game import get_user
from app.dao.main import UserDAO, WayDAO, HeroDAO

from app.bot.texts.tutorial import epigraph, potion_choice
from app.keyboards.game import ways_keyboard
from app.keyboards.tutorial import epigraph_keyboard, potion_choice_keyboard

router = Router()


@router.callback_query(F.data == "new_game")
async def call_new_game(callback: CallbackQuery) -> None:
    await callback.message.edit_text(
        text=epigraph, reply_markup=epigraph_keyboard()
    )


@router.callback_query(F.data == "potion_choice")
async def call_potion_choice(callback: CallbackQuery) -> None:
    await callback.message.edit_text(text=potion_choice, reply_markup=potion_choice_keyboard())


@router.callback_query(F.data.in_(("potion_skill", "potion_stamina", "potion_luck")))
@get_user
async def call_potion_add(callback: CallbackQuery, user: User) -> None:
    user = await UserDAO.change_hero(user)
    await HeroDAO.patch(user.hero, potion=getattr(PotionEnum, callback.data.replace("potion_", "")))

    answer = user.hero.get_full_info() + "\n"
    answer += "Рекомендую вам ознакомится с 📜/prologue для большего погружения.\n\n Если ты готов, тогда вперед... 🏃"

    way = await WayDAO.find_one_or_none(next_page=1)
    await callback.message.edit_text(text=answer, reply_markup=ways_keyboard([way], user.hero))
