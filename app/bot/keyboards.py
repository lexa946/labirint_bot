from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.bot.models.main import Way, Stuff


def main_menu_keyboard():
    kb = InlineKeyboardBuilder()
    kb.button(text="Новая игра", callback_data="new_game")
    kb.button(text="Продолжить игру", callback_data="continue_game")
    kb.button(text="Персонаж", callback_data="person")
    kb.adjust(1)
    return kb.as_markup()

def ways_keyboard(ways: list[Way]):
    kb = InlineKeyboardBuilder()
    for way in ways:
        kb.button(text=way.description, callback_data=f"next_page_{way.next_page}")
    kb.button(text="Действия", callback_data="action")
    kb.button(text="Главное меню", callback_data="main_menu")
    kb.adjust(1)
    return kb.as_markup()

def epigraph_keyboard():
    kb = InlineKeyboardBuilder()
    kb.button(text="Продолжить", callback_data="potion_choice")
    kb.adjust(1)
    return kb.as_markup()


def potion_choice_keyboard():
    kb = InlineKeyboardBuilder()
    kb.button(text="Напиток Мудрых", callback_data="potion_skill")
    kb.button(text="Напиток Сильных", callback_data="potion_stamina")
    kb.button(text="Напиток Удачливых", callback_data="potion_luck")
    kb.adjust(1)
    return kb.as_markup()

def back_to_main_menu_keyboard():
    kb = InlineKeyboardBuilder()
    kb.button(text="Главное меню", callback_data="main_menu")
    kb.adjust(1)
    return kb.as_markup()


def prolog_keyboard(messages_id: list[int]):
    kb = InlineKeyboardBuilder()
    call_back_data = "prolog_close_" + "_".join(str(id_) for id_ in messages_id)
    kb.button(text="Закрыть пролог", callback_data=call_back_data)
    kb.adjust(1)
    return kb.as_markup()

def actions_keyboard():
    kb = InlineKeyboardBuilder()
    kb.button(text="Сделать привал", callback_data="use_provision")
    kb.button(text="Открыть рюкзак", callback_data="inventory")
    kb.button(text="Продолжить игру", callback_data="continue_game")
    kb.adjust(1)
    return kb.as_markup()

def inventory_keyboard(stuff_exists: bool=True):
    kb = InlineKeyboardBuilder()
    if stuff_exists:
        kb.button(text="Использовать предмет", callback_data="use_stuff")
    kb.button(text="Отмена", callback_data="action")
    kb.adjust(1)
    return kb.as_markup()


def stuffs_keyboard(stuffs: list[Stuff]):
    kb = InlineKeyboardBuilder()
    for stuff in stuffs:
        kb.button(text=stuff.name, callback_data=f"use_stuff_{stuff.id}")
    kb.button(text="Отмена", callback_data="action")
    kb.adjust(1)
    return kb.as_markup()
