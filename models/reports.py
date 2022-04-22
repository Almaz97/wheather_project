import datetime
from typing import Optional

from pydantic.main import BaseModel

from models.location import Location


class Report(BaseModel):
    description: str
    location: Location
    created_date: Optional[datetime.datetime]
