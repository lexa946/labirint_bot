from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.bot.models import Stuff, Way


def ways_keyboard(ways: list[Way]):
    kb = InlineKeyboardBuilder()
    for way in ways:
        kb.button(text=way.description, callback_data=f"next_page_{way.next_page}")
    kb.button(text="Действия", callback_data="action")
    kb.button(text="Главное меню", callback_data="main_menu")
    kb.adjust(1)
    return kb.as_markup()


def actions_keyboard():
    kb = InlineKeyboardBuilder()
    kb.button(text="Сделать привал", callback_data="use_provision")
    kb.button(text="Открыть рюкзак", callback_data="inventory")
    kb.button(text="Продолжить игру", callback_data="continue_game")
    kb.adjust(1)
    return kb.as_markup()


def inventory_keyboard(stuff_exists: bool = True):
    kb = InlineKeyboardBuilder()
    if stuff_exists:
        kb.button(text="Использовать предмет", callback_data="use_stuff")
    kb.button(text="Отмена", callback_data="action")
    kb.adjust(1)
    return kb.as_markup()


def stuffs_keyboard(stuffs: list[Stuff]):
    kb = InlineKeyboardBuilder()
    for stuff in filter(lambda s: s.is_active, stuffs):
        kb.button(text=stuff.name, callback_data=f"use_stuff_{stuff.id}")
    kb.button(text="Отмена", callback_data="action")
    kb.adjust(1)
    return kb.as_markup()
