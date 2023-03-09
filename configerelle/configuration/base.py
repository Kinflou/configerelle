# Standard Imports
from dataclasses import dataclass

# Local Imports
from configerelle.configuration.logic import ConfigBaseLogic

# External Imports


@dataclass(order=True, init=True, kw_only=False)
class ConfigBase(ConfigBaseLogic):

    # __custom: dict[str, dict] = field(default_factory=dict)
    # __linked: dict[str, 'ConfigBase'] = field(default_factory=dict)

    def self_dict(self) -> dict:
        return self.__dict__

