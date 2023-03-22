# Standard Imports
import platform
from pathlib import Path
from typing import TypeVar, ParamSpec, Callable, TYPE_CHECKING

# Local Imports
from configerelle.configuration.interpretation.abstration import Interpreter
from configerelle.configuration.interpretation import interpreter_nav

if TYPE_CHECKING:
    from configerelle.configuration.interpretation.binder import Binder

# External Imports


INTERPRETER: Interpreter = interpreter_nav.NavInterpreter

T = TypeVar('T', list, dict, str, int, float)
P = ParamSpec('P')


class ConfigBaseLogic:
    __custom: dict[str, dict] = {}
    __linked: dict[str, 'ConfigBaseLogic'] = {}
    __binder: 'Binder'

    def __post_init__(self):
        from configerelle.configuration.interpretation.binder import Binder
        self.__binder = Binder(INTERPRETER, self)

    def file_dir(self) -> Path | None:
        path = getattr(self, 'file_path', None)

        if path:
            return Path(path).parent

        return None

    def binder(self) -> 'Binder':
        return self.__binder

    def self_dict(self) -> dict:
        raise NotImplementedError

    def self_linked_dict(self) -> dict:
        shallow = self.self_dict().copy()
        shallow.update({
            'custom': self.__custom,
            'linked': self.linked_vars()
        })

        return shallow

    live_keywords: list[str] = [
        'std', 'cfg', 'file', 'custom', 'linked'
    ]

    def live_vars(self) -> dict:
        return {
            'std': {
                'system': platform.system().lower()
            },
            'cfg': self.self_dict(),
            'file': {
                'path': getattr(self, 'file_path', None),
                'dir': self.file_dir()
            },
            'custom': self.__custom,
            'linked': self.linked_vars()
        }

    def linked_vars(self) -> dict[str, Callable[[], dict]]:
        nested = {}

        for name, inner in self.__linked.items():
            nested[name] = inner

        return nested

    def link_config(self, name: str, config: 'ConfigBaseLogic'):
        self.__linked[name] = config

    def add_vars_group(self, group: dict):
        self.__custom.update(group)

    def var(self, points: str, default: str | list | dict | None = None, **kwargs) -> str | list | dict | None:
        sections = INTERPRETER().sections_from_expr(points)

        return self.__binder.var(sections.inner)

    def var_of(self, kind, expr: str, raise_lookup_fail: bool = True, **kwargs):
        pass

    def expr(self, expr: str, raise_lookup_fail: bool = True, **kwargs):
        sections = INTERPRETER().sections_from_expr(expr)
        return self.__binder.from_expr(sections.inner, raise_lookup_fail)

    def expr_of(self, kind, expr: str, raise_lookup_fail: bool = True, **kwargs):
        sections = INTERPRETER().sections_from_expr(expr)
        return self.__binder.from_expr_of(kind, sections.inner, raise_lookup_fail, **kwargs)

