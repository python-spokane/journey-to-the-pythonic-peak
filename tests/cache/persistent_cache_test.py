from contextlib import contextmanager
import os
import sqlite3
from typing import Generator

import pytest

from app.cache.persistent_cache import PersistentCache
from app.items import Item


@contextmanager
def open_cursor() -> Generator[sqlite3.Cursor, None, None]:
    connection = sqlite3.connect("test.db")
    cursor = connection.cursor()
    yield cursor
    connection.commit()
    cursor.close()
    connection.close()


@pytest.fixture(scope="module", autouse=True)
def verify_cache_removed():
    db_name = "test.db"
    if os.path.exists(db_name):
        os.remove(db_name)
    yield
    if os.path.exists(db_name):
        os.remove(db_name)


@pytest.fixture(scope="function")
def cache():
    db_name = "test.db"
    cache = PersistentCache(db_name = db_name)
    yield cache
    os.remove(db_name)
    assert not os.path.exists(db_name)


def test__persistent_cache__add(cache: PersistentCache[Item]):
    # Act
    item = Item("key", "title", 1)
    with cache:
        cache.add(item.item_id, item)
    
    # Assert
    with open_cursor() as cursor:
        cursor.execute("SELECT * FROM items")
        actual = cursor.fetchall()

    assert len(actual) == 1
    assert actual[0][0] == "key"


def test__persistent_cache__count(cache: PersistentCache[Item]):
    # Arrange
    item = Item("key", "value_1", 1)
    with cache:
        cache.add(item.item_id, item)
    item.title = "value_2"
    with cache:
        cache.add(item.item_id, item)

    # Act
    with cache:
        actual = cache.count("key")

    # Assert
    assert actual == 2


def test__persistent_cache__count_empty(cache: PersistentCache[Item]):
    # Act
    with cache:
        actual = cache.count("key")

    # Assert
    assert actual == 0


def test__persistent_cache__head(cache: PersistentCache[Item]):
    # Arrange
    item = Item("key", "value_1", 1)
    with cache:
        cache.add(item.item_id, item)
    item.title = "value_2"
    with cache:
        cache.add(item.item_id, item)

    # Act
    with cache:
        actual = cache.head("key")

    # Assert
    assert isinstance(actual, Item)
    assert actual.item_id == "key"
    assert actual.title == "value_2"


def test__persistent_cache__head_empty(cache: PersistentCache[Item]):
    with pytest.raises(Exception):
        with cache:
            cache.head("key")


def test__persistent_cache__list(cache: PersistentCache[Item]):
    # Arrange
    item = Item("key", "value_1", 1)
    with cache:
        cache.add(item.item_id, item)
    item.title = "value_2"
    with cache:
        cache.add(item.item_id, item)

    # Act
    with cache:
        actual = list(cache.list())

    # Assert
    assert len(actual) == 2
    assert set([item.title for item in actual]) == {"value_1", "value_2"}
