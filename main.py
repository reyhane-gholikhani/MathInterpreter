"""Command-line runner with lexical, syntax and semantic validation."""
from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from MathScriptLexer import MathScriptLexer
from MathScriptParser import MathScriptParser
from semantic import SemanticAnalyzer
from interpreter import EvalVisitor
from error_messages import translate_lexer_error, translate_parser_error, format_error


class ErrorCollector(ErrorListener):
    def __init__(self, kind):
        self.kind, self.errors = kind, []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        detail = translate_lexer_error(msg) if self.kind == 'واژگانی' else translate_parser_error(msg)
        self.errors.append(format_error(self.kind, line, column, detail))


def run_script(code):
    lexer = MathScriptLexer(InputStream(code))
    lex_errors = ErrorCollector('واژگانی')
    lexer.removeErrorListeners(); lexer.addErrorListener(lex_errors)
    stream = CommonTokenStream(lexer)
    parser = MathScriptParser(stream)
    parse_errors = ErrorCollector('نحوی')
    parser.removeErrorListeners(); parser.addErrorListener(parse_errors)
    tree = parser.program()

    errors = lex_errors.errors + parse_errors.errors
    if not errors:
        analyzer = SemanticAnalyzer()
        analyzer.visit(tree)
        errors.extend(analyzer.errors)

    if errors:
        for error in errors:
            print('❌', error)
        return

    print('✅ تحلیل واژگانی، نحوی و معنایی موفق بود.')
    visitor = EvalVisitor()
    visitor.visit(tree)
    for result in visitor.results:
        print('>> نتیجه:', result)
    print('حافظه:', visitor.memory)


if __name__ == '__main__':
    sample = '''
    // نمونه محاسبات ریاضی
    radius = 4.5;
    area = 3.14159 * (radius ^ 2);
    hypotenuse = sqrt(3 ^ 2 + 4 ^ 2);
    print area;
    print hypotenuse;
    '''
    run_script(sample)
