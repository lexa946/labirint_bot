from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.bot.models.secondary import HeroStuff
from app.database import Base


class Stuff(Base):
    __tablename__ = 'stuffs'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]


    heroes: Mapped[list['Hero']] = relationship(back_populates="stuffs", secondary=HeroStuff.__table__)
    add_pages: Mapped[list['Page']] = relationship(back_populates="add_stuffs", secondary=HeroStuff.__table__)
    remove_pages: Mapped[list['Page']] = relationship(back_populates="remove_stuffs", secondary=HeroStuff.__table__)
    ways_used: Mapped[list['Way']] = relationship(back_populates="stuff_need")

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name}"

    def get_status(self):
        return f"<b>{self.name}</b>: {self.description}"
