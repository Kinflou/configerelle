# Standard Imports
from dataclasses import dataclass
from pathlib import Path

# Local Imports
from configerelle.configuration.logic import ConfigBaseLogic

# External Imports
import yaml
import cattrs


@dataclass(order=True, init=True, kw_only=False)
class ConfigBase(ConfigBaseLogic):

    # __custom: dict[str, dict] = field(default_factory=dict)
    # __linked: dict[str, 'ConfigBase'] = field(default_factory=dict)

    def __post_init__(self):
        super().__post_init__()

    def self_dict(self) -> dict:
        return self.__dict__

    @classmethod
    def from_path(cls, path: Path):
        content = path.read_text()

        match path.suffix:
            case '.yml':
                return from_yaml(cls, content, path)
            case _:
                raise NotImplementedError(f'{cls.__name__} file format {path.suffix} is not supported ')


def from_yaml(kind, content: str, path: Path):
    content_dct = yaml.safe_load(content)
    content_dct['file_path'] = path

    cattrs.register_structure_hook(
        Path,
        lambda d, t: d
    )

    return cattrs.structure(content_dct, kind)
