from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from backend.database.models.base import Base


class Teams(Base):
    __tablename__ = "teams"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    points: Mapped[int]
    bonus: Mapped[int]

    users:  Mapped[list["Users"]] = relationship(back_populates="team")
    incidents: Mapped[list["Incidents"]] = relationship(back_populates="team")
    safety_tasks: Mapped[list["SafetyTasks"]] = relationship(back_populates="team")
