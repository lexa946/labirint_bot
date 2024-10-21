from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.bot.utils.main import create_inline_keyboard


@create_inline_keyboard
def epigraph_keyboard(kb:InlineKeyboardBuilder):
    kb.button(text="Продолжить", callback_data="potion_choice")

@create_inline_keyboard
def potion_choice_keyboard(kb:InlineKeyboardBuilder):
    kb.button(text="Напиток Мудрых", callback_data="potion_skill")
    kb.button(text="Напиток Сильных", callback_data="potion_stamina")
    kb.button(text="Напиток Удачливых", callback_data="potion_luck")