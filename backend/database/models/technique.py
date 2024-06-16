from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from backend.database.models.base import Base


class Techniques(Base):
    __tablename__ = "techniques"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    incidents: Mapped[list["Techniques"]] = relationship(back_populates="technique")
