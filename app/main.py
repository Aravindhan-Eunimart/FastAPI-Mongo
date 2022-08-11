import uvicorn
from fastapi import FastAPI, Depends, status
from database import get_db
from schemas import ProgressBase, StudentBase, StudentPublic, StudentWithProgress
from pymongo.collection import Collection


import service


app = FastAPI()

DEBUG = True


@app.get("/student/{id}")
async def get_single(id: int, db: Collection = Depends(get_db)):
    status = service.get_single_record(id, db)
    return status 


@app.get('/student/')
def get_all(db: Collection = Depends(get_db)):
    status = service.get_all_record(db)
    return status


@app.post('/student/', status_code=status.HTTP_201_CREATED)
async def insert_single(student: StudentBase, progress: ProgressBase, db: Collection = Depends(get_db)):
    print(student)
    print(progress)
    status = service.insert_single_record(student, db)
    return status


@app.post('/students/', status_code=status.HTTP_201_CREATED)
async def insert_many(students: list[StudentWithProgress], db: Collection = Depends(get_db)):
    students_data = [data.student.dict() for data in students]
    print(students_data)
    status = service.insert_multiple_record(students_data, db)
    return status


@app.delete('/student/{id}')
def delete_single(id: int, db: Collection = Depends(get_db)):
    status = service.delete_single_record(id, db)
    return status


@app.delete('/student/')
def delete_all(db: Collection = Depends(get_db)):
    status = service.delete_all_record(db)
    return status


if __name__ == "__main__":
    uvicorn.run("main:app", debug=DEBUG, port=5000, reload=True)
