from typing import Literal

from pydantic import BaseModel, ConfigDict

from .node import Node

class RssFeedData(BaseModel):
    name: str
    url: str

    model_config = ConfigDict(extra="allow")

class RssFeed(Node):
    type: Literal["RssFeed"]
    data: RssFeedData