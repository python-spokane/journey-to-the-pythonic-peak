import argparse
from dataclasses import dataclass
from typing import Literal, Union


@dataclass
class CliArgs:
    persist: bool
    filename: str
    wait: float
    loglevel: Union[
        Literal["CRITICAL"],
        Literal["ERROR"],
        Literal["WARNING"],
        Literal["INFO"],
        Literal["DEBUG"],
    ]
    command: Union[None, Literal["ls"]]


def parse() -> CliArgs:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--persist",
        action="store_true",
        help="Set to persist results in local database. Defaults to false.",
    )
    parser.add_argument(
        "-f",
        "--filename",
        default="config.json",
        help="Filename to look for configuration in.",
    )
    parser.add_argument(
        "-w",
        "--wait",
        type=float,
        default=5.0,
        help="How long to wait in between HTTP requests.",
    )
    parser.add_argument(
        "-l",
        "--loglevel",
        default="DEBUG",
        help="Provide logging level. Example --loglevel DEBUG",
    )
    subparser = parser.add_subparsers(dest="command")
    subparser.add_parser("ls")
    cli_args = CliArgs(**vars(parser.parse_args()))
    return cli_args
