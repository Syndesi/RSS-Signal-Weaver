from typing import Any
from uuid import UUID

from pydantic import BaseModel


class Relation(BaseModel):
    id: UUID
    type: str
    start: UUID
    end: UUID
    data: dict[str, Any]
