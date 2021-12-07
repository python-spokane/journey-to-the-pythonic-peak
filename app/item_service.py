import logging
import time
from typing import Generator, Optional

import requests

from .cache.supports_caching import SupportsCaching
from .items import Item
from .parsers import Parser


# See: https://dabeaz.com/coroutines/
def coroutine(func):
    def start(*args, **kwargs):
        coroutine = func(*args, **kwargs)
        next(coroutine)
        return coroutine

    return start


class ItemService:
    def __init__(
        self,
        parser: Parser,
        cache: SupportsCaching,
        logger: Optional[logging.Logger] = None,
    ) -> None:
        self._parser = parser
        self._cache = cache
        self._logger = logger or logging.getLogger(ItemService.__name__)

    @coroutine
    def start(self, wait: float) -> Generator[None, str, None]:
        """
        Parses and updates items, while waiting `wait` seconds in-between URLs.
        Returns a Generator for URLs to be sent to.
        """
        while True:
            url = yield
            response = requests.get(url)
            response.raise_for_status()
            items = self._parser.parse_items(response.text)
            self._logger.debug(f"Found {len(items)} items")
            for item in items:
                self.update_item(item)

            self._logger.debug(f"Sleeping for {wait} seconds...")
            time.sleep(wait)

    def update_items(self, text: str) -> None:
        """Updates multiple items after parsing from text"""
        items = self._parser.parse_items(text)
        for item in items:
            self.update_item(item)

    def update_item(self, item: Item) -> int:
        """Upserts the item in the cache only if it is new or has been updated."""
        item_id = item.item_id
        with self._cache:
            try:
                head = self._cache.head(item_id)
            except KeyError:
                self._cache.add(item_id, item)
            else:
                # Only add item if it has been updated
                if head != item:
                    item_count = self._cache.add(item_id, item)
            item_count = self._cache.count(item_id)
        return item_count
