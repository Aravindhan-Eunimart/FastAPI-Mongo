from typing import Optional
from pydantic import BaseModel
from pydantic import EmailStr, Field
from typing import Optional

class StudentBase(BaseModel):
    id: int
    name: str
    age: int
    class_: str = Field(..., alias='class')
    mother_name: str
    father_name: str
    mother_occupation: Optional [str]
    father_occupation: Optional [str]
    address: str
    phone_number_1: int = Field(..., alias='phone-number-1')
    phone_number_2: Optional [int]
    email: Optional [EmailStr]


class ProgressBase(BaseModel):
    exam_name: str
    grade: str
    physics: int
    chemistry: int 
    maths: int 
    total: int 
    percentage: int 


class StudentPublic(StudentBase):
    id: int


class StudentWithProgress(BaseModel):
    student: StudentBase
    progress: ProgressBase