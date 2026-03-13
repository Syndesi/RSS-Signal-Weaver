from typing import TypeVar, Type, Iterable
from ..type import Element

T = TypeVar("T")

def filter_elements(items: Iterable[Element], cls: Type[T]) -> list[T]:
    return [e for e in items if isinstance(e, cls)]
