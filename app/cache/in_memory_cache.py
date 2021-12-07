from typing import Generic, TypeVar

from .supports_caching import SupportsCaching


CT = TypeVar("CT")


class InMemoryCache(SupportsCaching, Generic[CT]):
    """A cache that does not persists in between app restarting"""

    _data: dict[str, list[CT]] = {}

    def __init__(self) -> None:
        self._data = {}

    def add(self, key: str, value: CT) -> None:
        """Adds the value to the cache."""
        self._data.setdefault(key, [])
        self._data[key].append(value)

    def head(self, key: str) -> CT:
        """
        Returns the most recently added value for the key.
        Raises KeyError if the key is not found.
        """
        return self._data[key][-1]

    def count(self, key: str) -> int:
        """Return the number of values stored for the key."""
        try:
            count = len(self._data[key])
        except KeyError:
            count = 0
        return count

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass
