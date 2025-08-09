from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str=Field(min_length=2,max_length=20)
    age: int
    city: str
    salary: float=Field(gt=0,le=10000)

