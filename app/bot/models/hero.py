import enum

from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates

from app.bot.models.secondary import HeroBuff, HeroStuff
from app.database import Base


class PotionEnum(enum.Enum):
    skill = "Напиток Мудрых"
    stamina = "Напиток Сильных"
    luck = "Напиток Удачливых"

    def __str__(self):
        return self.value

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

    potion: Mapped[PotionEnum] = mapped_column(Enum(PotionEnum), nullable=True)

    def get_status(self):
        return f"💪{self.current_skill}/{self.max_skill} ❤️{self.current_stamina}/{self.max_stamina} 🍀{self.current_luck}/{self.max_luck}"

    def get_full_info(self):
        return f"""
        Твой персонаж:
        💪 <b>Мастерство</b>: {self.current_skill}/{self.max_skill}
        ❤️ <b>Выносливость</b>: {self.current_stamina}/{self.max_stamina}
        🍀 <b>Удачливость</b>: {self.current_luck}/{self.max_luck}
        💰 <b>Золото</b>: {self.money_count}
        🍗 <b>Провизия</b>: {self.provision_count}
        ☠️ <b>Мерт</b>: {"Да" if self.has_died else "Нет"}
        🍷 <b>Напиток</b>: {self.potion or "Нет"}
        """

    def get_inventory(self):
        result = "Инвентарь:\n"
        for stuff in self.stuffs:
            result += stuff.get_status() + "\n"
        return result


    def __repr__(self):
        return f"{self.__class__.__name__} {self.user.first_name} {self.user.username}"

    @validates("provision_count", )
    def validate_provision_count(self, key, value):
        if value < 1:
            return 0
        return value

    @validates("current_luck","current_skill", "current_stamina")
    def validate_characteristics(self, key, value):
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


