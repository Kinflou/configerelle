# Standard Imports
from dataclasses import dataclass, field


# Local Imports

# External Imports


@dataclass
class Namespace:
    segments: list[str] = field(default_factory=list)


@dataclass
class LiteralNamespace:
    segments: list[str] = field(default_factory=list)


@dataclass
class Expression:
    texts: list[str] = field(default_factory=list)
    namespaces: list[Namespace] = field(default_factory=list)
    literal_namespaces: list[LiteralNamespace] = field(default_factory=list)


@dataclass
class Root:
    expressions: list[Expression] = field(default_factory=list)


if __name__ == '__main__':
    root = Root(
        expressions=[
            Expression(texts=['some']),
            Expression()
        ]
    )

    ...

