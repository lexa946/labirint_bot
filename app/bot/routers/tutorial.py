from aiogram import Router, F
from aiogram.types import CallbackQuery


from app.dao.main import UserDAO, WayDAO, StuffDAO, HeroDAO

from app.bot.texts.tutorial import epigraph, potion_choice
from app.bot.utils.main import get_hero_info
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
async def call_potion_add(callback: CallbackQuery) -> None:
    potion_translate = {
        "potion_skill": "Напиток Мудрых",
        "potion_stamina": "Напиток Сильных",
        "potion_luck": "Напиток Удачливых"
    }
    potion_stuff = await StuffDAO.find_one_or_none(name=potion_translate[callback.data])

    user = await UserDAO.find_one_or_none(telegram_id=callback.from_user.id)
    if not user:
        user = await UserDAO.add(telegram_id=callback.from_user.id,
                                 first_name=callback.from_user.first_name,
                                 username=callback.from_user.username,
                                 state=0,
                                 )

    user = await UserDAO.change_hero(user)

    await HeroDAO.add_stuff(user.hero, potion_stuff)

    answer = get_hero_info(user.hero) + "\n"
    answer += "Рекомендую вам ознакомится с 📜/prologue для большего погружения.\n\n Если ты готов, тогда вперед... 🏃"

    way = await WayDAO.find_one_or_none(next_page=1)
    await callback.message.edit_text(text=answer, reply_markup=ways_keyboard([way]))
