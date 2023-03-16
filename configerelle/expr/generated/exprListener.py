# Generated from /home/jibunta/PycharmProjects/configerelle/configerelle/expr/expr.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .exprParser import exprParser
else:
    from exprParser import exprParser

# This class defines a complete listener for a parse tree produced by exprParser.
class exprListener(ParseTreeListener):

    # Enter a parse tree produced by exprParser#expressions.
    def enterExpressions(self, ctx:exprParser.ExpressionsContext):
        pass

    # Exit a parse tree produced by exprParser#expressions.
    def exitExpressions(self, ctx:exprParser.ExpressionsContext):
        pass


    # Enter a parse tree produced by exprParser#expression.
    def enterExpression(self, ctx:exprParser.ExpressionContext):
        pass

    # Exit a parse tree produced by exprParser#expression.
    def exitExpression(self, ctx:exprParser.ExpressionContext):
        pass


    # Enter a parse tree produced by exprParser#namespace.
    def enterNamespace(self, ctx:exprParser.NamespaceContext):
        pass

    # Exit a parse tree produced by exprParser#namespace.
    def exitNamespace(self, ctx:exprParser.NamespaceContext):
        pass


    # Enter a parse tree produced by exprParser#segments.
    def enterSegments(self, ctx:exprParser.SegmentsContext):
        pass

    # Exit a parse tree produced by exprParser#segments.
    def exitSegments(self, ctx:exprParser.SegmentsContext):
        pass


    # Enter a parse tree produced by exprParser#literal_namespace.
    def enterLiteral_namespace(self, ctx:exprParser.Literal_namespaceContext):
        pass

    # Exit a parse tree produced by exprParser#literal_namespace.
    def exitLiteral_namespace(self, ctx:exprParser.Literal_namespaceContext):
        pass



del exprParser