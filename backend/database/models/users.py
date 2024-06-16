from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from backend.database.models.base import Base


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    team: Mapped["Teams"] = relationship(back_populates="users")
    incidents: Mapped[list["Incidents"]] = relationship(back_populates="user")
    safety_tasks: Mapped[list["SafetyTasks"]] = relationship(back_populates="user")
