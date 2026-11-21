import math
from MathScriptVisitor import MathScriptVisitor


class EvalVisitor(MathScriptVisitor):
    """Evaluates a program only after lexical, syntax and semantic checks pass."""
    def __init__(self):
        self.memory = {}
        self.results = []

    def visitAssignStat(self, ctx):
        value = self.visit(ctx.expr())
        self.memory[ctx.ID().getText()] = value
        return value

    def visitPrintStat(self, ctx):
        value = self.visit(ctx.expr()); self.results.append(value); return value

    def visitExpressionStat(self, ctx):
        value = self.visit(ctx.expr()); self.results.append(value); return value

    def visitUnaryMinusExpr(self, ctx): return -self.visit(ctx.expr())
    def visitPowerExpr(self, ctx): return self.visit(ctx.expr(0)) ** self.visit(ctx.expr(1))

    def visitMulDivModExpr(self, ctx):
        left, right, op = self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), ctx.op.text
        if op == '*': return left * right
        if op == '/': return left / right
        if op == '%': return left % right

    def visitAddSubExpr(self, ctx):
        left, right = self.visit(ctx.expr(0)), self.visit(ctx.expr(1))
        return left + right if ctx.op.text == '+' else left - right

    def visitComparisonExpr(self, ctx):
        left, right, op = self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), ctx.op.text
        checks = {'<': left < right, '>': left > right, '==': left == right, '!=': left != right}
        return 1 if checks[op] else 0

    def visitFuncCallExpr(self, ctx):
        funcs = {
            'sqrt': math.sqrt, 'sin': lambda x: math.sin(math.radians(x)),
            'cos': lambda x: math.cos(math.radians(x)), 'tan': lambda x: math.tan(math.radians(x)),
            'abs': abs, 'log': math.log10, 'ln': math.log,
            'floor': math.floor, 'ceil': math.ceil,
        }
        return funcs[ctx.ID().getText()](*(self.visit(e) for e in ctx.expr()))

    def visitFloatExpr(self, ctx): return float(ctx.FLOAT().getText())
    def visitIntExpr(self, ctx): return int(ctx.INT().getText())
    def visitIdExpr(self, ctx): return self.memory[ctx.ID().getText()]
    def visitParenExpr(self, ctx): return self.visit(ctx.expr())
