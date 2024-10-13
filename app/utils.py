import json

from sqlalchemy import select

from app.bot.models.main import Stuff, Page, Way, Enemy
from app.database import async_session_maker


async def insert_data_to_db():
    def read_mock(model):
        with open(f"mock_{model}.json", 'r', encoding="UTF-8") as f:
            return json.load(f)


    mock_stuff = read_mock("stuff")
    mock_pages = read_mock("pages")
    mock_enemies = read_mock("enemies")



    async with async_session_maker() as session:
        for stuff in mock_stuff:
            session.add(Stuff(**stuff))

        for enemy in mock_enemies:
            session.add(Enemy(**enemy))

        for mock_page in mock_pages:
            page = Page()
            page.id = mock_page['id']
            page.text = mock_page['text']
            if mock_page.get('game_over', False):
                page.game_over = True
            if mock_page.get('change_characteristic_name'):
                page.change_characteristic_name = mock_page.get('change_characteristic_name')
                page.change_characteristic_count = mock_page.get('change_characteristic_count')

            if mock_page.get('enemies'):
                for mock_enemy in mock_page.get('enemies'):
                    enemy = await session.scalar(
                        select(Enemy).where(Enemy.name==mock_enemy)
                    )
                    page.enemies.append(enemy)

            session.add(page)
            await session.flush()

            for mock_way in mock_page.get('ways', []):
                way = Way()
                way.description = mock_way['description']
                way.next_page = mock_way['next_page']
                if mock_way.get('luck_test', False):
                    way.luck_test = True


                if mock_way.get('stuff_need'):
                    stuff = await session.scalar(
                        select(Stuff).where(Stuff.name==mock_way['stuff_need'])
                    )
                    way.stuff_need = stuff
                way.page_id = page.id
                session.add(way)

        session.add(
            Way(description="Вперед", next_page=1)
        )

        await session.commit()
