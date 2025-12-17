from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from ..database import SessionLocal
from .. import crud, schemas, auth

router = APIRouter(prefix="/employees", tags=["Employees"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signup", response_model=schemas.Employee)
def signup(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    if crud.get_employee_by_email(db, employee.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_employee(db, employee)

@router.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.get_employee_by_email(db, form_data.username)
    if not user or not auth.verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = auth.create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
