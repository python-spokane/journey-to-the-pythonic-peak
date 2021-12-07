from contextlib import contextmanager
import os
import sqlite3
from typing import Generator

import pytest

from app.cache.persistent_cache import PersistentCache


@contextmanager
def open_cursor() -> Generator[sqlite3.Cursor, None, None]:
    connection = sqlite3.connect("test.db")
    cursor = connection.cursor()
    yield cursor
    connection.commit()
    cursor.close()
    connection.close()


@pytest.fixture(scope="function")
def cache():
    db_name = "test.db"
    cache = PersistentCache(db_name = db_name)
    yield cache
    os.remove(db_name)
    assert not os.path.exists(db_name)


def test__persistent_cache__add(cache: PersistentCache):
    # Act
    with cache:
        cache.add("key", "value")
    
    # Assert
    with open_cursor() as cursor:
        cursor.execute("SELECT * FROM items")
        actual = cursor.fetchall()

    assert len(actual) == 1
    assert actual[0][0] == "key"


def test__persistent_cache__count(cache: PersistentCache):
    # Arrange
    with open_cursor() as cursor:
        cursor.execute(
            "INSERT INTO items (key, value) "
            "VALUES (?, ?)",
            ("key", "value_1")
        )
        cursor.execute(
            "INSERT INTO items (key, value) "
            "VALUES (?, ?)",
            ("key", "value_2")
        )

    # Act
    with cache:
        actual = cache.count("key")

    # Assert
    assert actual == 2


def test__persistent_cache__count_empty(cache: PersistentCache):
    # Act
    with cache:
        actual = cache.count("key")

    # Assert
    assert actual == 0


def test__peristent_cache__head(cache: PersistentCache):
    # Arrange
    with open_cursor() as cursor:
        cursor.execute(
            "INSERT INTO items (key, value) "
            "VALUES (?, ?)",
            ("key", "value_1")
        )
    with open_cursor() as cursor:
        cursor.execute(
            "INSERT INTO items (key, value) "
            "VALUES (?, ?)",
            ("key", "value_2")
        )

    # Act
    with cache:
        actual = cache.head("key")

    # Assert
    assert actual[0] == "key"
    assert actual[1] == "value_2"


def test__peristent_cache__head_empty(cache: PersistentCache):
    with pytest.raises(Exception):
        with cache:
            actual = cache.head("key")
