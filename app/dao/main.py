from sqlalchemy import select, delete

from app.bot.models import User, Page, Way, Stuff, Hero, Combat, EnemyCombat
from app.bot.utils.main import create_hero
from app.dao.base import BaseDAO
from app.database import async_session_maker


class UserDAO(BaseDAO):
    model = User

    @classmethod
    async def change_hero(cls, user: User):
        async with async_session_maker() as session:
            if user.hero:
                user.hero.stuffs.clear()
                user.hero.buffs.clear()
                session.add(user.hero)
                await session.flush()
                await session.execute(
                    delete(Hero).where(Hero.id == user.hero.id)
                )
            new_hero = create_hero()
            new_hero.user_id = user.telegram_id
            session.add(new_hero)
            await session.commit()
            return await session.scalar(
                select(User).where(User.telegram_id == user.telegram_id)
            )


class PageDAO(BaseDAO):
    model = Page


class WayDAO(BaseDAO):
    model = Way

class CombatDAO(BaseDAO):
    model = Combat

class EnemyCombatDAO(BaseDAO):
    model = EnemyCombat


class StuffDAO(BaseDAO):
    model = Stuff


class HeroDAO(BaseDAO):
    model = Hero

    @classmethod
    async def add_stuff(cls, hero: Hero, stuff: Stuff):
        """
           Добавляет предмет герою
        """
        async with async_session_maker() as session:
            hero.stuffs.append(stuff)
            session.add(hero)
            await session.commit()

    @classmethod
    async def remove_stuff(cls, hero: Hero, stuff: Stuff):
        """
           Убирает предмет у героя
        """
        async with async_session_maker() as session:
            for hero_stuff in hero.stuffs:
                if hero_stuff.id == stuff.id:
                    hero.stuffs.remove(hero_stuff)
                    session.add(hero)
                    break
            await session.commit()

    @classmethod
    async def use_provision(cls, hero: Hero):
        """
           Привал героя
        """
        if hero.provision_count < 1: return
        async with async_session_maker() as session:
            hero.provision_count -= 1
            hero.current_stamina += 4
            session.add(hero)
            await session.commit()

    @classmethod
    async def change_characteristic(cls, hero: Hero, characteristic_name: str, characteristic_count: int):
        """
            Изменение характеристики героя
        """
        async with async_session_maker() as session:
            setattr(hero, characteristic_name,
                    getattr(hero, characteristic_name) + characteristic_count)
            session.add(hero)
            await session.commit()
