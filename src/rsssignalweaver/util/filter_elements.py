from __future__ import annotations

from typing import Iterable, TypeVar

from ..type import Element

T = TypeVar("T")

def filter_elements(items: Iterable[Element], cls: type[T]) -> list[T]:
    return [e for e in items if isinstance(e, cls)]
