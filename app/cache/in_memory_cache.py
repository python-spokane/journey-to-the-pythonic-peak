from typing import Generic, TypeVar

from .supports_caching import SupportsCaching


CT = TypeVar("CT")


class InMemoryCache(SupportsCaching, Generic[CT]):
    """A cache that does not perists in between app restarting"""

    _data: dict[str, list[CT]] = {}

    def __init__(self) -> None:
        self._data = {}

    def add(self, key, value) -> None:
        """Adds the value to the cache."""
        self._data.setdefault(key, [])
        self._data[key].append(value)

    def head(self, key) -> CT:
        """
        Returns the most recently added value for the key.
        Raises KeyError if the key is not found.
        """
        return self._data[key][-1]

    def count(self, key) -> int:
        """Return the number of values stored for the key."""
        try:
            count = len(self._data[key])
        except KeyError:
            count = 0
        return count

    def __enter__(self):
        return self

    def __exit__(self, _, __, ___):
        pass
