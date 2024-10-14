from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates

from app.bot.models.secondary import PageEnemy
from app.database import Base


class Enemy(Base):
    __tablename__ = 'enemies'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    skill: Mapped[int]
    stamina: Mapped[int]

    combat_enemies: Mapped[list['EnemyCombat']] = relationship(back_populates="enemy_base")

    pages: Mapped[list['Page']] = relationship(back_populates="enemies", secondary=PageEnemy.__table__)

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name}"


class EnemyCombat(Base):
    __tablename__ = 'enemy_combat'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    enemy_id: Mapped[int] = mapped_column(ForeignKey('enemies.id'))
    enemy_base: Mapped["Enemy"] = relationship(back_populates="combat_enemies", lazy="joined")

    current_stamina: Mapped[int]

    combat_id: Mapped[int] = mapped_column(ForeignKey('combat.id', ondelete="CASCADE"))
    combat: Mapped['Combat'] = relationship(back_populates="enemies")

    def __str__(self) -> str:
        return (f"{self.enemy_base.name} "
                f"💪{self.enemy_base.skill} ❤️{self.current_stamina}/{self.enemy_base.stamina}")

    def __repr__(self):
        return (f"{self.__class__.__name__} {self.enemy_base.name} "
                f"💪{self.enemy_base.skill} ❤️{self.current_stamina}/{self.enemy_base.stamina}")

    def get_health_status(self) -> str:
        return f"❤️{self.current_stamina}/{self.enemy_base.stamina}"

    @validates("current_stamina")
    def validate_stamina(self, key, value):
        if self.max_stamina < value:
            return self.max_stamina
        elif value < 1:
            return 0
        return value