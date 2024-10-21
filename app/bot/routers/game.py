from aiogram import Router, F
from aiogram.types import CallbackQuery

from app.bot.models import Page, User
from app.bot.routers.combat import start_combat
from app.bot.utils.game import check_game_over, get_user
from app.dao.main import PageDAO, HeroDAO
from app.keyboards.game import actions_keyboard, inventory_keyboard, ways_keyboard

router = Router()


@router.callback_query(F.data == "continue_game")
@get_user
async def call_continue_game(callback: CallbackQuery, user: User) -> None:
    await call_next_page(
        CallbackQuery(id=callback.id, from_user=callback.from_user, chat_instance=callback.chat_instance,
                      message=callback.message, data=f"next_page_{user.hero.current_page_id}"))


@router.callback_query(F.data == "action")
@get_user
async def call_action(callback: CallbackQuery, user: User) -> None:
    answer = user.hero.get_full_info() + "\n"
    answer += "Выберите действие 👇"
    await callback.message.edit_text(answer, reply_markup=actions_keyboard())


@router.callback_query(F.data == "inventory")
@get_user
async def call_inventory(callback: CallbackQuery, user: User) -> None:
    if not user.hero.stuffs:
        await callback.message.edit_text(text="У вас пустой рюкзак 🎒💨", reply_markup=inventory_keyboard())
        return
    answer = user.hero.get_inventory()
    await callback.message.edit_text(text=answer, reply_markup=inventory_keyboard())


@router.callback_query(F.data == "use_provision")
@get_user
async def call_use_provision(callback: CallbackQuery, user: User) -> None:
    if user.hero.provision_count > 0:
        await HeroDAO.use_provision(user.hero)
        await callback.answer("Привал устроен! 🤤 Выносливость увеличина на 4")
    else:
        await callback.answer("Провизия кончилась 😔")

    await call_action(CallbackQuery(id=callback.id, from_user=callback.from_user, chat_instance=callback.chat_instance,
                                    message=callback.message))


@router.callback_query(F.data == "use_potion")
@get_user
async def call_use_potion(callback: CallbackQuery, user: User) -> None:
    if not user.hero.potion:
        await callback.answer(f"Напиток был использован ранее!")

    if user.hero.potion == "Напиток Мудрых":
        await HeroDAO.path(user.hero, current_skill=user.hero.max_skill)
    elif user.hero.potion == "Напиток Сильных":
        await HeroDAO.path(user.hero, current_stamina=user.hero.max_stamina)
    elif user.hero.potion == "Напиток Удачливых":
        await HeroDAO.path(user.hero, max_luck=user.hero.max_luck + 1, current_luck=user.hero.max_luck + 1)

    await callback.answer(f"{user.hero.potion} - использован!")
    await HeroDAO.path(user.hero, potion=None)


    await call_action(
        CallbackQuery(id=callback.id, from_user=callback.from_user, chat_instance=callback.chat_instance,
                      message=callback.message))


@router.callback_query(F.data.startswith("next_page_"))
@get_user
@check_game_over
async def call_next_page(callback: CallbackQuery, user: User) -> None:
    nex_page_id = int(callback.data.replace("next_page_", ""))
    next_page: Page = await PageDAO.find_one_or_none(id=nex_page_id)

    if next_page.game_over:
        await HeroDAO.path(user.hero, has_died=True)

    await HeroDAO.path(user.hero, current_page_id=next_page.id)

    if next_page.change_characteristic_name:
        for change_characteristic_name, change_characteristic_count in zip(
                next_page.change_characteristic_name.split(";"), next_page.change_characteristic_count.split(";")):
            await HeroDAO.change_characteristic(
                user.hero, change_characteristic_name, int(change_characteristic_count)
            )

    if next_page.enemies:
        await start_combat(callback, user.hero, next_page)
        return

    await callback.message.edit_text(f"{next_page.id}. {next_page.text}\n\n{user.hero.get_status()}", reply_markup=ways_keyboard(next_page.ways))
