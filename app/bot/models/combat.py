from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from app.database import Base


class Combat(Base):
    __tablename__ = "combat"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    hero_id: Mapped[int] = mapped_column(ForeignKey('heroes.id', ondelete="CASCADE"))
    hero: Mapped['Hero'] = relationship(back_populates='combat', lazy="joined")

    win_page_id: Mapped[int] = mapped_column(ForeignKey('pages.id'))
    # win_page: Mapped['Page'] = relationship(back_populates="combats_win_page", lazy="joined")

    leave_page_id: Mapped[int] = mapped_column(ForeignKey('pages.id'), nullable=True)
    # leave_page: Mapped['Page'] = relationship(back_populates="combats_leave_page", lazy="joined")

    enemies: Mapped[list['EnemyCombat']] = relationship(back_populates="combat", lazy="joined", cascade="all, delete")
