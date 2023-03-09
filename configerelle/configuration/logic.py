# Standard Imports
import ast
import re
import platform
from pathlib import Path
from typing import TypeVar, ParamSpec, Callable

# Local Imports

# External Imports


T = TypeVar('T', list, dict, str, int, float)
P = ParamSpec('P')


class ConfigBaseLogic:
    __custom: dict[str, dict] = {}
    __linked: dict[str, 'ConfigBaseLogic'] = {}

    def file_dir(self) -> Path | None:
        path = getattr(self, 'file_path', None)

        if path:
            return Path(path).parent

        return None

    def self_dict(self) -> dict:
        raise NotImplementedError

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

    def linked_vars(self) -> dict[str, dict]:
        nested = {}

        for name, inner in self.__linked.items():
            nested[name] = inner.__dict__

        return nested

    def link_config(self, name: str, config: 'ConfigBaseLogic'):
        self.__linked[name] = config

    def add_vars_group(self, group: dict):
        self.__custom.update(group)

    @staticmethod
    def namespace_of(name: str) -> list[str]:
        names = name.split('::')
        return names

    @staticmethod
    def has_expr(potential_expr: str) -> bool:
        regex = re.compile(r".+?::.+?")
        return regex.match(potential_expr) is not None

    def expr(self, expression: str, fail_on_lookup: bool = False, **kwargs):
        regex = re.compile(r"{(.+?)}")

        result = expression
        for _, match in enumerate(regex.finditer(expression), start=1):
            val = self.var(match.group(1), **kwargs)

            if val:
                result = regex.sub(str(val), result, 1)
            else:
                if fail_on_lookup:
                    raise ValueError(f"Variable '{match.group(1)}' not found in configuration")

                result = regex.sub('', result, 1)

        return result

    @staticmethod
    def segments_of(expr: str) -> list[str]:
        regex = re.compile(r"\{([^}]*)\}|([^{]*)")

        segments = []
        for n, match in enumerate(regex.finditer(expr), start=1):
            record = match.group(1)

            if not record:
                r = match.group(0)

                if r:
                    segments.append(r)

            if record:
                segments.append(record)

        return segments

    def var(self, name: str, default: str | list | dict | None = None, **kwargs) -> str | list | dict | None:
        names = self.namespace_of(name)

        inner: dict = self.live_vars()
        inner['local'] = kwargs

        index = 0
        while True:
            val: str | list | dict | None = inner.get(names[index], default)

            if index + 1 == len(names):
                if isinstance(val, str):
                    if self.has_expr(val):
                        return self.expr(val, **kwargs)

                return val

            if callable(val):
                return val()

            elif not isinstance(val, dict):
                return val

            inner = val
            index += 1

    def var_from_namespace_segments(self, segments: list[str], variables: dict, default: None = None, **kwargs):
        idx: int = 0
        inner = variables

        while True:
            segment = segments[idx]

            if inner is None:
                break

            if "#" in segment:
                if not isinstance(inner, list):
                    raise TypeError()

                pos = segment.replace('#', '')

                if not pos.isdecimal():
                    raise ValueError()

                pos = int(pos)

                if pos >= len(inner):
                    raise IndexError(
                        f'Tried to get value for index {pos} but length is {len(inner)}, available values are:'
                        f'\n - {"".join(inner)}'
                    )

                inner = inner[int(pos)]
            else:
                inner = inner.get(segment, default)

            if callable(inner):
                inner = inner()

            if idx + 1 >= len(segments):
                if isinstance(inner, str):
                    if self.has_expr(inner):
                        return self.from_expr(inner, variables, **kwargs)

                break

            if not isinstance(inner, dict):
                halt = True
                if idx + 1 > len(segments) and halt:
                    raise NotImplementedError()

            idx += 1

        return inner

    def from_expr(self, expr: str, default: object | None = None, **kwargs) -> list[object] | None:
        variables: dict = self.live_vars()
        variables['local'] = kwargs

        segments = self.segments_of(expr)
        result = []

        for segment in segments:
            if self.has_expr(segment):
                namespace_segments = self.namespace_of(segment)
                var = self.var_from_namespace_segments(namespace_segments, variables, default)
            else:
                var = segment

            if not var:
                raise AttributeError(f"Segment '{segment}' is none")

            if isinstance(var, list):
                result += var
            else:
                result.append(var)

        return result

    def expr_of(self, kind: Callable[P, T], expr: str, default: str | None = None) -> str | None:
        vals = self.from_expr(expr)

        if not vals:
            return default

        if kind is dict:
            whole = {}
            for val in vals:
                whole |= val

        elif kind == list:
            whole = []
            for val in vals:
                whole.append(val)

        elif kind == str:
            whole = ''.join(vals)

        elif kind == int or float:
            whole = 0
            for val in vals:
                whole += val

        else:
            whole = []
            for val in vals:
                whole.append(val)

        return whole

    def eval_vars_of(self, kind: Callable[P, T], expr: str, default: object | None = None) -> Callable[P, T] | None:
        val = self.from_expr(expr, default)
        val = ''.join(val)
        result = ast.literal_eval(val)

        return kind(result)

    def var_of(self, kind: Callable[P, T], expr: str, default: object | None = None) -> Callable[P, T] | None:
        val = self.from_expr(expr)[0]

        if not isinstance(val, kind):
            return default

        return val
