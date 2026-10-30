
from sqlalchemy import Boolean, Column, Integer, String
from bd import Base


class Tache(Base):
    __tablename__ = "taches"

    id = Column(Integer, primary_key=True, index=True)
    titre = Column(String(255), nullable=False)
    description = Column(String(1000), nullable=True)
    terminee = Column(Boolean, default=False)





