# Generated from MathScript.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MathScriptParser import MathScriptParser
else:
    from MathScriptParser import MathScriptParser

# This class defines a complete listener for a parse tree produced by MathScriptParser.
class MathScriptListener(ParseTreeListener):

    # Enter a parse tree produced by MathScriptParser#program.
    def enterProgram(self, ctx:MathScriptParser.ProgramContext):
        pass

    # Exit a parse tree produced by MathScriptParser#program.
    def exitProgram(self, ctx:MathScriptParser.ProgramContext):
        pass


    # Enter a parse tree produced by MathScriptParser#assignStat.
    def enterAssignStat(self, ctx:MathScriptParser.AssignStatContext):
        pass

    # Exit a parse tree produced by MathScriptParser#assignStat.
    def exitAssignStat(self, ctx:MathScriptParser.AssignStatContext):
        pass


    # Enter a parse tree produced by MathScriptParser#printStat.
    def enterPrintStat(self, ctx:MathScriptParser.PrintStatContext):
        pass

    # Exit a parse tree produced by MathScriptParser#printStat.
    def exitPrintStat(self, ctx:MathScriptParser.PrintStatContext):
        pass


    # Enter a parse tree produced by MathScriptParser#floatExpr.
    def enterFloatExpr(self, ctx:MathScriptParser.FloatExprContext):
        pass

    # Exit a parse tree produced by MathScriptParser#floatExpr.
    def exitFloatExpr(self, ctx:MathScriptParser.FloatExprContext):
        pass


    # Enter a parse tree produced by MathScriptParser#intExpr.
    def enterIntExpr(self, ctx:MathScriptParser.IntExprContext):
        pass

    # Exit a parse tree produced by MathScriptParser#intExpr.
    def exitIntExpr(self, ctx:MathScriptParser.IntExprContext):
        pass


    # Enter a parse tree produced by MathScriptParser#powerExpr.
    def enterPowerExpr(self, ctx:MathScriptParser.PowerExprContext):
        pass

    # Exit a parse tree produced by MathScriptParser#powerExpr.
    def exitPowerExpr(self, ctx:MathScriptParser.PowerExprContext):
        pass


    # Enter a parse tree produced by MathScriptParser#addSubExpr.
    def enterAddSubExpr(self, ctx:MathScriptParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by MathScriptParser#addSubExpr.
    def exitAddSubExpr(self, ctx:MathScriptParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by MathScriptParser#unaryMinusExpr.
    def enterUnaryMinusExpr(self, ctx:MathScriptParser.UnaryMinusExprContext):
        pass

    # Exit a parse tree produced by MathScriptParser#unaryMinusExpr.
    def exitUnaryMinusExpr(self, ctx:MathScriptParser.UnaryMinusExprContext):
        pass


    # Enter a parse tree produced by MathScriptParser#mulDivModExpr.
    def enterMulDivModExpr(self, ctx:MathScriptParser.MulDivModExprContext):
        pass

    # Exit a parse tree produced by MathScriptParser#mulDivModExpr.
    def exitMulDivModExpr(self, ctx:MathScriptParser.MulDivModExprContext):
        pass


    # Enter a parse tree produced by MathScriptParser#comparisonExpr.
    def enterComparisonExpr(self, ctx:MathScriptParser.ComparisonExprContext):
        pass

    # Exit a parse tree produced by MathScriptParser#comparisonExpr.
    def exitComparisonExpr(self, ctx:MathScriptParser.ComparisonExprContext):
        pass


    # Enter a parse tree produced by MathScriptParser#funcCallExpr.
    def enterFuncCallExpr(self, ctx:MathScriptParser.FuncCallExprContext):
        pass

    # Exit a parse tree produced by MathScriptParser#funcCallExpr.
    def exitFuncCallExpr(self, ctx:MathScriptParser.FuncCallExprContext):
        pass


    # Enter a parse tree produced by MathScriptParser#parenExpr.
    def enterParenExpr(self, ctx:MathScriptParser.ParenExprContext):
        pass

    # Exit a parse tree produced by MathScriptParser#parenExpr.
    def exitParenExpr(self, ctx:MathScriptParser.ParenExprContext):
        pass


    # Enter a parse tree produced by MathScriptParser#idExpr.
    def enterIdExpr(self, ctx:MathScriptParser.IdExprContext):
        pass

    # Exit a parse tree produced by MathScriptParser#idExpr.
    def exitIdExpr(self, ctx:MathScriptParser.IdExprContext):
        pass



del MathScriptParser