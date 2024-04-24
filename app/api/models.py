from pydantic import BaseModel
from typing import List, Optional


class CompanyIn(BaseModel):
    name: str
    description: str
    staff: str
    age: str
    engineer_id: List[int]


class CompanyOut(CompanyIn):
    id: int


class ArtistUpdate(CompanyIn):
    name: Optional[str] = None
    description: Optional[str] = None
    staff: Optional[str] = None
    age: Optional[str] = None
    engineer_id: Optional[List[int]] = None