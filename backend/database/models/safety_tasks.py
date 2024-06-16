from sqlalchemy.orm import Mapped
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from backend.database.models.base import Base


class SafetyTasks(Base):
    __tablename__ = "safety_tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", onupdate="CASCADE", ondelete="CASCADE")
    )
    team_id: Mapped[int] = mapped_column(
        ForeignKey("teams.id", onupdate="CASCADE", ondelete="CASCADE")
    )
    task: Mapped[str]
    name: Mapped[str]
    date: Mapped[str]
    weight: Mapped[int]
    description: Mapped[str]

    user: Mapped[list["Users"]] = relationship(back_populates="safety_tasks")
    team: Mapped[list["Teams"]] = relationship(back_populates="safety_tasks")
