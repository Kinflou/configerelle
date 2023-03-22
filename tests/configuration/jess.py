# Standard Imports
from dataclasses import dataclass, field

# Local Imports

# External Imports
from configerelle.configuration.base import ConfigBase


@dataclass
class Jess(ConfigBase):
    quotes: list[str]
    items: list[str]
    dreams: dict = field(default_factory=dict)
    missing: list[str] = field(default_factory=list)

