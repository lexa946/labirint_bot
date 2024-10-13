from aiogram import Router, F

from aiogram.types import  CallbackQuery

from app.bot.utils import get_hero_info, get_stuffs_info
from app.dao.main import PageDAO, UserDAO, StuffDAO, HeroDAO
from app.bot.keyboards import ways_keyboard, actions_keyboard, inventory_keyboard, stuffs_keyboard

router = Router()



@router.callback_query(F.data == "continue_game")
async def call_continue_game(callback: CallbackQuery) -> None:
    user = await UserDAO.find_one_or_none(telegram_id=callback.from_user.id)
    await call_next_page(CallbackQuery(id=callback.id, from_user=callback.from_user, chat_instance=callback.chat_instance,
                                       message=callback.message, data=f"next_page_{user.hero.current_page_id}"))

@router.callback_query(F.data == "action")
async def call_action(callback: CallbackQuery) -> None:
    user = await UserDAO.find_one_or_none(telegram_id=callback.from_user.id)
    answer = get_hero_info(user.hero) + "\n"
    answer += "Выберите действие"
    await callback.message.edit_text(answer, reply_markup=actions_keyboard())


@router.callback_query(F.data == "inventory")
async def call_inventory(callback: CallbackQuery) -> None:
    user = await UserDAO.find_one_or_none(telegram_id=callback.from_user.id)
    if not user.hero.stuffs:
        await callback.message.edit_text(text="У вас пустой рюкзак", reply_markup=stuffs_keyboard([]))
        return
    answer = get_stuffs_info(user.hero.stuffs)
    await callback.message.edit_text(text=answer, reply_markup=inventory_keyboard(bool(user.hero.stuffs)))


@router.callback_query(F.data == "use_provision")
async def call_use_provision(callback: CallbackQuery) -> None:
    user = await UserDAO.find_one_or_none(telegram_id=callback.from_user.id)
    await HeroDAO.use_provision(user.hero)
    await callback.answer("Привал устроен! Выносливость увеличина на 4")
    await call_action(CallbackQuery(id=callback.id, from_user=callback.from_user, chat_instance=callback.chat_instance,
                                       message=callback.message))



@router.callback_query(F.data == "use_stuff")
async def call_stuff(callback: CallbackQuery) -> None:
    user = await UserDAO.find_one_or_none(telegram_id=callback.from_user.id)
    await callback.message.edit_reply_markup(reply_markup=stuffs_keyboard(user.hero.stuffs))


@router.callback_query(F.data.startswith("use_stuff_"))
async def call_use_stuff(callback: CallbackQuery) -> None:
    user = await UserDAO.find_one_or_none(telegram_id=callback.from_user.id)
    stuff_id = int(callback.data.replace("use_stuff_", ""))
    stuff = await StuffDAO.find_one_or_none(id=stuff_id)

    if stuff.name == "Напиток Мудрых":
        await HeroDAO.path(user.hero, current_skill=user.hero.max_skill)
    elif stuff.name == "Напиток Сильных":
        await HeroDAO.path(user.hero, current_stamina=user.hero.max_stamina)
    elif stuff.name == "Напиток Удачливых":
        await HeroDAO.path(user.hero, max_luck=user.hero.max_luck+1, current_luck=user.hero.max_luck+1)
    await HeroDAO.remove_stuff(user.hero, stuff)
    await callback.answer(f"{stuff.name} - использован!")

    await call_inventory(CallbackQuery(id=callback.id, from_user=callback.from_user, chat_instance=callback.chat_instance,
                                       message=callback.message))





@router.callback_query(F.data.startswith("next_page_"))
async def call_next_page(callback: CallbackQuery) -> None:
    nex_page_id = int(callback.data.replace("next_page_", ""))
    next_page = await PageDAO.find_one_or_none(id=nex_page_id)
    keyboard = ways_keyboard(next_page.ways)
    await callback.message.edit_text(next_page.text, reply_markup=keyboard)
