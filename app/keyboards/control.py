from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.bot.utils.main import create_inline_keyboard


@create_inline_keyboard
def main_menu_keyboard(kb:InlineKeyboardBuilder):
    kb.button(text="Новая игра", callback_data="new_game")
    kb.button(text="Продолжить игру", callback_data="continue_game")
    kb.button(text="Персонаж", callback_data="person")

@create_inline_keyboard
def back_to_main_menu_keyboard(kb:InlineKeyboardBuilder):
    kb.button(text="Главное меню", callback_data="main_menu")

@create_inline_keyboard
def close_long_message_keyboard(kb:InlineKeyboardBuilder, messages_id: list[int]):
    call_back_data = "long_close_" + "_".join(str(id_) for id_ in messages_id)
    kb.button(text="Закрыть", callback_data=call_back_data)