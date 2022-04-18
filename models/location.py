from typing import Optional

from pydantic.main import BaseModel


class Location(BaseModel):
    city: str
    state: Optional[str] = None
    country: str = 'US'
