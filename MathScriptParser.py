# Generated from MathScript.g4 by ANTLR 4.13.2
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
        4,1,22,70,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,8,8,0,11,0,12,0,9,1,0,
        1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,25,8,1,3,1,27,
        8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,37,8,2,10,2,12,2,40,9,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,51,8,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,65,8,2,10,2,12,2,68,9,2,1,2,0,
        1,4,3,0,2,4,0,3,1,0,8,10,1,0,11,12,1,0,13,16,80,0,7,1,0,0,0,2,26,
        1,0,0,0,4,50,1,0,0,0,6,8,3,2,1,0,7,6,1,0,0,0,8,9,1,0,0,0,9,7,1,0,
        0,0,9,10,1,0,0,0,10,11,1,0,0,0,11,12,5,0,0,1,12,1,1,0,0,0,13,14,
        5,19,0,0,14,15,5,2,0,0,15,16,3,4,2,0,16,17,5,3,0,0,17,27,1,0,0,0,
        18,19,5,1,0,0,19,20,3,4,2,0,20,21,5,3,0,0,21,27,1,0,0,0,22,24,3,
        4,2,0,23,25,5,3,0,0,24,23,1,0,0,0,24,25,1,0,0,0,25,27,1,0,0,0,26,
        13,1,0,0,0,26,18,1,0,0,0,26,22,1,0,0,0,27,3,1,0,0,0,28,29,6,2,-1,
        0,29,30,5,12,0,0,30,51,3,4,2,10,31,32,5,19,0,0,32,33,5,4,0,0,33,
        38,3,4,2,0,34,35,5,6,0,0,35,37,3,4,2,0,36,34,1,0,0,0,37,40,1,0,0,
        0,38,36,1,0,0,0,38,39,1,0,0,0,39,41,1,0,0,0,40,38,1,0,0,0,41,42,
        5,5,0,0,42,51,1,0,0,0,43,51,5,17,0,0,44,51,5,18,0,0,45,51,5,19,0,
        0,46,47,5,4,0,0,47,48,3,4,2,0,48,49,5,5,0,0,49,51,1,0,0,0,50,28,
        1,0,0,0,50,31,1,0,0,0,50,43,1,0,0,0,50,44,1,0,0,0,50,45,1,0,0,0,
        50,46,1,0,0,0,51,66,1,0,0,0,52,53,10,9,0,0,53,54,5,7,0,0,54,65,3,
        4,2,10,55,56,10,8,0,0,56,57,7,0,0,0,57,65,3,4,2,9,58,59,10,7,0,0,
        59,60,7,1,0,0,60,65,3,4,2,8,61,62,10,6,0,0,62,63,7,2,0,0,63,65,3,
        4,2,7,64,52,1,0,0,0,64,55,1,0,0,0,64,58,1,0,0,0,64,61,1,0,0,0,65,
        68,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,5,1,0,0,0,68,66,1,0,0,
        0,7,9,24,26,38,50,64,66
    ]

class MathScriptParser ( Parser ):

    grammarFileName = "MathScript.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print'", "'='", "';'", "'('", "')'", 
                     "','", "'^'", "'*'", "'/'", "'%'", "'+'", "'-'", "'<'", 
                     "'>'", "'=='", "'!='" ]

    symbolicNames = [ "<INVALID>", "PRINT", "ASSIGN", "SEMI", "LPAREN", 
                      "RPAREN", "COMMA", "POWER", "MULTIPLY", "DIVIDE", 
                      "MODULO", "PLUS", "MINUS", "LESS", "GREATER", "EQUAL", 
                      "NOT_EQUAL", "FLOAT", "INT", "ID", "LINE_COMMENT", 
                      "BLOCK_COMMENT", "WS" ]

    RULE_program = 0
    RULE_stat = 1
    RULE_expr = 2

    ruleNames =  [ "program", "stat", "expr" ]

    EOF = Token.EOF
    PRINT=1
    ASSIGN=2
    SEMI=3
    LPAREN=4
    RPAREN=5
    COMMA=6
    POWER=7
    MULTIPLY=8
    DIVIDE=9
    MODULO=10
    PLUS=11
    MINUS=12
    LESS=13
    GREATER=14
    EQUAL=15
    NOT_EQUAL=16
    FLOAT=17
    INT=18
    ID=19
    LINE_COMMENT=20
    BLOCK_COMMENT=21
    WS=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MathScriptParser.EOF, 0)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathScriptParser.StatContext)
            else:
                return self.getTypedRuleContext(MathScriptParser.StatContext,i)


        def getRuleIndex(self):
            return MathScriptParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MathScriptParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.stat()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 921618) != 0)):
                    break

            self.state = 11
            self.match(MathScriptParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MathScriptParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExpressionStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathScriptParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MathScriptParser.ExprContext,0)

        def SEMI(self):
            return self.getToken(MathScriptParser.SEMI, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionStat" ):
                return visitor.visitExpressionStat(self)
            else:
                return visitor.visitChildren(self)


    class PrintStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathScriptParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRINT(self):
            return self.getToken(MathScriptParser.PRINT, 0)
        def expr(self):
            return self.getTypedRuleContext(MathScriptParser.ExprContext,0)

        def SEMI(self):
            return self.getToken(MathScriptParser.SEMI, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStat" ):
                return visitor.visitPrintStat(self)
            else:
                return visitor.visitChildren(self)


    class AssignStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathScriptParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MathScriptParser.ID, 0)
        def ASSIGN(self):
            return self.getToken(MathScriptParser.ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathScriptParser.ExprContext,0)

        def SEMI(self):
            return self.getToken(MathScriptParser.SEMI, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStat" ):
                return visitor.visitAssignStat(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = MathScriptParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.state = 26
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = MathScriptParser.AssignStatContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.match(MathScriptParser.ID)
                self.state = 14
                self.match(MathScriptParser.ASSIGN)
                self.state = 15
                self.expr(0)
                self.state = 16
                self.match(MathScriptParser.SEMI)
                pass

            elif la_ == 2:
                localctx = MathScriptParser.PrintStatContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.match(MathScriptParser.PRINT)
                self.state = 19
                self.expr(0)
                self.state = 20
                self.match(MathScriptParser.SEMI)
                pass

            elif la_ == 3:
                localctx = MathScriptParser.ExpressionStatContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 22
                self.expr(0)
                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==3:
                    self.state = 23
                    self.match(MathScriptParser.SEMI)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MathScriptParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class FloatExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(MathScriptParser.FLOAT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatExpr" ):
                return visitor.visitFloatExpr(self)
            else:
                return visitor.visitChildren(self)


    class IntExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(MathScriptParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntExpr" ):
                return visitor.visitIntExpr(self)
            else:
                return visitor.visitChildren(self)


    class PowerExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathScriptParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathScriptParser.ExprContext,i)

        def POWER(self):
            return self.getToken(MathScriptParser.POWER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPowerExpr" ):
                return visitor.visitPowerExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddSubExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathScriptParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathScriptParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(MathScriptParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(MathScriptParser.MINUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubExpr" ):
                return visitor.visitAddSubExpr(self)
            else:
                return visitor.visitChildren(self)


    class UnaryMinusExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(MathScriptParser.MINUS, 0)
        def expr(self):
            return self.getTypedRuleContext(MathScriptParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryMinusExpr" ):
                return visitor.visitUnaryMinusExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulDivModExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathScriptParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathScriptParser.ExprContext,i)

        def MULTIPLY(self):
            return self.getToken(MathScriptParser.MULTIPLY, 0)
        def DIVIDE(self):
            return self.getToken(MathScriptParser.DIVIDE, 0)
        def MODULO(self):
            return self.getToken(MathScriptParser.MODULO, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivModExpr" ):
                return visitor.visitMulDivModExpr(self)
            else:
                return visitor.visitChildren(self)


    class ComparisonExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathScriptParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathScriptParser.ExprContext,i)

        def LESS(self):
            return self.getToken(MathScriptParser.LESS, 0)
        def GREATER(self):
            return self.getToken(MathScriptParser.GREATER, 0)
        def EQUAL(self):
            return self.getToken(MathScriptParser.EQUAL, 0)
        def NOT_EQUAL(self):
            return self.getToken(MathScriptParser.NOT_EQUAL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonExpr" ):
                return visitor.visitComparisonExpr(self)
            else:
                return visitor.visitChildren(self)


    class FuncCallExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MathScriptParser.ID, 0)
        def LPAREN(self):
            return self.getToken(MathScriptParser.LPAREN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathScriptParser.ExprContext,i)

        def RPAREN(self):
            return self.getToken(MathScriptParser.RPAREN, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MathScriptParser.COMMA)
            else:
                return self.getToken(MathScriptParser.COMMA, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCallExpr" ):
                return visitor.visitFuncCallExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(MathScriptParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MathScriptParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MathScriptParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MathScriptParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdExpr" ):
                return visitor.visitIdExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MathScriptParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = MathScriptParser.UnaryMinusExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 29
                self.match(MathScriptParser.MINUS)
                self.state = 30
                self.expr(10)
                pass

            elif la_ == 2:
                localctx = MathScriptParser.FuncCallExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 31
                self.match(MathScriptParser.ID)
                self.state = 32
                self.match(MathScriptParser.LPAREN)
                self.state = 33
                self.expr(0)
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 34
                    self.match(MathScriptParser.COMMA)
                    self.state = 35
                    self.expr(0)
                    self.state = 40
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 41
                self.match(MathScriptParser.RPAREN)
                pass

            elif la_ == 3:
                localctx = MathScriptParser.FloatExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 43
                self.match(MathScriptParser.FLOAT)
                pass

            elif la_ == 4:
                localctx = MathScriptParser.IntExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 44
                self.match(MathScriptParser.INT)
                pass

            elif la_ == 5:
                localctx = MathScriptParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 45
                self.match(MathScriptParser.ID)
                pass

            elif la_ == 6:
                localctx = MathScriptParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 46
                self.match(MathScriptParser.LPAREN)
                self.state = 47
                self.expr(0)
                self.state = 48
                self.match(MathScriptParser.RPAREN)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 66
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 64
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = MathScriptParser.PowerExprContext(self, MathScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 52
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 53
                        localctx.op = self.match(MathScriptParser.POWER)
                        self.state = 54
                        self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = MathScriptParser.MulDivModExprContext(self, MathScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 55
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 56
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1792) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 57
                        self.expr(9)
                        pass

                    elif la_ == 3:
                        localctx = MathScriptParser.AddSubExprContext(self, MathScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 58
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 59
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==11 or _la==12):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 60
                        self.expr(8)
                        pass

                    elif la_ == 4:
                        localctx = MathScriptParser.ComparisonExprContext(self, MathScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 61
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 62
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 122880) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 63
                        self.expr(7)
                        pass

             
                self.state = 68
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         




