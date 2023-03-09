# Standard Imports

# Local Imports
from configerelle.configuration.logic import ConfigBaseLogic

# External Imports


def check_sanity_of(config: ConfigBaseLogic) -> list[str]:
    missing: list[str] = []

    for items in config.self_dict():
        raise NotImplementedError

    return missing

