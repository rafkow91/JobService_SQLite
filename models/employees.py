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

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return f'{self.id} - {self.first_name} {self.last_name} ({self.title_id})'