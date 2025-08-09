from typing import Optional

from pydantic import BaseModel
from typing import Optional

class Person(BaseModel):
    name: str
    age: int
    city: str
    salary :Optional[float]=None
    isActive :Optional[bool]=True


person = Person(name="dog" ,age=35.5, city="Chicago" , salary=1234563232)

try:
    print(person)
    print(type(person))
except ValueError as e:
    print(e)

