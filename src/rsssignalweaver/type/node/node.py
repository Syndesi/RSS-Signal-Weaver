from typing import Any
from uuid import UUID

from pydantic import BaseModel


class Node(BaseModel):
    id: UUID
    type: str
    data: dict[str, Any]
