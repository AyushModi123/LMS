from pydantic import BaseModel,  constr
from typing import Optional

class Address(BaseModel):
    city: constr(min_length=1)
    country: constr(min_length=1)
    
class StudentDetailsSchema(BaseModel):
    name: constr(min_length=1)
    age: int
    address: Address

class PatchStudentSchema(BaseModel):
    name: Optional[str]
    age: Optional[int]
    address: Optional[Address]