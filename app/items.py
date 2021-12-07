from dataclasses import dataclass
from typing import Optional


@dataclass
class Item:
    item_id: str
    title: str
    price: int
    image_urls: Optional[list[str]] = None
