from dataclasses import dataclass
from typing import List


@dataclass(slots=True)
class Config:
    feeds: List[str]


@dataclass(slots=True)
class Article:
    title: str
    content: str
    language: str | None = None


@dataclass(slots=True)
class LanguageBatch:
    language: str
    articles: List[Article]
