# Standard Imports
import typing
from pathlib import Path
import inspect

# Local Imports
from configerelle.configuration.logic import ConfigBaseLogic

# External Imports
import attrs
import cattrs
import yaml


@attrs.define(order=True, init=True, kw_only=False)
class ConfigBase(ConfigBaseLogic):

    # __custom: dict[str, dict] = attrs.field(default=dict())
    # __linked: dict[str, 'ConfigBase'] = attrs.field(default=dict())

    def __post_init__(self):
        super().__post_init__()

    def self_dict(self) -> dict:
        fields = {
            'custom': self._ConfigBaseLogic__custom,
            'linked': self._ConfigBaseLogic__linked
        }

        for i in inspect.getmembers(self):
            name = i[0]
            if not name.startswith('_'):
                if not inspect.ismethod(i[1]):
                    fields[name] = getattr(self, name)

        return fields

    @classmethod
    def from_path(cls, path: Path) -> typing.Self:
        content = path.read_text()

        match path.suffix:
            case '.yml':
                return from_yaml(cls, content, path)
            case _:
                raise NotImplementedError(f'{cls.__name__} file format {path.suffix} is not supported ')


def from_yaml(kind, content: str, path: Path):
    content_dct = yaml.safe_load(content)

    cattrs.register_structure_hook(
        Path,
        lambda d, t: d
    )

    instance = cattrs.structure(content_dct, kind)
    instance.__post_init__()

    return instance
