from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None

class AdjectiveCreate(BaseModel):
    title: str

class ProjectCreate(BaseModel):
    slug: str
    user_id: int

class FeedBackCreate(BaseModel):
    user_id: int
    project_id: int
