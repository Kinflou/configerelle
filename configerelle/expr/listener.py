# Standard Imports
from typing import Type

from antlr4 import TerminalNode, ParserRuleContext

# Local Imports
from configerelle.expr.generated.exprListener import exprListener
from configerelle.expr.generated.exprParser import exprParser

# External Imports
from flatdict import FlatDict


class ExprCombiner(exprListener):

    def __init__(self):
        super().__init__()

        self.current: str = 'root'
        self.indexes: dict = {}
        self.sections: FlatDict = FlatDict(delimiter='.')

    def next_idx(self, new) -> str:
        return self.current + '.' + new

    def parent_idx(self, child: str | None = None) -> str:
        if child:
            parts = child.split('.')
        else:
            parts = self.current.split('.')

        return '.'.join(parts[:-1])

    def last_idx(self, rule: Type[ParserRuleContext]) -> int:
        parent = self.parent_idx()
        name = rule.__name__
        val = self.sections[parent].get(name, None)

        if not val:
            return None

        vals = self.sections[parent][name]

        if not vals:
            return None

        return len(vals) - 1

    def last(self, rule) -> FlatDict | None:
        parent = self.parent_idx()
        name = rule.__name__
        val = self.sections[parent].get(name, None)

        if not val:
            return None

        vals = self.sections[parent][name]

        if not vals:
            return None

        return self.sections[parent][name][-1]

    def parent(self):
        return self.sections[self.parent_idx()]

    def enterExpressions(self, ctx: exprParser.ExpressionsContext):
        self.current = self.next_idx(exprParser.ExpressionsContext.__name__)
        self.sections[self.current] = {
            exprParser.ExpressionContext.__name__: []
        }
        ...

    def enterExpression(self, ctx: exprParser.ExpressionContext):
        self.current = self.next_idx(exprParser.ExpressionContext.__name__)
        self.sections[self.current].append({
            'text': [],
            exprParser.NamespaceContext.__name__: [],
            exprParser.Literal_namespaceContext.__name__: []
        })
        self.current = f'{self.current}.{self.last_idx(exprParser.ExpressionContext)}'
        ...

    def enterNamespace(self, ctx: exprParser.NamespaceContext):
        self.current = self.next_idx(exprParser.NamespaceContext.__name__)
        self.sections[self.current] = {
            exprParser.SegmentContext: []
        }
        ...

    def enterSegments(self, ctx: exprParser.SegmentsContext):
        self.current = self.next_idx(exprParser.SegmentsContext.__name__)
        self.sections[self.current] = {
            exprParser.SegmentContext: [],
            exprParser.SegmentsContext: []
        }
        ...

    def enterSegment(self, ctx: exprParser.SegmentContext):
        self.current = self.next_idx(exprParser.SegmentContext.__name__)
        self.sections[self.current] = {
            'text': [],
        }
        ...

    def enterLiteral_namespace(self, ctx: exprParser.Literal_namespaceContext):
        self.sections[self.current] = {
            'segments': [],
        }
        self.current = self.next_idx(exprParser.Literal_namespaceContext.__name__)
        ...

    def exitExpressions(self, ctx: exprParser.ExpressionsContext):
        self.current = self.parent_idx()
        ...

    def exitExpression(self, ctx: exprParser.ExpressionContext):
        texts = unite(ctx.TEXT())
        namespaces = unite(ctx.namespace())
        literal_namespaces = unite(ctx.literal_namespace())

        parent = self.parent_idx()
        last = len(self.sections[parent]) - 1
        self.sections[parent][last] = clean_values({
            'texts': texts,
            'namespaces': namespaces,
            'literal_namespaces': literal_namespaces
        })

        self.current = self.parent_idx()
        ...

    def exitNamespace(self, ctx: exprParser.NamespaceContext):
        segments = unite(ctx.segments())
        self.sections[self.current] = clean_values({
            'segments': segments
        })

        self.current = self.parent_idx()
        ...

    def exitSegments(self, ctx: exprParser.SegmentsContext):
        return

        segments = unite(ctx.segment())
        literal_namespaces = unite(ctx.literal_namespace())
        self.sections[self.current].update({
            'segments': segments,
            'literal_namespaces': literal_namespaces
        })

        self.current = self.parent_idx()
        ...

    def exitSegment(self, ctx: exprParser.SegmentContext):
        texts = unite(ctx.TEXT())
        self.sections[self.current] = clean_values({
            'texts': texts,
        })

        self.current = self.parent_idx()
        ...

    def exitLiteral_namespace(self, ctx: exprParser.Literal_namespaceContext):
        segments = unite(ctx.segments())
        self.sections[self.current] = clean_values({
            'segments': segments,
        })

        self.current = self.parent_idx()
        ...


def unite(node: TerminalNode):
    if not node:
        return []

    if isinstance(node, list):
        united = [n.getText() for n in node]
    else:
        united = [node.getText()]

    return united


def clean_values(dct: dict):
    new = dct.copy()

    for k, v in dct.items():
        if v is None or not v:
            del new[k]

    return new


