from sqladmin import ModelView

from app.bot.models import User, Page, Stuff, Buff, Enemy, Way, Hero, Combat


class UserAdmin(ModelView, model=User):
    column_list = [c.name for c in User.__table__.c]

class HeroAdmin(ModelView, model=Hero):
    column_list = [c.name for c in Hero.__table__.c]

class PageAdmin(ModelView, model=Page):
    column_exclude_list = [Page.ways, Page.enemies, Page.add_buff_id, Page.heroes]

    column_formatters = {
        Page.text: lambda m, a: m.text[:50] + "...",
    }

    form_excluded_columns = [Page.ways, Page.enemies, Page.heroes]


class StuffAdmin(ModelView, model=Stuff):
    column_list = [c.name for c in Stuff.__table__.c]
    form_excluded_columns = [Stuff.heroes]

class BuffAdmin(ModelView, model=Buff):
    column_list = [c.name for c in Buff.__table__.c]


class EnemyAdmin(ModelView, model=Enemy):
    column_list = [c.name for c in Enemy.__table__.c]


class WayAdmin(ModelView, model=Way):
    column_list = [c.name for c in Way.__table__.c]

class CombatAdmin(ModelView, model=Combat):
    column_list = [c.name for c in Combat.__table__.c]






