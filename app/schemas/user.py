from pydantic import BaseModel
from typing import Optional
class User(BaseModel):
 name: Optional[str]
 email: Optional[str]
 username: str
 password: str
 