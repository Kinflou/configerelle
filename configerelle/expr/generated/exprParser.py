# Generated from /home/jibunta/PycharmProjects/configerelle/configerelle/expr/expr.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,7,40,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,5,0,12,8,0,
        10,0,12,0,15,9,0,1,1,1,1,3,1,19,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,
        1,3,3,3,29,8,3,5,3,31,8,3,10,3,12,3,34,9,3,1,4,1,4,1,4,1,4,1,4,0,
        0,5,0,2,4,6,8,0,0,38,0,13,1,0,0,0,2,18,1,0,0,0,4,20,1,0,0,0,6,24,
        1,0,0,0,8,35,1,0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,15,1,0,0,0,13,
        11,1,0,0,0,13,14,1,0,0,0,14,1,1,0,0,0,15,13,1,0,0,0,16,19,5,7,0,
        0,17,19,3,4,2,0,18,16,1,0,0,0,18,17,1,0,0,0,19,3,1,0,0,0,20,21,5,
        2,0,0,21,22,3,6,3,0,22,23,5,3,0,0,23,5,1,0,0,0,24,32,5,6,0,0,25,
        28,5,1,0,0,26,29,5,6,0,0,27,29,3,8,4,0,28,26,1,0,0,0,28,27,1,0,0,
        0,29,31,1,0,0,0,30,25,1,0,0,0,31,34,1,0,0,0,32,30,1,0,0,0,32,33,
        1,0,0,0,33,7,1,0,0,0,34,32,1,0,0,0,35,36,5,4,0,0,36,37,3,6,3,0,37,
        38,5,5,0,0,38,9,1,0,0,0,4,13,18,28,32
    ]

class exprParser ( Parser ):

    grammarFileName = "expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'::'", "'{'", "'}'", "'-{'", "'}-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "LCB", "RCB", "LLCB", "LRCB", 
                      "SEGMENT_TEXT", "TEXT" ]

    RULE_expressions = 0
    RULE_expression = 1
    RULE_namespace = 2
    RULE_segments = 3
    RULE_literal_namespace = 4

    ruleNames =  [ "expressions", "expression", "namespace", "segments", 
                   "literal_namespace" ]

    EOF = Token.EOF
    T__0=1
    LCB=2
    RCB=3
    LLCB=4
    LRCB=5
    SEGMENT_TEXT=6
    TEXT=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExpressionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(exprParser.ExpressionContext,i)


        def getRuleIndex(self):
            return exprParser.RULE_expressions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressions" ):
                listener.enterExpressions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressions" ):
                listener.exitExpressions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressions" ):
                return visitor.visitExpressions(self)
            else:
                return visitor.visitChildren(self)




    def expressions(self):

        localctx = exprParser.ExpressionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expressions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==7:
                self.state = 10
                self.expression()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(exprParser.TEXT, 0)

        def namespace(self):
            return self.getTypedRuleContext(exprParser.NamespaceContext,0)


        def getRuleIndex(self):
            return exprParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = exprParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expression)
        try:
            self.state = 18
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                self.match(exprParser.TEXT)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 17
                self.namespace()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NamespaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(exprParser.LCB, 0)

        def segments(self):
            return self.getTypedRuleContext(exprParser.SegmentsContext,0)


        def RCB(self):
            return self.getToken(exprParser.RCB, 0)

        def getRuleIndex(self):
            return exprParser.RULE_namespace

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamespace" ):
                listener.enterNamespace(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamespace" ):
                listener.exitNamespace(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamespace" ):
                return visitor.visitNamespace(self)
            else:
                return visitor.visitChildren(self)




    def namespace(self):

        localctx = exprParser.NamespaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_namespace)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(exprParser.LCB)
            self.state = 21
            self.segments()
            self.state = 22
            self.match(exprParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SegmentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEGMENT_TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(exprParser.SEGMENT_TEXT)
            else:
                return self.getToken(exprParser.SEGMENT_TEXT, i)

        def literal_namespace(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprParser.Literal_namespaceContext)
            else:
                return self.getTypedRuleContext(exprParser.Literal_namespaceContext,i)


        def getRuleIndex(self):
            return exprParser.RULE_segments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSegments" ):
                listener.enterSegments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSegments" ):
                listener.exitSegments(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSegments" ):
                return visitor.visitSegments(self)
            else:
                return visitor.visitChildren(self)




    def segments(self):

        localctx = exprParser.SegmentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_segments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(exprParser.SEGMENT_TEXT)
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 25
                self.match(exprParser.T__0)
                self.state = 28
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6]:
                    self.state = 26
                    self.match(exprParser.SEGMENT_TEXT)
                    pass
                elif token in [4]:
                    self.state = 27
                    self.literal_namespace()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_namespaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLCB(self):
            return self.getToken(exprParser.LLCB, 0)

        def segments(self):
            return self.getTypedRuleContext(exprParser.SegmentsContext,0)


        def LRCB(self):
            return self.getToken(exprParser.LRCB, 0)

        def getRuleIndex(self):
            return exprParser.RULE_literal_namespace

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral_namespace" ):
                listener.enterLiteral_namespace(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral_namespace" ):
                listener.exitLiteral_namespace(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_namespace" ):
                return visitor.visitLiteral_namespace(self)
            else:
                return visitor.visitChildren(self)




    def literal_namespace(self):

        localctx = exprParser.Literal_namespaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_literal_namespace)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(exprParser.LLCB)
            self.state = 36
            self.segments()
            self.state = 37
            self.match(exprParser.LRCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





