
import pytest

from app.cache.in_memory_cache import InMemoryCache


def test__persistent_cache__add():
    # Act
    cache = InMemoryCache()
    cache.add("key", "value")
    
    # Assert
    actual = cache._data["key"]
    assert len(cache._data) == 1
    assert actual == ["value"]


def test__persistent_cache__count():
    # Arrange
    cache = InMemoryCache()
    cache._data["key"] = []
    cache._data["key"].append("value_1")
    cache._data["key"].append("value_2")

    # Act
    actual = cache.count("key")

    # Assert
    assert actual == 2


def test__persistent_cache__count_empty():
    # Act
    cache = InMemoryCache()
    actual = cache.count("key")

    # Assert
    assert actual == 0


def test__persistent_cache__head():
    # Arrange
    cache = InMemoryCache()
    cache._data["key"] = []
    cache._data["key"].append("value_1")
    cache._data["key"].append("value_2")

    # Act
    actual = cache.head("key")

    # Assert
    assert actual == "value_2"


def test__persistent_cache__head_empty():
    with pytest.raises(Exception):
        with InMemoryCache() as cache:
            actual = cache.head("key")
