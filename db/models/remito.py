from pydantic import BaseModel
from datetime import datetime

class Device(BaseModel):
    description: str 
    quantity: int

class Remito(BaseModel):   
    id: str | None 
    number: int
    date: str
    from_workshop: str
    to_workshop: str
    user: str
    devices: list[Device] 

class Date(BaseModel):
    date_strt: str
    date_end: str


   