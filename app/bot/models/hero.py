from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates

from app.bot.models.secondary import HeroBuff, HeroStuff
from app.database import Base

class Hero(Base):
    __tablename__ = 'heroes'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    has_died: Mapped[bool] = mapped_column(default=False)

    current_page_id: Mapped[int] = mapped_column(ForeignKey('pages.id'))
    current_page: Mapped['Page'] = relationship(back_populates='heroes')

    user_id: Mapped[int] = mapped_column(ForeignKey('users.telegram_id'))
    user: Mapped['User'] = relationship(back_populates='hero', lazy="joined")

    combat: Mapped['Combat'] = relationship(back_populates='hero', lazy="joined", cascade="all, delete")

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

    def get_status(self):
        return f"💪{self.current_skill}/{self.max_skill} ❤️{self.current_stamina}/{self.max_stamina} 🍀{self.current_luck}/{self.max_luck}"

    def __repr__(self):
        return f"{self.__class__.__name__} {self.user.first_name} {self.user.username}"

    @validates("provision_count", )
    def validate_provision_count(self, key, value):
        if value < 1:
            return 0
        return value

    @validates("current_luck","current_skill", "current_stamina")
    def validate_luck(self, key, value):
        attrs_check = {
            "current_luck": self.max_luck,
            "current_skill": self.max_skill,
            "current_stamina": self.max_stamina,
        }
        if attrs_check[key] < value:
            return attrs_check[key]
        elif value < 1:
            return 0
        return value
