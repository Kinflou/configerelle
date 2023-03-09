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
        4,1,8,47,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,5,0,
        14,8,0,10,0,12,0,17,9,0,1,1,1,1,1,1,3,1,22,8,1,1,2,1,2,1,2,1,2,1,
        3,1,3,1,3,1,3,5,3,32,8,3,10,3,12,3,35,9,3,1,4,5,4,38,8,4,10,4,12,
        4,41,9,4,1,5,1,5,1,5,1,5,1,5,1,39,0,6,0,2,4,6,8,10,0,0,46,0,15,1,
        0,0,0,2,21,1,0,0,0,4,23,1,0,0,0,6,27,1,0,0,0,8,39,1,0,0,0,10,42,
        1,0,0,0,12,14,3,2,1,0,13,12,1,0,0,0,14,17,1,0,0,0,15,13,1,0,0,0,
        15,16,1,0,0,0,16,1,1,0,0,0,17,15,1,0,0,0,18,22,5,6,0,0,19,22,3,4,
        2,0,20,22,3,10,5,0,21,18,1,0,0,0,21,19,1,0,0,0,21,20,1,0,0,0,22,
        3,1,0,0,0,23,24,5,2,0,0,24,25,3,6,3,0,25,26,5,3,0,0,26,5,1,0,0,0,
        27,33,3,8,4,0,28,29,5,1,0,0,29,32,3,8,4,0,30,32,3,10,5,0,31,28,1,
        0,0,0,31,30,1,0,0,0,32,35,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,
        7,1,0,0,0,35,33,1,0,0,0,36,38,5,6,0,0,37,36,1,0,0,0,38,41,1,0,0,
        0,39,40,1,0,0,0,39,37,1,0,0,0,40,9,1,0,0,0,41,39,1,0,0,0,42,43,5,
        4,0,0,43,44,3,6,3,0,44,45,5,5,0,0,45,11,1,0,0,0,5,15,21,31,33,39
    ]

class exprParser ( Parser ):

    grammarFileName = "expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'::'", "'{'", "'}'", "'-{'", "'}-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "LCB", "RCB", "LLCB", "LRCB", 
                      "TEXT", "WS", "NL" ]

    RULE_expressions = 0
    RULE_expression = 1
    RULE_namespace = 2
    RULE_segments = 3
    RULE_segment = 4
    RULE_literal_namespace = 5

    ruleNames =  [ "expressions", "expression", "namespace", "segments", 
                   "segment", "literal_namespace" ]

    EOF = Token.EOF
    T__0=1
    LCB=2
    RCB=3
    LLCB=4
    LRCB=5
    TEXT=6
    WS=7
    NL=8

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
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 84) != 0:
                self.state = 12
                self.expression()
                self.state = 17
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


        def literal_namespace(self):
            return self.getTypedRuleContext(exprParser.Literal_namespaceContext,0)


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
            self.state = 21
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.match(exprParser.TEXT)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.namespace()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 20
                self.literal_namespace()
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
            self.state = 23
            self.match(exprParser.LCB)
            self.state = 24
            self.segments()
            self.state = 25
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

        def segment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprParser.SegmentContext)
            else:
                return self.getTypedRuleContext(exprParser.SegmentContext,i)


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
            self.state = 27
            self.segment()
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==4:
                self.state = 31
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 28
                    self.match(exprParser.T__0)
                    self.state = 29
                    self.segment()
                    pass
                elif token in [4]:
                    self.state = 30
                    self.literal_namespace()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SegmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(exprParser.TEXT)
            else:
                return self.getToken(exprParser.TEXT, i)

        def getRuleIndex(self):
            return exprParser.RULE_segment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSegment" ):
                listener.enterSegment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSegment" ):
                listener.exitSegment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSegment" ):
                return visitor.visitSegment(self)
            else:
                return visitor.visitChildren(self)




    def segment(self):

        localctx = exprParser.SegmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_segment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 36
                    self.match(exprParser.TEXT) 
                self.state = 41
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
        self.enterRule(localctx, 10, self.RULE_literal_namespace)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(exprParser.LLCB)
            self.state = 43
            self.segments()
            self.state = 44
            self.match(exprParser.LRCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





