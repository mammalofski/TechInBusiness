from pydantic import BaseModel, EmailStr
from typing import Optional

class ContactForm(BaseModel):
    name: str
    email: EmailStr
    company: Optional[str] = None
    service: str
    message: str