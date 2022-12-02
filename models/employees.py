from typing import Optional
from pydantic import BaseModel


class Employee(BaseModel):
    id: Optional[int]
    first_name: str
    last_name: str
    phone: int
    login: str
    mail: str
    title_id: int
    password: str
