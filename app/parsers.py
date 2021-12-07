import re
from typing import Union

import bs4
import bs4.element

from .items import Item


class Parser:
    def parse_items(self, text: str) -> list[Item]:
        soup = bs4.BeautifulSoup(text, "html.parser")
        items: list[Item] = []
        results: bs4.element.ResultSet[bs4.element.Tag] = soup.find_all(
            "li", class_="result-row"
        )
        for result in results:
            element_id = result["data-pid"]
            if isinstance(element_id, list):
                raise ValueError(f"Unable to parse element_id from: {element_id}")
            title_element = self._find_element(result, ".result-title")
            price_element = self._find_element(result, ".result-price")
            image_container_element = self._find_element(result, ".result-image")
            title = title_element.text
            price = self._parse_price(price_element.text)
            image_urls = self._parse_image_urls(image_container_element)
            item = Item(
                element_id,
                title,
                price,
                image_urls=image_urls,
            )
            items.append(item)
        return items

    def _find_element(
        self, soup: Union[bs4.BeautifulSoup, bs4.element.Tag], selector: str, **kwargs
    ):
        """Find an element in the soup using the selector"""
        element = soup.select_one(selector, **kwargs)
        if element is None:
            raise ValueError(f"No element with selector={selector} found.")
        return element

    def _parse_price(self, text: str) -> int:
        """Parse the price from the passed-in text"""
        price_match = re.match(r"\$(\d+)", text)
        if price_match is None:
            raise ValueError(f"Could not parse result_price from text={text}")
        price = int(price_match.groups()[0])
        return price

    def _parse_image_urls(self, tag: bs4.element.Tag) -> list[str]:
        """Parse the image URLs from the passed-in soup element"""
        image_ids = tag["data-ids"]
        if isinstance(image_ids, str):
            image_ids = image_ids.split(",")
        image_ids = [re.sub(r"\d:", "", image_id) for image_id in image_ids]
        image_urls = [
            f"https://images.craigslist.org/{data_id}_300x300.jpg"
            for data_id in image_ids
        ]
        return image_urls
