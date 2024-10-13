from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates

from app.bot.models.secondary import PageEnemy, HeroBuff, HeroStuff
from app.database import Base


class User(Base):
    __tablename__ = 'users'
    telegram_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(nullable=True)
    state: Mapped[int] = mapped_column(nullable=False)

    hero: Mapped["Hero"] = relationship(back_populates='user', lazy="joined")

    def __str__(self):
        return f"{self.__class__.__name__} {self.first_name} {self.username}"


class Hero(Base):
    __tablename__ = 'heroes'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    has_died: Mapped[bool] = mapped_column(default=False)

    current_page_id: Mapped[int] = mapped_column(ForeignKey('pages.id'))
    current_page: Mapped["Page"] = relationship(back_populates='heroes')

    user_id: Mapped[int] = mapped_column(ForeignKey('users.telegram_id'))
    user: Mapped["User"] = relationship(back_populates='hero', lazy="joined")

    current_skill: Mapped[int]
    max_skill: Mapped[int]

    current_stamina: Mapped[int]
    max_stamina: Mapped[int]

    current_luck: Mapped[int]
    max_luck: Mapped[int]

    provision_count: Mapped[int] = mapped_column(default=10)
    money_count: Mapped[int] = mapped_column(default=0)

    buffs: Mapped[list['Buff']] = relationship(back_populates="heroes", secondary=HeroBuff.__table__, lazy="joined")
    stuffs: Mapped[list['Stuff']] = relationship(back_populates="heroes", secondary=HeroStuff.__table__, lazy="joined")

    def __str__(self):
        return f"{self.__class__.__name__} {self.user.first_name} {self.user.username}"

    @validates("provision_count")
    def validate_provision_count(self, key, value):
        if value < 1:
            return 0
        return value

    @validates("current_skill")
    def validate_skill(self, key, value):
        if self.max_skill < value:
            return self.max_skill
        return value

    @validates("current_stamina")
    def validate_stamina(self, key, value):
        if self.max_stamina < value:
            return self.max_stamina
        return value

    @validates("current_luck")
    def validate_luck(self, key, value):
        if self.max_luck < value:
            return self.max_luck
        return value


class Buff(Base):
    __tablename__ = 'buffs'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False, )

    heroes: Mapped[list['Hero']] = relationship(back_populates="buffs", secondary=HeroBuff.__table__)
    pages: Mapped[list['Page']] = relationship(back_populates="add_buff")

    def __str__(self):
        return f"{self.__class__.__name__} {self.name}"


class Stuff(Base):
    __tablename__ = 'stuffs'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    description: Mapped[str] = mapped_column(nullable=True)
    is_active: Mapped[bool] = mapped_column(default=False)

    heroes: Mapped[list['Hero']] = relationship(back_populates="stuffs", secondary=HeroStuff.__table__)
    pages: Mapped[list['Page']] = relationship(back_populates="add_stuff")
    ways_used: Mapped[list['Way']] = relationship(back_populates="stuff_need")


    def __repr__(self):
        return f"{self.__class__.__name__} {self.name}"


class Enemy(Base):
    __tablename__ = 'enemies'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    skill: Mapped[int]
    stamina: Mapped[int]

    pages: Mapped[list["Page"]] = relationship(back_populates="enemies", secondary=PageEnemy.__table__)

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name}"

class Page(Base):
    __tablename__ = 'pages'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    text: Mapped[str]

    enemies: Mapped[list["Enemy"]] = relationship(back_populates="pages", secondary=PageEnemy.__table__)

    game_over: Mapped[bool] = mapped_column(nullable=True, default=False)


    add_stuff_id:Mapped[int] = mapped_column(ForeignKey('stuffs.id'), nullable=True)
    add_stuff: Mapped['Stuff'] = relationship(back_populates="pages")


    add_buff_id: Mapped[int] = mapped_column(ForeignKey('buffs.id'), nullable=True)
    add_buff: Mapped['Buff'] = relationship(back_populates="pages")

    ways: Mapped[list['Way']] = relationship(back_populates="page", lazy="joined")

    heroes: Mapped[list['Hero']] = relationship(back_populates="current_page")


    dice: Mapped[bool] = mapped_column(default=False)
    change_characteristic_name: Mapped[str] = mapped_column(nullable=True) # несколько характеристик надо писать через ; без пробела. Например "money_count;current_skill"
    change_characteristic_count: Mapped[str] = mapped_column(nullable=True) # необходимо записывать в нотации кубика +1d1, -10d1, +1d6+1d6, -1d6+1d6-2d1. несколько записей разделяй ;


    def __str__(self):
        if len(self.text) < 25:
            return f"{self.__class__.__name__} {self.id} {self.text}"
        else:
            return f"{self.__class__.__name__} {self.id} {self.text[:25]}..."


class Way(Base):
    __tablename__ = 'ways'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    description: Mapped[str]
    next_page: Mapped[int]

    stuff_need_id: Mapped[int] = mapped_column(ForeignKey('stuffs.id'), nullable=True)
    stuff_need: Mapped['Stuff'] = relationship(back_populates="ways_used")

    page_id: Mapped[int] = mapped_column(ForeignKey('pages.id'), nullable=True)
    page: Mapped['Page'] = relationship(back_populates="ways")

    characteristic_test: Mapped[str] = mapped_column(nullable=True)


    def __str__(self):
        return f"{self.__class__.__name__} {self.description} {self.next_page}"
