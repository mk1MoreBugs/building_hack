from sqlalchemy.orm import Mapped
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column
from typing import Optional
from backend.database.models.base import Base
from sqlalchemy.orm import relationship


class Incidents(Base):
    __tablename__ = "incidents"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("users.id", onupdate="CASCADE", ondelete="CASCADE")
    )
    team_id: Mapped[int] = mapped_column(
        ForeignKey("teams.id", onupdate="CASCADE", ondelete="CASCADE")
    )
    technique_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("techniques.id", onupdate="CASCADE", ondelete="CASCADE")
    )
    date: Mapped[str]
    description: Mapped[str]

    user: Mapped["Users"] = relationship(back_populates="incidents")
    team: Mapped["Teams"] = relationship(back_populates="incidents")
    technique: Mapped["Techniques"] = relationship(back_populates="incidents")
