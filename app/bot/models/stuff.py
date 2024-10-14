from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.bot.models.secondary import HeroStuff
from app.database import Base


class Stuff(Base):
    __tablename__ = 'stuffs'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]
    is_active: Mapped[bool] = mapped_column(default=False)

    heroes: Mapped[list['Hero']] = relationship(back_populates="stuffs", secondary=HeroStuff.__table__)
    pages: Mapped[list['Page']] = relationship(back_populates="add_stuff")
    ways_used: Mapped[list['Way']] = relationship(back_populates="stuff_need")

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name}"
