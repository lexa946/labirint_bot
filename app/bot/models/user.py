from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

class User(Base):
    __tablename__ = 'users'
    telegram_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    first_name: Mapped[str]
    username: Mapped[Optional[str]]
    state: Mapped[Optional[int]]

    hero: Mapped['Hero'] = relationship(back_populates='user', lazy="joined")

    def __str__(self):
        return f"{self.__class__.__name__} {self.first_name} {self.username}"
