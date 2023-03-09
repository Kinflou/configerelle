# Standard Imports
from dataclasses import dataclass

# Local Imports

# External Imports
from configerelle.configuration.base import ConfigBase


@dataclass
class Jess(ConfigBase):
    quotes: list[str]
    items: list[str]

