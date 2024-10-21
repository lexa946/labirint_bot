from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.bot.models.secondary import PageEnemy, PageAddStuff, PageRemoveStuff, PageAddBuff
from app.database import Base


class Page(Base):
    __tablename__ = 'pages'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    text: Mapped[str]

    enemies: Mapped[list['Enemy']] = relationship(back_populates="pages", secondary=PageEnemy.__table__, lazy="joined")
    add_stuffs: Mapped[list['Stuff']] = relationship(back_populates="add_pages", secondary=PageAddStuff.__table__, lazy="joined")
    remove_stuffs: Mapped[list['Stuff']] = relationship(back_populates="remove_pages", secondary=PageRemoveStuff.__table__, lazy="joined")
    add_buffs: Mapped[list['Buff']] = relationship(back_populates="add_pages", secondary=PageAddBuff.__table__, lazy="joined")

    game_over: Mapped[bool] = mapped_column(nullable=True, default=False)

    ways: Mapped[list['Way']] = relationship(back_populates="page", lazy="joined")
    heroes: Mapped[list['Hero']] = relationship(back_populates="current_page")

    combats_win_page: Mapped[list['Combat']] = relationship(backref="win_page", foreign_keys="Combat.win_page_id", lazy="joined")
    combats_leave_page: Mapped[list['Combat']] = relationship(backref="leave_page", foreign_keys="Combat.leave_page_id", lazy="joined")

    dice: Mapped[bool] = mapped_column(default=False)


    change_characteristic_name: Mapped[Optional[str]]
    change_characteristic_count: Mapped[Optional[str]]

    def __str__(self):
        if len(self.text) < 25:
            return f"{self.__class__.__name__} {self.id} {self.text}"
        else:
            return f"{self.__class__.__name__} {self.id} {self.text[:25]}..."
