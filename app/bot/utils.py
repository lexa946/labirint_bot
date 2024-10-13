import random

from app.bot.models.main import Hero, Stuff
from app.bot.texts.game import hero_info, stuff_info


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


def get_hero_info(hero: Hero) -> str:
    info = hero_info.replace("{skill}", f"{hero.current_skill}/{hero.max_skill}")
    info = info.replace("{stamina}", f"{hero.current_stamina}/{hero.max_stamina}")
    info = info.replace("{luck}", f"{hero.current_luck}/{hero.max_luck}")
    info = info.replace("{inventory}", ", ".join(stuff.name for stuff in hero.stuffs))
    info = info.replace("{gold}", f"{hero.money_count}")
    info = info.replace("{provision}", f"{hero.provision_count}")
    if hero.has_died:
        info = info.replace("{has_died}", "Да")
    else:
        info = info.replace("{has_died}", "Нет")
    return info


def get_stuffs_info(stuffs: list[Stuff]) -> str:
    info = ""
    for stuff in stuffs:
        #<b>{stuff_name}</b>: {stuff_description}| {is_active}
        info += (stuff_info
                   .replace("{stuff_name}", stuff.name)
                   .replace("{stuff_description}", stuff.description)
                   .replace("{is_active}", "Активный" if stuff.is_active else "Пассивный")
                   )
    return info