import asyncio

from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from app.bot.models import User
from app.bot.texts.tutorial import prolog
from app.bot.utils.game import get_user
from app.bot.utils.main import dice_parser
from app.dao.main import UserDAO, HeroDAO
from app.keyboards.control import main_menu_keyboard, prolog_keyboard, back_to_main_menu_keyboard
from app.keyboards.game import ways_keyboard

router = Router()


@router.message(CommandStart())
@get_user
async def cmd_stat(message: Message, user: User) -> None:
    await message.answer(text="👋 Добро пожаловать в игру 💀\"Лабиринт страха\"🦴", reply_markup=main_menu_keyboard())


@router.message(Command('prologue'))
async def cmd_prologue(message: Message) -> None:
    messages_id = []
    for paragraph in prolog[:-1]:
        response = await message.answer(text=paragraph)
        messages_id.append(response.message_id)
    messages_id.append(messages_id[-1] + 1)
    await message.answer(text=prolog[-1], reply_markup=prolog_keyboard(messages_id))


@router.message(Command('roll'))
@get_user
async def cmd_roll(message: Message, user: User) -> None:
    send_message = await message.answer("Подготавливаем кубики 🎲🎲")
    await asyncio.sleep(0.7)
    await send_message.edit_text("✊ Мешаем...")
    await asyncio.sleep(0.7)
    dice = dice_parser("+1d6+1d6")
    await send_message.edit_text(f"Твой результат {dice[0]} - {dice[1][0]} {dice[1][1]}")

    if not user.hero.current_page.ways[0].characteristic_test and not user.hero.current_page.ways[1].characteristic_test:
        return

    test_pass = False

    if user.hero.current_page.ways[0].characteristic_test:
        test_characteristic_way = user.hero.current_page.ways[0]
        passed_way = user.hero.current_page.ways[1]
    else:
        test_characteristic_way = user.hero.current_page.ways[1]
        passed_way = user.hero.current_page.ways[0]

    if test_characteristic_way.characteristic_test == "current_luck":
        if user.hero.current_luck >= dice[0]:
            test_pass = True
        await HeroDAO.patch(user.hero, current_luck=user.hero.current_luck - 1)
    elif test_characteristic_way.characteristic_test == "current_skill":
        if user.hero.current_skill >= dice[0]:
            test_pass = True

    if test_pass:
        await message.answer("Испытание пройдено",
                             reply_markup=ways_keyboard([test_characteristic_way], user.hero))
    else:
        await message.answer("Испытание не пройдено",
                             reply_markup=ways_keyboard([passed_way], user.hero))


@router.callback_query(F.data.startswith("prolog_close_"))
async def call_prolog_close(callback: CallbackQuery) -> None:
    messages_id = [int(id_) for id_ in callback.data.replace("prolog_close_", "").split("_")]
    for message_id in messages_id:
        await callback.bot.delete_message(chat_id=callback.message.chat.id, message_id=message_id)


@router.message(Command('main_menu'))
async def cmd_main_menu(message: Message) -> None:
    await message.answer(text="Главное меню 💀\"Лабиринт страха\"🦴",
                         reply_markup=main_menu_keyboard())


@router.callback_query(F.data == "main_menu")
async def call_main_menu(callback: CallbackQuery) -> None:
    await callback.message.edit_text(text="Главное меню 💀\"Лабиринт страха\"🦴", reply_markup=main_menu_keyboard())


@router.callback_query(F.data == "person")
@get_user
async def call_person(callback: CallbackQuery, user: User) -> None:
    if not user.hero:
        user = await UserDAO.change_hero(user)
    await callback.message.edit_text(text=user.hero.get_full_info(), reply_markup=back_to_main_menu_keyboard())
