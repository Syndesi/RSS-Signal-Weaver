from __future__ import annotations

from collections.abc import Iterable
from typing import TypeVar, Type

from ..type import Element

T = TypeVar('T', bound=Element)


def filter_elements(items: Iterable[Element], cls: Type[T]) -> list[T]:
	return [e for e in items if isinstance(e, cls)]
