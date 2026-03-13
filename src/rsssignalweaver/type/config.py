from dataclasses import dataclass
from typing import List


@dataclass(slots=True)
class Config:
    feeds: List[str]