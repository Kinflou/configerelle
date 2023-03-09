# Generated from /home/jibunta/PycharmProjects/configerelle/configerelle/expr/expr.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,8,47,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,
        4,1,5,4,5,32,8,5,11,5,12,5,33,1,6,4,6,37,8,6,11,6,12,6,38,1,6,1,
        6,1,7,3,7,44,8,7,1,7,1,7,0,0,8,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,
        8,1,0,2,3,0,65,65,90,90,97,122,3,0,9,10,13,13,32,32,49,0,1,1,0,0,
        0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,
        13,1,0,0,0,0,15,1,0,0,0,1,17,1,0,0,0,3,20,1,0,0,0,5,22,1,0,0,0,7,
        24,1,0,0,0,9,27,1,0,0,0,11,31,1,0,0,0,13,36,1,0,0,0,15,43,1,0,0,
        0,17,18,5,58,0,0,18,19,5,58,0,0,19,2,1,0,0,0,20,21,5,123,0,0,21,
        4,1,0,0,0,22,23,5,125,0,0,23,6,1,0,0,0,24,25,5,45,0,0,25,26,5,123,
        0,0,26,8,1,0,0,0,27,28,5,125,0,0,28,29,5,45,0,0,29,10,1,0,0,0,30,
        32,7,0,0,0,31,30,1,0,0,0,32,33,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,
        0,34,12,1,0,0,0,35,37,7,1,0,0,36,35,1,0,0,0,37,38,1,0,0,0,38,36,
        1,0,0,0,38,39,1,0,0,0,39,40,1,0,0,0,40,41,6,6,0,0,41,14,1,0,0,0,
        42,44,5,13,0,0,43,42,1,0,0,0,43,44,1,0,0,0,44,45,1,0,0,0,45,46,5,
        10,0,0,46,16,1,0,0,0,4,0,33,38,43,1,6,0,0
    ]

class exprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    LCB = 2
    RCB = 3
    LLCB = 4
    LRCB = 5
    TEXT = 6
    WS = 7
    NL = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'::'", "'{'", "'}'", "'-{'", "'}-'" ]

    symbolicNames = [ "<INVALID>",
            "LCB", "RCB", "LLCB", "LRCB", "TEXT", "WS", "NL" ]

    ruleNames = [ "T__0", "LCB", "RCB", "LLCB", "LRCB", "TEXT", "WS", "NL" ]

    grammarFileName = "expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


