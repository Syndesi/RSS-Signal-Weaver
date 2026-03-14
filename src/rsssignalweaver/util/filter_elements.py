from __future__ import annotations

from collections.abc import Iterable

from ..type import Element


def filter_elements[T: Element](items: Iterable[Element], cls: type[T]) -> list[T]:
	return [e for e in items if isinstance(e, cls)]
