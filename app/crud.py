from sqlalchemy.orm import Session
from . import models, schemas, auth

def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(
        email=employee.email,
        password=auth.hash_password(employee.password)
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def get_employee_by_email(db: Session, email: str):
    return db.query(models.Employee).filter(models.Employee.email == email).first()

def create_address(db: Session, address: schemas.AddressCreate, employee_id: int):
    db_address = models.Address(**address.dict(), employee_id=employee_id)
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address
