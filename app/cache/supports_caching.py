from typing import Protocol, TypeVar


CT = TypeVar("CT", covariant=True)


class SupportsCaching(Protocol[CT]):
    def add(self, key, value) -> None:
        ...

    def head(self, key) -> CT:
        ...

    def count(self, key) -> int:
        ...
