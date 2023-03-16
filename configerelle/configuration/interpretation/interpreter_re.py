# Standard Imports
import re

# Local Imports
from configerelle.configuration.interpretation.abstration import Interpreter
from configerelle.utils.navigator import Navigator


# External Imports


class RegexInterpreter(Interpreter):

    def namespace_of(name: str) -> list[str]:
        names = name.split('::')
        return names

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

    def sections_from_expr(self, expression: str) -> Navigator:
        ...


def has_expr(potential_expr: str) -> bool:
    regex = re.compile(r".+?::.+?")
    return regex.match(potential_expr) is not None
