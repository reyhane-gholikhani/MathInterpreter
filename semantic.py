"""Static semantic analysis for MathScript. No program execution occurs here."""
import math
from MathScriptVisitor import MathScriptVisitor


FUNCTIONS = {
    "sqrt": 1, "sin": 1, "cos": 1, "tan": 1,
    "abs": 1, "log": 1, "ln": 1, "floor": 1, "ceil": 1,
}


class SemanticAnalyzer(MathScriptVisitor):
    def __init__(self):
        self.symbols = set()
        self.errors = []

    def error(self, ctx, message):
        token = getattr(ctx, "start", None)
        line = getattr(token, "line", 1)
        column = getattr(token, "column", 0)
        self.errors.append(
            f"خطای معنایی در خط {line}، ستون {column}: {message}"
        )

    def visitAssignStat(self, ctx):
        self.visit(ctx.expr())
        self.symbols.add(ctx.ID().getText())

    def visitPrintStat(self, ctx):
        self.visit(ctx.expr())

    def visitExpressionStat(self, ctx):
        self.visit(ctx.expr())

    def visitIdExpr(self, ctx):
        name = ctx.ID().getText()
        if name not in self.symbols:
            self.error(ctx, f"متغیر '{name}' پیش از استفاده تعریف نشده است.")

    def visitFuncCallExpr(self, ctx):
        name = ctx.ID().getText()
        args = ctx.expr()
        for arg in args:
            self.visit(arg)
        if name not in FUNCTIONS:
            self.error(ctx, f"تابع '{name}' شناخته‌شده نیست.")
        elif len(args) != FUNCTIONS[name]:
            self.error(ctx, f"تابع '{name}' باید {FUNCTIONS[name]} آرگومان بگیرد، اما {len(args)} آرگومان دریافت کرده است.")

    def visitUnaryMinusExpr(self, ctx): self.visit(ctx.expr())
    def visitPowerExpr(self, ctx):
        for expr in ctx.expr(): self.visit(expr)
    def visitMulDivModExpr(self, ctx):
        for expr in ctx.expr(): self.visit(expr)
    def visitAddSubExpr(self, ctx):
        for expr in ctx.expr(): self.visit(expr)
    def visitComparisonExpr(self, ctx):
        for expr in ctx.expr(): self.visit(expr)
    def visitParenExpr(self, ctx): self.visit(ctx.expr())
