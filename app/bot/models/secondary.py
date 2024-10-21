from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class PageEnemy(Base):
    __tablename__ = 'page_enemy'

    enemy_id: Mapped[int] = mapped_column(ForeignKey('enemies.id'), primary_key=True, index=True)
    page_id: Mapped[int] = mapped_column(ForeignKey('pages.id'), primary_key=True, index=True)


class PageAddStuff(Base):
    __tablename__ = 'page_add_stuff'

    page_id: Mapped[int] = mapped_column(ForeignKey('pages.id'), primary_key=True, index=True)
    stuff_id: Mapped[int] = mapped_column(ForeignKey('stuffs.id'), primary_key=True, index=True)


class PageRemoveStuff(Base):
    __tablename__ = 'page_remove_stuff'

    page_id: Mapped[int] = mapped_column(ForeignKey('pages.id'), primary_key=True, index=True)
    stuff_id: Mapped[int] = mapped_column(ForeignKey('stuffs.id'), primary_key=True, index=True)


class PageAddBuff(Base):
    __tablename__ = 'page_add_buff'

    page_id: Mapped[int] = mapped_column(ForeignKey('pages.id'), primary_key=True, index=True)
    buff_id: Mapped[int] = mapped_column(ForeignKey('buffs.id'), primary_key=True, index=True)


class HeroBuff(Base):
    __tablename__ = 'hero_buff'
    hero_id: Mapped[int] = mapped_column(ForeignKey('heroes.id'), primary_key=True, index=True)
    buff_id: Mapped[int] = mapped_column(ForeignKey('buffs.id'), primary_key=True, index=True)


class HeroStuff(Base):
    __tablename__ = 'hero_stuff'

    hero_id: Mapped[int] = mapped_column(ForeignKey('heroes.id'), primary_key=True, index=True)
    stuff_id: Mapped[int] = mapped_column(ForeignKey('stuffs.id'), primary_key=True, index=True)
