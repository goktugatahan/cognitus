from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Data(Base):
    __tablename__ = "webapp_data"

    id = Column(Integer, primary_key=True)
    text = Column(String, index=True)
    label =  Column(String, index=True)
