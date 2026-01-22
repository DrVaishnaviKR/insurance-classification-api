# app/schema.py

from pydantic import BaseModel

class InsuranceRequest(BaseModel):
    age: int
    bmi: float
    children: int
    smoker: int   # 0 = No, 1 = Yes

class InsuranceResponse(BaseModel):
    premium_class: int
