from aiogram import Router, F
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove

from app.bot.models import Hero, Page, EnemyCombat, User
from app.bot.utils.game import check_game_over, get_user
from app.bot.utils.main import dice_parser
from app.dao.main import CombatDAO, EnemyCombatDAO, HeroDAO
from app.keyboards.combat import attack_keyboard, luck_keyboard
from app.keyboards.game import ways_keyboard, combat_win_keyboard

router = Router()


@router.callback_query(F.data.startswith("combat_luck_"))
@get_user
async def call_luck(callback: CallbackQuery, user: User):
    punch_type, target_enemy_name = callback.data.replace("combat_luck_", "").split("_")

    enemies = user.hero.combat.enemies
    if not user.hero.combat:
        await callback.message.edit_reply_markup(reply_markup=None)
        return

    target_enemy = None
    for enemy in enemies:
        if enemy.enemy_base.name == target_enemy_name:
            target_enemy = enemy

    luck_dice = dice_parser("+1d6+1d6")
    if luck_dice[0] <= user.hero.current_luck:
        luck = True
        if punch_type == "defend":
            await HeroDAO.patch(user.hero, current_stamina=user.hero.current_stamina + 1)
            change_history_row = "Враг ранил тебя -1❤️"

        else:
            await EnemyCombatDAO.patch(target_enemy, current_stamina=target_enemy.current_stamina - 2)
            change_history_row = "Тебе удалось ранить врага -4❤️"
    else:
        luck = False
        if punch_type == "defend":
            await HeroDAO.patch(user.hero, current_stamina=user.hero.current_stamina - 1)
            change_history_row = "Враг ранил тебя -3❤️"

        else:
            await EnemyCombatDAO.patch(target_enemy, current_stamina=target_enemy.current_stamina + 1)
            target_enemy.current_stamina += 1
            change_history_row = "Тебе удалось ранить врага -1❤️"

    new_current_luck = user.hero.current_luck - 1
    await HeroDAO.patch(user.hero, current_luck=new_current_luck)
    user.hero.current_luck = new_current_luck

    answer = callback.message.text.split("\n")
    answer[0] = f"Характеристики: {user.hero.get_status()}"
    answer[5] = change_history_row
    answer.append("Удача на твоей стороне 🤗" if luck else "Удача отвернулась от тебя 😔")

    enemy_power = answer[3].split(":")[1]
    answer[3] = f"{target_enemy.enemy_base.name} {target_enemy.get_health_status()} : {enemy_power}"

    answer = "\n".join(answer)

    await callback.message.edit_text(answer, reply_markup=None)
    await check_died(callback.message, user, target_enemy)


@router.message(F.text.startswith("Атаковать"))
@get_user
@check_game_over
async def message_attack(message: Message, user: User):
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
        await EnemyCombatDAO.patch(target_enemy, current_stamina=target_enemy.current_stamina - 2)
        punch_type = "attack"
    elif hero_power < enemy_power:
        await HeroDAO.patch(user.hero, current_stamina=user.hero.current_stamina - 2)
        punch_type = "defend"
    else:
        punch_type = "pary"

    died = await check_died(message, user, target_enemy)
    if died: return

    punch_type_translate = {
        "attack": "Тебе удалось ранить врага -2❤️",
        "defend": "Враг ранил тебя -2❤️",
        "pary": "Вы отразили удары друг друга",
    }

    answer = f"Характеристики: {user.hero.get_status()}\n"
    answer += f"Твой бросок: {hero_dice[1][0]} {hero_dice[1][1]} - сила атаки {hero_power}\n\n"
    answer += f"{target_enemy.enemy_base.name} {target_enemy.get_health_status()} : {enemy_dice[1][0]} {enemy_dice[1][1]} - сила атаки {enemy_power}\n\n"
    answer += punch_type_translate[punch_type]

    if punch_type in ("attack", "defend"):
        keyboard = luck_keyboard(f"{punch_type}_{target_enemy_name}")
    else:
        keyboard = None
    await message.answer(answer, reply_markup=keyboard)
    return


async def check_died(message: Message, user: User, target_enemy: EnemyCombat) -> bool:
    enemies = user.hero.combat.enemies
    if user.hero.current_stamina < 1:
        await HeroDAO.patch(user.hero, has_died=True)
        await message.answer("Тебе не удалось победить этого врага.\nНа этом твое приключение окончено!",
                             reply_markup=ways_keyboard([]))
        return True

    if target_enemy.current_stamina < 1:
        await EnemyCombatDAO.delete(target_enemy)
        enemies.remove(target_enemy)
        if enemies:
            await message.answer(f"{target_enemy.enemy_base.name} погиб ⚰️",
                                 reply_markup=attack_keyboard(enemies, can_leave=bool(user.hero.combat.leave_page_id)))
            return True
        else:
            await message.reply(text="*<s>удаление клавитуры</s>*", reply_markup=ReplyKeyboardRemove())
            await message.answer(f"💪 Ты одержал победу 🎉",
                                 reply_markup=combat_win_keyboard(user.hero.combat.win_page_id))
            return True


async def start_combat(callback: CallbackQuery, hero: Hero, page: Page):
    if hero.combat:
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
        ) for enemy in page.enemies],
    )

    combat = await CombatDAO.find_one_or_none(id=combat.id)

    await callback.message.edit_text(page.text)
    await callback.message.answer(
        text=f"💥 Бой начинается. Твои противники:\n\n{'\n'.join(str(enemy) for enemy in combat.enemies)}",
        reply_markup=attack_keyboard(combat.enemies, can_leave=bool(leave_page_id))
    )
