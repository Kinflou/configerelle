# Standard Imports

# Local Imports
from configerelle.configuration.logic import ConfigBaseLogic
from configerelle.expr.generated.exprListener import exprListener
from configerelle.expr.generated.exprParser import exprParser

# External Imports
from antlr4 import ParserRuleContext


class ExprCombinerDirect(exprListener):
    def __init__(self, config: ConfigBaseLogic):
        super().__init__()

        self.combined = ""

    def enterExpressions(self, ctx: exprParser.ExpressionsContext):
        ...

    def exitExpressions(self, ctx: exprParser.ExpressionsContext):
        ...

    def enterExpression(self, ctx: exprParser.ExpressionContext):
        segment = ctx.getText()
        texts = ctx.TEXT()
        namespaces = ctx.namespace()
        literals = ctx.literal_namespace()

        ...

    def exitExpression(self, ctx: exprParser.ExpressionContext):
        # last_list = deepest_list(self.sections)
        segment = ctx.getText()
        texts = ctx.TEXT()
        namespaces = ctx.namespace()
        literals = ctx.literal_namespace()

        # self.sections.append(segment)
        ...

    def enterNamespace(self, ctx: exprParser.NamespaceContext):
        ...

    def enterSegments(self, ctx: exprParser.SegmentsContext):
        ...

    def enterSegment(self, ctx: exprParser.SegmentContext):
        ...

    def enterLiteral_namespace(self, ctx: exprParser.Literal_namespaceContext):
        ...

    def exitNamespace(self, ctx: exprParser.NamespaceContext):
        ...

    def exitSegments(self, ctx: exprParser.SegmentsContext):
        ...

    def exitSegment(self, ctx: exprParser.SegmentContext):
        ...

    def exitLiteral_namespace(self, ctx: exprParser.Literal_namespaceContext):
        ...

