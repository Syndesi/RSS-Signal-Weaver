from typing import Literal

from pydantic import ConfigDict, BaseModel

from .relation import Relation

class OwnsData(BaseModel):
    model_config = ConfigDict(extra="allow")

class Owns(Relation):
    type: Literal["OWNS"]
    data: OwnsData
