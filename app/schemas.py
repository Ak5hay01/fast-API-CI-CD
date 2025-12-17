from pydantic import BaseModel, EmailStr

class AddressBase(BaseModel):
    city: str
    state: str
    zipcode: str

class AddressCreate(AddressBase):
    pass

class Address(AddressBase):
    id: int

    class Config:
        from_attributes = True


class EmployeeCreate(BaseModel):
    email: EmailStr
    password: str


class Employee(BaseModel):
    id: int
    email: EmailStr
    address: Address | None = None

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str
