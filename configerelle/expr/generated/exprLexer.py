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
        4,0,7,68,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,
        3,1,3,1,4,1,4,1,4,1,5,1,5,3,5,37,8,5,1,6,1,6,4,6,41,8,6,11,6,12,
        6,42,1,7,4,7,46,8,7,11,7,12,7,47,1,8,5,8,51,8,8,10,8,12,8,54,9,8,
        1,8,4,8,57,8,8,11,8,12,8,58,1,8,5,8,62,8,8,10,8,12,8,65,9,8,1,9,
        1,9,0,0,10,1,1,3,2,5,3,7,4,9,5,11,6,13,0,15,0,17,7,19,0,1,0,4,1,
        0,48,57,5,0,45,45,65,65,90,90,95,95,97,122,3,0,9,10,13,13,32,32,
        5,0,10,10,13,13,58,58,123,123,125,125,70,0,1,1,0,0,0,0,3,1,0,0,0,
        0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,17,1,0,0,0,1,
        21,1,0,0,0,3,24,1,0,0,0,5,26,1,0,0,0,7,28,1,0,0,0,9,31,1,0,0,0,11,
        36,1,0,0,0,13,38,1,0,0,0,15,45,1,0,0,0,17,52,1,0,0,0,19,66,1,0,0,
        0,21,22,5,58,0,0,22,23,5,58,0,0,23,2,1,0,0,0,24,25,5,123,0,0,25,
        4,1,0,0,0,26,27,5,125,0,0,27,6,1,0,0,0,28,29,5,45,0,0,29,30,5,123,
        0,0,30,8,1,0,0,0,31,32,5,125,0,0,32,33,5,45,0,0,33,10,1,0,0,0,34,
        37,3,15,7,0,35,37,3,13,6,0,36,34,1,0,0,0,36,35,1,0,0,0,37,12,1,0,
        0,0,38,40,5,35,0,0,39,41,7,0,0,0,40,39,1,0,0,0,41,42,1,0,0,0,42,
        40,1,0,0,0,42,43,1,0,0,0,43,14,1,0,0,0,44,46,7,1,0,0,45,44,1,0,0,
        0,46,47,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,16,1,0,0,0,49,51,
        7,2,0,0,50,49,1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,
        53,56,1,0,0,0,54,52,1,0,0,0,55,57,3,19,9,0,56,55,1,0,0,0,57,58,1,
        0,0,0,58,56,1,0,0,0,58,59,1,0,0,0,59,63,1,0,0,0,60,62,7,2,0,0,61,
        60,1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,18,1,0,0,
        0,65,63,1,0,0,0,66,67,8,3,0,0,67,20,1,0,0,0,8,0,36,42,45,47,52,58,
        63,0
    ]

class exprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    LCB = 2
    RCB = 3
    LLCB = 4
    LRCB = 5
    SEGMENT_TEXT = 6
    TEXT = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'::'", "'{'", "'}'", "'-{'", "'}-'" ]

    symbolicNames = [ "<INVALID>",
            "LCB", "RCB", "LLCB", "LRCB", "SEGMENT_TEXT", "TEXT" ]

    ruleNames = [ "T__0", "LCB", "RCB", "LLCB", "LRCB", "SEGMENT_TEXT", 
                  "IN_INDEX", "IN_TEXT", "TEXT", "INNER_STR" ]

    grammarFileName = "expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


