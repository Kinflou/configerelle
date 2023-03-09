# Standard Imports

# Local Imports
from configerelle.configuration.logic import ConfigBaseLogic

# External Imports
import attrs


@attrs.define(order=True, init=True, kw_only=False)
class ConfigBase(ConfigBaseLogic):

    # __custom: dict[str, dict] = attrs.field(default=dict())
    # __linked: dict[str, 'ConfigBase'] = attrs.field(default=dict())

    def self_dict(self) -> dict:
        return self.__dict__

