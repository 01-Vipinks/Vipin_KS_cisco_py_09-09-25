from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, Float, Boolean

Base = declarative_base()  # model base class

# models

class Flight(Base):  # our model class defined from ORM
    __tablename__ = "flights"

    id = Column(Integer, primary_key=True)
    number = Column(String(255), nullable=False)
    airline_name = Column(String(255), nullable=False)
    capacity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    source = Column(String(255), nullable=False)
    destination = Column(String(255), nullable=False)
    is_active = Column(Boolean, nullable=False)

    def __repr__(self):
        return f"[id={self.id}, number={self.number}, airline_name={self.airline_name}, capacity={self.capacity}, price={self.price}, source={self.source}, destination={self.destination}]"
