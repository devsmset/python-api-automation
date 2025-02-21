from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
    gender: str
    status: str

