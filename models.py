from sqlalchemy import Column, Integer, String

from database import Base


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    address = Column(String(250))
    description = Column(String(500))
    age = Column(Integer)
