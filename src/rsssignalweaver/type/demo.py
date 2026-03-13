from typing import Literal
from pydantic import BaseModel


class Demo(BaseModel):
    type: Literal["demo"]
    name: str
    value: int
