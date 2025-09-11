from sqlalchemy.orm import declarative_base
from sqlalchemy import column, String, Integer, Float, Boolean

Base=declarative_base()  # model base class

#models
class Employee(Base):  # our model class defined from ORM
    __tablename__ = "employees"
    id=column(Integer, primary_key=True)
    name=column(String(255), nullable=False)
    age=column(Integer, nullable=False)
    salary=column(Float, nullable=False)
    is_active=column(Boolean, nullable=False)

    def __repr__(self):
        return f"[id=(self.id), name={self.name}, age={self.age}, salary={self.salary}]"    #f string is placeholder or interpolated string
        