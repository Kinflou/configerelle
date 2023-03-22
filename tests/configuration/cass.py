# Standard Imports
from dataclasses import dataclass, field

# Local Imports

# External Imports
from configerelle.configuration.base import ConfigBase


@dataclass
class Cass(ConfigBase):
    quotes: list[str]
    items: list[str]
    dreams: list[str] = field(default_factory=list)

