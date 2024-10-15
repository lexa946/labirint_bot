from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from app.bot.models import User
from app.bot.utils.game import get_user
from app.dao.main import UserDAO

from app.bot.texts.tutorial import prolog
from app.bot.utils.main import get_hero_info
from app.keyboards.control import main_menu_keyboard, prolog_keyboard, back_to_main_menu_keyboard

router = Router()


@router.message(CommandStart())
@get_user
async def cmd_stat(message: Message, user:User) -> None:
    await message.answer(text="👋 Добро пожаловать в игру 💀\"Лабиринт страха\"🦴", reply_markup=main_menu_keyboard())


@router.message(Command('prologue'))
async def cmd_prologue(message: Message) -> None:
    messages_id = []
    for paragraph in prolog[:-1]:
        response = await message.answer(text=paragraph)
        messages_id.append(response.message_id)
    messages_id.append(messages_id[-1]+1)
    await message.answer(text=prolog[-1], reply_markup=prolog_keyboard(messages_id))


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
    await callback.message.edit_text(text=get_hero_info(user.hero), reply_markup=back_to_main_menu_keyboard())
