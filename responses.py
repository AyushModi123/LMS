from pydantic import BaseModel
from bson import ObjectId

class MongoDBResponseModel(BaseModel):
    id: str = None

    class Config:
        allow_population_by_field_name = True
        json_encoders = {
            ObjectId: str
        }

class Address(BaseModel):
    city: str
    country: str

class StudentDetailsResponseModel(BaseModel):
    name: str
    age: int
    address: Address
    
class StudentResponseModel(BaseModel):
    name: str
    age: int    

class ListStudentsModel(BaseModel):
    data: list[StudentResponseModel]