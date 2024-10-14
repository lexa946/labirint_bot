from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup

from app.bot.models import EnemyCombat
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def attack_keyboard(enemies:list[EnemyCombat], can_leave=False) -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    for enemy in enemies:
        kb.button(text=f"Атаковать ⚔️ {enemy.enemy_base.name}")
    if can_leave:
        kb.button(text="Отступить 🏃💨")
    kb.adjust(1)
    return kb.as_markup()


def luck_keyboard(callback_data:str) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Испытать удачу", callback_data=f"combat_luck_{callback_data}")
    kb.adjust(1)
    return kb.as_markup()
