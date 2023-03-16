# Standard Imports

# Local Imports
from configerelle.expr.generated.exprLexer import exprLexer
from configerelle.expr.generated.exprParser import exprParser
from configerelle.expr.listener import ExprCombiner

# External Imports
from antlr4 import CommonTokenStream, InputStream


def navigate(expr: str):
    stream = InputStream(expr)

    lexer = exprLexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = exprParser(tokens)

    listener = ExprCombiner()
    parser.addParseListener(listener)

    tree = parser.expressions()

    # print(tree.toStringTree(recog=parser))


if __name__ == '__main__':
    test_expr = 'word {some} with {foo::bar} is {foo::-{baz}-}'
    navigate(test_expr)

