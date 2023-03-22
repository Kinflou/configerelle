# Standard Imports
from antlr4.tree.Tree import TerminalNodeImpl

# Local Imports
from configerelle.expr.generated.exprListener import exprListener
from configerelle.expr.generated.exprParser import exprParser
from configerelle.utils.navigator import Navigator

# External Imports
from antlr4 import TerminalNode


class ExprCombiner(exprListener):

    def __init__(self):
        super().__init__()

        self.sections: Navigator = Navigator(value={})

    def enterExpressions(self, ctx: exprParser.ExpressionsContext):
        self.sections.next(exprParser.ExpressionsContext.__name__)
        self.sections.current_item = []
        ...

    def enterExpression(self, ctx: exprParser.ExpressionContext):
        self.sections.current_item.append({
            'texts': [],
            exprParser.NamespaceContext.__name__: [],
        })

        self.sections.current_index = self.sections.last()
        ...

    def enterNamespace(self, ctx: exprParser.NamespaceContext):
        self.sections.next(exprParser.NamespaceContext.__name__)

        self.sections.current_item = {
            exprParser.SegmentsContext.__name__: []
        }
        ...

    def enterSegments(self, ctx: exprParser.SegmentsContext):
        self.sections.next(exprParser.SegmentsContext.__name__)

        self.sections.current_item.append({
            'texts': [],
            exprParser.Literal_namespaceContext.__name__: []
        })

        self.sections.current_index = self.sections.last()
        ...

    def enterLiteral_namespace(self, ctx: exprParser.Literal_namespaceContext):
        self.sections.next(exprParser.Literal_namespaceContext.__name__)

        positions = []
        pos = 0
        for idx in range(len(ctx.parentCtx.children)):
            child = ctx.parentCtx.children[idx]

            if isinstance(child, TerminalNodeImpl):
                if child.getText() == '::':
                    pos += 1

            elif isinstance(child, exprParser.Literal_namespaceContext):
                positions.append(pos)

        self.sections.parent_item.update({
            'positions': positions,
        })

        self.sections.current_item.append({
            exprParser.SegmentsContext.__name__: []
        })

        self.sections.current_index = self.sections.last()
        ...

    def exitExpressions(self, ctx: exprParser.ExpressionsContext):
        self.sections.back()
        ...

    def exitExpression(self, ctx: exprParser.ExpressionContext):
        texts = unite(ctx.TEXT())
        
        self.sections.current_item = clean_values({
            'texts': texts,
            exprParser.NamespaceContext.__name__:
                self.sections.current_item[exprParser.NamespaceContext.__name__],
        })

        self.sections.back()
        ...

    def exitNamespace(self, ctx: exprParser.NamespaceContext):
        self.sections.back().back()
        ...

    def exitSegments(self, ctx: exprParser.SegmentsContext):
        texts = unite(ctx.SEGMENT_TEXT())

        self.sections.current_item.update(clean_values({
            'texts': texts,
        }))

        self.sections.back()
        ...

    def exitLiteral_namespace(self, ctx: exprParser.Literal_namespaceContext):
        self.sections.back().back().back()
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

