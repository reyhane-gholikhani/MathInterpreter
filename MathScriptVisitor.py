# Generated from MathScript.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MathScriptParser import MathScriptParser
else:
    from MathScriptParser import MathScriptParser

# This class defines a complete generic visitor for a parse tree produced by MathScriptParser.

class MathScriptVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MathScriptParser#program.
    def visitProgram(self, ctx:MathScriptParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathScriptParser#assignStat.
    def visitAssignStat(self, ctx:MathScriptParser.AssignStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathScriptParser#printStat.
    def visitPrintStat(self, ctx:MathScriptParser.PrintStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathScriptParser#expressionStat.
    def visitExpressionStat(self, ctx:MathScriptParser.ExpressionStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathScriptParser#floatExpr.
    def visitFloatExpr(self, ctx:MathScriptParser.FloatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathScriptParser#intExpr.
    def visitIntExpr(self, ctx:MathScriptParser.IntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathScriptParser#powerExpr.
    def visitPowerExpr(self, ctx:MathScriptParser.PowerExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathScriptParser#addSubExpr.
    def visitAddSubExpr(self, ctx:MathScriptParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathScriptParser#unaryMinusExpr.
    def visitUnaryMinusExpr(self, ctx:MathScriptParser.UnaryMinusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathScriptParser#mulDivModExpr.
    def visitMulDivModExpr(self, ctx:MathScriptParser.MulDivModExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathScriptParser#comparisonExpr.
    def visitComparisonExpr(self, ctx:MathScriptParser.ComparisonExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathScriptParser#funcCallExpr.
    def visitFuncCallExpr(self, ctx:MathScriptParser.FuncCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathScriptParser#parenExpr.
    def visitParenExpr(self, ctx:MathScriptParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathScriptParser#idExpr.
    def visitIdExpr(self, ctx:MathScriptParser.IdExprContext):
        return self.visitChildren(ctx)



del MathScriptParser