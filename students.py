from fastapi import FastAPI, HTTPException, Query
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Depends

from database import get_db, Collection

from bson import ObjectId
from responses import MongoDBResponseModel, ListStudentsModel, StudentResponseModel, StudentDetailsResponseModel
from schemas import StudentDetailsSchema, PatchStudentSchema

router = APIRouter(prefix="/students", tags=["Students"])

#660fe379370d151b5e0a7ea9
#660fe50418d1840ae638e75c

# Create Student
@router.post("", response_model=MongoDBResponseModel)
async def create_student(student: StudentDetailsSchema, collection: Collection = Depends(get_db)):
    student_dict = student.dict()
    result = collection.insert_one(student_dict)
    inserted_id = str(result.inserted_id)
    return {"id": inserted_id}

# List Students
@router.get("", response_model=ListStudentsModel)
async def list_students(country: str = Query(None), age: int = Query(None), collection: Collection = Depends(get_db)):
    filter_query = {}
    if country:
        filter_query['address.country'] = country
    if age:
        filter_query['age'] = {"$gte": age}

    students = collection.find(filter_query, {'name': 1, 'age': 1})
    return {"data": list(students)}

# Fetch Student
@router.get("/{student_id}", response_model=StudentDetailsResponseModel)
async def fetch_student(student_id: str, collection: Collection = Depends(get_db)):
    student = collection.find_one({"_id": ObjectId(student_id)})
    if student:
        return student
    raise HTTPException(status_code=404, detail="Student not found")

# Update Student
@router.patch("/{student_id}", response_model=dict({}))
async def update_student(student_id: str, student_data: PatchStudentSchema, collection: Collection = Depends(get_db)):
    student_data = jsonable_encoder(student_data)
    update_result = collection.update_one({"_id": ObjectId(student_id)}, {"$set": student_data})
    if update_result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return {}

# Delete Student
@router.delete("/{student_id}", response_model=dict({}))
async def delete_student(student_id: str,  collection: Collection = Depends(get_db)):
    delete_result = collection.delete_one({"_id": ObjectId(student_id)})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return {}
