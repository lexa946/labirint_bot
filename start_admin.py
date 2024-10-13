from fastapi import FastAPI
from sqladmin import Admin

from app.database import async_engine
from app.admin.views import PageAdmin, UserAdmin, BuffAdmin, StuffAdmin, EnemyAdmin, WayAdmin, HeroAdmin
app = FastAPI()



admin = Admin(app, async_engine)


admin.add_view(UserAdmin)
admin.add_view(PageAdmin)
admin.add_view(BuffAdmin)
admin.add_view(StuffAdmin)
admin.add_view(EnemyAdmin)
admin.add_view(WayAdmin)
admin.add_view(HeroAdmin)
