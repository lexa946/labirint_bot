import random
import re
from functools import wraps

from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.bot.models import Hero, Stuff
from app.bot.texts.game import dice_dict


def create_inline_keyboard(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        kb = InlineKeyboardBuilder()
        func(kb, *args, **kwargs)
        kb.adjust(1)
        return kb.as_markup()
    return wrapper

def create_hero() -> Hero:
    skill = 6 + random.randint(1, 6)
    stamina = 12 + random.randint(2, 12)
    luck = 6 +  random.randint(1, 6)

    new_hero = Hero()
    new_hero.max_skill = new_hero.current_skill = skill
    new_hero.max_stamina = new_hero.current_stamina = stamina
    new_hero.max_luck = new_hero.current_luck = luck

    new_hero.provision_count = 10
    new_hero.money_count = 0

    new_hero.current_page_id = 1
    return new_hero



def dice_parser(dice:str) -> tuple[int, list[str]]:
    matches = re.findall(r"[-+]\dd\d?", dice)
    result = 0
    dice_roll = []
    for match in matches:
        num_x, num_y = match.split("d")
        rand_y = random.randint(1, int(num_y))
        result += int(num_x) * rand_y
        dice_roll.append(dice_dict[rand_y])

    return result, dice_roll

