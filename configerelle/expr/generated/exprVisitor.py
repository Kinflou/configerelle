# Generated from /home/jibunta/PycharmProjects/configerelle/configerelle/expr/expr.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .exprParser import exprParser
else:
    from exprParser import exprParser

# This class defines a complete generic visitor for a parse tree produced by exprParser.

class exprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by exprParser#expressions.
    def visitExpressions(self, ctx:exprParser.ExpressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#expression.
    def visitExpression(self, ctx:exprParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#namespace.
    def visitNamespace(self, ctx:exprParser.NamespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#segments.
    def visitSegments(self, ctx:exprParser.SegmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#segment.
    def visitSegment(self, ctx:exprParser.SegmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#literal_namespace.
    def visitLiteral_namespace(self, ctx:exprParser.Literal_namespaceContext):
        return self.visitChildren(ctx)



del exprParser