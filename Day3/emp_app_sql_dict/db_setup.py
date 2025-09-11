from sqlalchemy import engine, create_engine
from sqlalchemy.orm import sessionmaker
from db_models import Base, Employee

# db setup
enginer=create_engine("sqlite:///employee_app_db.db", echo= True)
Base.metadata.create_all(engine) #creates tables
#session for sql operations
SessionLocal = sessionmaker(bind=engine)
session=SessionLocal() # for sql ops