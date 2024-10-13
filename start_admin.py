from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqladmin import Admin

from app.utils import insert_data_to_db
from app.database import async_engine, create_tables, drop_tables
from app.admin.views import PageAdmin, UserAdmin, BuffAdmin, StuffAdmin, EnemyAdmin, WayAdmin, HeroAdmin


@asynccontextmanager
async def lifespan(app: FastAPI):
    await drop_tables()
    await create_tables()
    await insert_data_to_db()
    yield

app = FastAPI(lifespan=lifespan)



admin = Admin(app, async_engine)


admin.add_view(UserAdmin)
admin.add_view(PageAdmin)
admin.add_view(BuffAdmin)
admin.add_view(StuffAdmin)
admin.add_view(EnemyAdmin)
admin.add_view(WayAdmin)
admin.add_view(HeroAdmin)
