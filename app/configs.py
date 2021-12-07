import json
from typing import TypedDict


class Config(TypedDict):
    urls: list[str]


def load(filename: str) -> Config:
    with open(filename) as config_file:
        config = json.load(config_file)
    return config
