# Standard Imports
import functools
from typing import TYPE_CHECKING, Callable

# Local Imports
from configerelle.expr.generated.exprParser import exprParser
from configerelle.configuration.interpretation import interpreter_re
from configerelle.configuration.exceptions import SegmentNotFoundError

if TYPE_CHECKING:
    from configerelle.configuration.logic import ConfigBaseLogic


# External Imports


class Binder:

    def __init__(self, interpreter_type, config: 'ConfigBaseLogic'):
        self.interpreter_type = interpreter_type
        self.config = config

    """
    def var(self, segments: list[str], default=None, raise_lookup_fail: bool = True, **kwargs):
        inner: dict | list | str | Callable = self.config.live_vars()
        inner['local'] = kwargs

        idx: int = 0
        while True:
            segment = segments[idx]

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

            elif isinstance(inner, str):
                if has_expr(inner):
                    return self.config.from_expr(inner, **kwargs)

            else:
                inner = inner.get(segment, default)

            if callable(inner):
                inner = inner()

            if inner is None:
                if raise_lookup_fail:
                    raise SegmentNotFoundError(segment, segments[:idx])

                return None

            if idx + 1 >= len(segments):
                if isinstance(inner, str):
                    if has_expr(inner):
                        return self.config.from_expr(inner, **kwargs)

                break

            if not isinstance(inner, dict):
                halt = True
                if idx + 1 > len(segments) and halt:
                    raise NotImplementedError()

            idx += 1

        return inner
    """

    def var(self, segments: list[str], default=None, raise_lookup_fail: bool = True, **kwargs):
        from configerelle.configuration.logic import ConfigBaseLogic

        inner: dict | list | str | Callable | ConfigBaseLogic = self.config.live_vars()
        inner['local'] = kwargs

        idx: int = 0
        while True:
            segment = segments[idx]

            if "#" in segment:
                if not isinstance(inner, list):
                    raise TypeError(f"Tried to index using '{segment}' on non-list type '{type(inner).__name__}'")

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

            elif isinstance(inner, str):
                if has_expr(inner):
                    inner = self.config.expr(inner, **kwargs)

                    if idx + 1 >= len(segments):
                        inner = inner[0]
                        idx -= 1

            else:
                if segment not in inner:
                    if raise_lookup_fail:
                        raise SegmentNotFoundError(segment, segments[:idx])

                    return None

                inner = inner.get(segment, default)

            if callable(inner):
                inner = inner()

            if isinstance(inner, ConfigBaseLogic):
                routed = segments[idx + 1:]

                if len(routed) < 1:
                    break

                if routed[0] not in self.config.reserved_keywords:
                    routed.insert(0, 'cfg')

                inner = inner.binder().var(routed)

                break

            if idx + 1 >= len(segments):
                if isinstance(inner, str):
                    if has_expr(inner):
                        return self.config.expr(inner, **kwargs)

                break

            idx += 1

        return inner

    def var_of(self, kind, expr_sections: dict, default: object | None = None):
        ...

    def from_expr_of(self, kind, expr_sections: dict, raise_lookup_fail: bool = True, **kwargs):
        parts = self.from_inner(expr_sections, raise_lookup_fail, **kwargs)
        return expr_of_kind(kind, parts)

    def from_expr(self, expr_sections: dict, raise_lookup_fail: bool = True, **kwargs):
        parts = self.from_inner(expr_sections, raise_lookup_fail, **kwargs)
        return parts

    def from_inner(self, inner: dict, raise_lookup_fail: bool = True, **kwargs) -> list:
        recurse = functools.partial(
            self.from_inner, raise_lookup_fail=raise_lookup_fail, **kwargs
        )

        values = []

        current = inner
        while True:
            for k, section in current.items():
                if k == exprParser.ExpressionsContext.__name__:
                    for expression in section:
                        values.extend(recurse(expression))

                elif k == exprParser.NamespaceContext.__name__:
                    values.extend(recurse(section))

                elif k == exprParser.SegmentsContext.__name__:
                    for segment in section:
                        segments: list[str] = segment['texts']

                        if exprParser.Literal_namespaceContext.__name__ in segment:
                            if segment[exprParser.Literal_namespaceContext.__name__]:
                                solved_literals = []

                                for literal in segment[exprParser.Literal_namespaceContext.__name__]:
                                    solved_literals.extend(recurse(literal))

                                ordered = segments

                                idx = 0
                                for index in segment['positions']:
                                    ordered.insert(index, solved_literals[idx])
                                    idx += 1

                                segments = ordered

                        var = self.var(segments, raise_lookup_fail=raise_lookup_fail, **kwargs)

                        # TODO: Be sure that ignoring null is the correct choice of flow
                        if var:
                            if isinstance(var, list):
                                values.extend(var)
                            else:
                                values.append(var)

                elif k == exprParser.Literal_namespaceContext.__name__:
                    var = recurse(section)
                    values.extend(var)

                elif k == 'texts':
                    values.extend(section)

            break

        return values


def has_expr(maybe_expr: str) -> bool:
    return interpreter_re.has_expr(maybe_expr)


def expr_of_kind(kind, parts, default: str | None = None):
    if not parts:
        return default

    if kind is dict:
        whole = {}
        for part in parts:
            whole |= part

    elif kind == list:
        whole = parts

    elif kind == str:
        whole = ''.join(parts)

    elif kind == int or kind == float:
        whole = sum(parts)

    else:
        whole = parts[0]

    return whole


"""

    def from_expr(self, expr_sections: dict, default: object | None = None, **kwargs) -> list | None:
        variables: dict = self.config.live_vars()
        variables['local'] = kwargs

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
"""

