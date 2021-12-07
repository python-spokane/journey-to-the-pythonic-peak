import argparse
from dataclasses import dataclass
from typing import Literal, Union


@dataclass
class CliArgs:
    perist: bool
    filename: str
    wait: float
    loglevel: Union[
        Literal["CRITICAL"],
        Literal["ERROR"],
        Literal["WARNING"],
        Literal["INFO"],
        Literal["DEBUG"],
    ]


def parse() -> CliArgs:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--perist",
        action="store_true",
    )
    parser.add_argument(
        "-f",
        "--filename",
        default="config.json",
    )
    parser.add_argument(
        "-w",
        "--wait",
        type=float,
        default=5.0,
    )
    parser.add_argument(
        "-l",
        "--loglevel",
        default="WARNING",
        help="Provide logging level. Example --loglevel DEBUG, default=WARNING",
    )
    cli_args = CliArgs(**vars(parser.parse_args()))
    return cli_args
