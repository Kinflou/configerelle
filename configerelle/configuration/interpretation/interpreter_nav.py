# Standard Imports

# Local Imports
from configerelle.expr.generated.exprLexer import exprLexer
from configerelle.expr.generated.exprParser import exprParser
from configerelle.expr.listener import ExprCombiner
from configerelle.utils.navigator import Navigator
from configerelle.configuration.interpretation.abstration import Interpreter

# External Imports
from antlr4 import InputStream, CommonTokenStream


class NavInterpreter(Interpreter):

    def sections_from_expr(self, expression: str) -> Navigator:
        stream = InputStream(expression)

        lexer = exprLexer(stream)
        tokens = CommonTokenStream(lexer)
        parser = exprParser(tokens)

        listener = ExprCombiner()
        parser.addParseListener(listener)

        parser.expressions()

        return listener.sections
