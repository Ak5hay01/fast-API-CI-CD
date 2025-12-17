from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    address = relationship("Address", back_populates="employee", uselist=False)

class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String)
    state = Column(String)
    zipcode = Column(String)

    employee_id = Column(Integer, ForeignKey("employees.id"))
    employee = relationship("Employee", back_populates="address")
