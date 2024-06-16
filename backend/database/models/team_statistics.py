from sqlalchemy.orm import Mapped
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column
from typing import Optional
from sqlalchemy.orm import relationship

from backend.database.models.base import Base


class TeamStatistics(Base):
    __tablename__ = "team_statistics"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("users.id", onupdate="CASCADE", ondelete="CASCADE")
    )
    team_id: Mapped[int] = mapped_column(
        ForeignKey("teams.id", onupdate="CASCADE", ondelete="CASCADE")
    )
