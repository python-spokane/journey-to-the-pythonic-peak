from __future__ import annotations
from contextlib import contextmanager
import pickle
from typing import Generator, Generic, TypeVar

import sqlite3

from .supports_caching import SupportsCaching


CT = TypeVar("CT")


class PersistentCache(SupportsCaching, Generic[CT]):
    """A cache that persists in between app restarting"""

    def __init__(self, db_name: str = "items.db") -> None:
        self.database = db_name
        self._ensure_table_exists()

    def add(self, key: str, value: CT) -> None:
        """Adds the value to the cache."""
        picked_value = pickle.dumps(value)
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO items (key, value) VALUES (?, ?)",
            (key, picked_value),
        )
        self.connection.commit()
        cursor.close()

    def head(self, key: str) -> CT:
        """
        Returns the most recently added value for the key.
        Raises KeyError if the key is not found.
        """
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT value FROM items WHERE key = ? ORDER BY added DESC",
            # "LIMIT 1",
            (key,),
        )
        cursor_value = cursor.fetchone()
        if cursor_value is None:
            raise KeyError(key)
        pickled_value = cursor_value[0]
        value: CT = pickle.loads(pickled_value)
        return value

    def count(self, key: str) -> int:
        """Return the number of values stored for the key."""
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT COUNT(*) FROM items WHERE key = ?",
            (key,),
        )
        row_count: int = cursor.fetchone()[0]
        cursor.close()
        return row_count

    def list(self) -> Generator[CT, None, None]:
        cursor = self.connection.cursor()
        cursor.execute("SELECT value FROM items")
        for row in cursor.fetchall():
            pickled_value = row[0]
            value: CT = pickle.loads(pickled_value)
            yield value

    def _ensure_table_exists(self) -> None:
        with self:
            cursor = self.connection.cursor()
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS items "
                "(key TEXT, value BLOB, added DATETIME DEFAULT(STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW')))"
            )
            self.connection.commit()
            cursor.close()

    def __enter__(self) -> PersistentCache:
        """Open the underlying connection to the database"""
        self.connection = sqlite3.connect(self.database)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:
        """Close the underlying connection to the database"""
        self.connection.close()
