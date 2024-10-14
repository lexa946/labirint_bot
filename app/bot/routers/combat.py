from aiogram import Router, F
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove

from app.bot.models import Hero, Page, EnemyCombat, Way
from app.bot.utils.main import dice_parser
from app.bot.utils.game import check_game_over
from app.dao.main import CombatDAO, UserDAO, EnemyCombatDAO, HeroDAO
from app.keyboards.combat import attack_keyboard, luck_keyboard
from app.keyboards.game import ways_keyboard

router = Router()


@router.callback_query(F.data.startswith("combat_luck_"))
async def call_luck(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=None)


@router.message(F.text.startswith("Атаковать"))
@check_game_over
async def message_attack(message: Message):


    user = await UserDAO.find_one_or_none(telegram_id=message.from_user.id)
    if not user.hero.combat:
        return

    enemies = user.hero.combat.enemies

    try:
        target_enemy_name = message.text.split("⚔️")[1].strip()
    except IndexError:
        await message.answer(
            f"Я не понял кого ты бьешь 🤯"
        )
        return

    target_enemy = None
    for enemy in enemies:
        print(enemy)

        if enemy.enemy_base.name == target_enemy_name:
            target_enemy = enemy

    if not target_enemy:
        await message.answer(
            f"Я не понял кого ты бьешь 🤯"
        )
        return

    hero_dice = dice_parser("+1d6+1d6")
    hero_power = hero_dice[0] + user.hero.current_skill
    enemy_dice = dice_parser("+1d6+1d6")
    enemy_power = enemy_dice[0] + target_enemy.enemy_base.skill
    if hero_power > enemy_power:
        await EnemyCombatDAO.path(target_enemy, current_stamina=target_enemy.current_stamina-2)
        target_enemy.current_stamina -= 2
        punch_type = "attack"
    elif hero_power < enemy_power:
        await HeroDAO.path(user.hero, current_stamina=user.hero.current_stamina - 2)
        user.hero.current_stamina -= 2
        punch_type = "defend"
    else:
        punch_type = "pary"

    if user.hero.current_stamina < 1:
        await HeroDAO.path(user.hero, has_died=True)
        await message.answer("Тебе не удалось победить этого врага.\nНа этом твое приключение окончено!", reply_markup=ways_keyboard([]))
        return

    if target_enemy.current_stamina < 1:
        await EnemyCombatDAO.delete(target_enemy)
        enemies.remove(target_enemy)
        if enemies:
            await message.answer(f"{target_enemy.enemy_base.name} погиб ⚰️",
                                 reply_markup=attack_keyboard(enemies, can_leave=bool(user.hero.combat.leave_page_id)))
            return
        else:
            await message.reply(text="*<s>удаление клавитуры</s>*",reply_markup=ReplyKeyboardRemove())
            await message.answer(f"💪 Ты одержал победу 🎉", reply_markup=ways_keyboard([
                Way(description="Продолжить", next_page=user.hero.combat.win_page_id)
            ]))
            return

    punch_type_translate = {
        "attack":"Тебе удалось ранить врага -2❤️",
        "defend":"Враг ранил тебя -2❤️",
        "pary": "Вы отразили удары друг друга",
    }


    answer = f"Характеристики: {user.hero.get_status()}\n"
    answer += f"Твой бросок: {hero_dice[1][0]} {hero_dice[1][1]} - сила атаки {hero_power}\n\n"
    answer += f"{target_enemy.enemy_base.name} {target_enemy.get_health_status()} : {enemy_dice[1][0]} {enemy_dice[1][1]} - сила атаки {enemy_power}\n\n"
    answer += punch_type_translate[punch_type]

    await message.answer(answer, reply_markup=luck_keyboard(punch_type))
    return





async def start_combat(callback:CallbackQuery, hero:Hero, page:Page):
    if hero.combat:
        print(f"{hero.combat.id=}")
        await CombatDAO.delete(hero.combat)


    win_page_id = None
    leave_page_id = None

    for way in page.ways:
        if way.description.upper() == "ПОБЕДА":
            win_page_id = way.next_page
        elif way.description.upper() == "ОТСТУПИТЬ":
            leave_page_id = way.next_page

    combat = await CombatDAO.add(
        hero_id=hero.id,
        win_page_id=win_page_id,
        leave_page_id=leave_page_id,
        enemies=[EnemyCombat(
            enemy_id=enemy.id,
            current_stamina=enemy.stamina,
        )for enemy in page.enemies],
    )

    combat = await CombatDAO.find_one_or_none(id=combat.id)

    await callback.message.edit_text(page.text)
    await callback.message.answer(
        text=f"💥 Бой начинается. Твои противники:\n\n{'\n'.join(str(enemy) for enemy in combat.enemies)}",
        reply_markup=attack_keyboard(combat.enemies, can_leave=bool(leave_page_id))
    )


async def combat():
    ...