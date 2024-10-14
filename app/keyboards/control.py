from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_menu_keyboard():
    kb = InlineKeyboardBuilder()
    kb.button(text="Новая игра", callback_data="new_game")
    kb.button(text="Продолжить игру", callback_data="continue_game")
    kb.button(text="Персонаж", callback_data="person")
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