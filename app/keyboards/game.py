from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.bot.models import Way
from app.bot.utils.main import create_inline_keyboard


@create_inline_keyboard
def combat_win_keyboard(kb: InlineKeyboardBuilder, next_page_id:int):
    kb.button(text="Продолжить", callback_data=f"next_page_{next_page_id}")


@create_inline_keyboard
def ways_keyboard(kb: InlineKeyboardBuilder, ways: list[Way]):
    for way in ways:
        kb.button(text=way.description, callback_data=f"next_page_{way.next_page}")
    kb.button(text="Действия", callback_data="action")
    kb.button(text="Главное меню", callback_data="main_menu")

@create_inline_keyboard
def actions_keyboard(kb: InlineKeyboardBuilder,):
    kb.button(text="Сделать привал", callback_data="use_provision")
    kb.button(text="Использовать напиток", callback_data="use_potion")
    kb.button(text="Сделать привал", callback_data="use_provision")
    kb.button(text="Открыть рюкзак", callback_data="inventory")
    kb.button(text="Продолжить игру", callback_data="continue_game")


@create_inline_keyboard
def inventory_keyboard(kb: InlineKeyboardBuilder,):
    kb.button(text="Назад", callback_data="action")

