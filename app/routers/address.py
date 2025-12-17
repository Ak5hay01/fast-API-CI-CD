from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import crud, schemas

router = APIRouter(prefix="/address", tags=["Address"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/{employee_id}", response_model=schemas.Address)
def add_address(
    employee_id: int,
    address: schemas.AddressCreate,
    db: Session = Depends(get_db)
):
    return crud.create_address(db, address, employee_id)
