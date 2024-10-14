from aiogram.utils.keyboard import InlineKeyboardBuilder


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