import itertools
import logging

from . import cli, configs
from .cache.in_memory_cache import InMemoryCache
from .cache.persistent_cache import PersistentCache
from .item_service import ItemService
from .parsers import Parser


def main():
    cli_args = cli.parse()

    if cli_args.perist:
        cache = PersistentCache()
    else:
        cache = InMemoryCache()

    config = configs.load(cli_args.filename)
    urls = config["urls"]

    logger = logging.getLogger(ItemService.__name__)
    logger.setLevel(cli_args.loglevel)
    logger.addHandler(logging.StreamHandler())

    parser = Parser()
    item_service = ItemService(
        parser=parser,
        cache=cache,
        logger=logger,
    )

    item_generator = item_service.start(cli_args.wait)
    for url in itertools.cycle(urls):
        item_generator.send(url)
