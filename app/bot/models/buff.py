from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.bot.models.secondary import HeroBuff, PageAddBuff
from app.database import Base


class Buff(Base):
    __tablename__ = 'buffs'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]

    heroes: Mapped[list['Hero']] = relationship(back_populates="buffs", secondary=HeroBuff.__table__)
    add_pages: Mapped[list['Page']] = relationship(back_populates="add_buffs", secondary=PageAddBuff.__table__)
    ways_used: Mapped[list['Way']] = relationship(back_populates="buff_need")

    def __str__(self):
        return f"{self.__class__.__name__} {self.name}"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self.name == other.name:
                return True
        return False
