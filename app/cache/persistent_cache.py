from __future__ import annotations
import pickle
from typing import Generic, TypeVar

import sqlite3

from .supports_caching import SupportsCaching


CT = TypeVar("CT")


class PersistentCache(SupportsCaching, Generic[CT]):
    """A cache that perists in between app restarting"""

    def __init__(self, db_name: str = "items.db") -> None:
        self.database = db_name
        self._ensure_table_exists()

    def add(self, key, value) -> None:
        """Adds the value to the cache."""
        picked_value = pickle.dumps(value)
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO items (key, value) " "VALUES (?, ?)",
            (key, picked_value),
        )
        self.connection.commit()
        cursor.close()

    def head(self, key) -> CT:
        """
        Returns the most recently added value for the key.
        Raises KeyError if the key is not found.
        """
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT * " "FROM items " "WHERE key = ? " "ORDER BY added DESC ",
            # "LIMIT 1",
            (key,),
        )
        item = cursor.fetchone()
        cursor.close()
        if item is None:
            raise KeyError(key)
        return item

    def count(self, key) -> int:
        """Return the number of values stored for the key."""
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT COUNT(*) " "FROM items " "WHERE key = ?",
            (key,),
        )
        row_count: int = cursor.fetchone()[0]
        cursor.close()
        return row_count

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

    def __exit__(self, _, __, ___) -> None:
        """Close the underlying connection to the database"""
        self.connection.close()
