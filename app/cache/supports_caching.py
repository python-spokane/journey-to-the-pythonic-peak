from __future__ import annotations
from typing import Protocol, TypeVar


CT = TypeVar("CT", covariant=True)


class SupportsCaching(Protocol[CT]):
    def add(self, key, value) -> None:
        ...

    def head(self, key) -> CT:
        ...

    def count(self, key) -> int:
        ...

    def __enter__(self) -> SupportsCaching:
        ...

    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:
        ...
