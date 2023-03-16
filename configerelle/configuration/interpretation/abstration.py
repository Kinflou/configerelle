# Standard Imports
from typing import Protocol

# Local Imports
from configerelle.utils.navigator import Navigator

# External Imports


class Interpreter(Protocol):

    def sections_from_expr(self, expression: str) -> Navigator:
        ...

