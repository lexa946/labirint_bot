from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

class Way(Base):
    __tablename__ = 'ways'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    description: Mapped[str]
    next_page: Mapped[int]

    stuff_need_id: Mapped[int] = mapped_column(ForeignKey('stuffs.id'), nullable=True)
    stuff_need: Mapped['Stuff'] = relationship(back_populates="ways_used")

    buff_need_id: Mapped[int] = mapped_column(ForeignKey('buffs.id'), nullable=True)
    buff_need: Mapped['Buff'] = relationship(back_populates="ways_used")



    page_id: Mapped[int] = mapped_column(ForeignKey('pages.id'), nullable=True)
    page: Mapped['Page'] = relationship(back_populates="ways")

    characteristic_test: Mapped[Optional[str]]


    def __str__(self):
        return f"{self.__class__.__name__} {self.description} {self.next_page}"

