# Standard Imports
from dataclasses import dataclass

# Local Imports

# External Imports
from configerelle.configuration.base import ConfigBase


@dataclass
class Ali(ConfigBase):
    friends: list
