import click
from .query import Query as Query
from .tool import BowlerTool as BowlerTool
from .types import START as START, SYMBOL as SYMBOL, TOKEN as TOKEN
from typing import List

def main(ctx: click.Context, debug: bool, version: bool) -> None: ...
def dump(selector_pattern: bool, paths: List[str]) -> None: ...
def do(interactive: bool, query: str, paths: List[str]) -> None: ...
def run(codemod: str, argv: List[str]) -> None: ...
def test(codemod: str) -> None: ...
