
from flask import Flask, render_template, request, jsonify
import os
from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener

from MathScriptLexer import MathScriptLexer
from MathScriptParser import MathScriptParser

from interpreter import EvalVisitor
from semantic import SemanticAnalyzer

from error_messages import (
    translate_lexer_error,
    translate_parser_error,
    format_error
)

app = Flask(__name__)


# جمع‌آوری خطاهای واژگانی و نحوی
class CollectingErrorListener(ErrorListener):

    def __init__(self, category):
        self.category = category
        self.errors = []

    def syntaxError(
        self, recognizer, offendingSymbol,
        line, column, msg, e
    ):
        if self.category == 'واژگانی':
            detail = translate_lexer_error(msg)
        else:
            detail = translate_parser_error(msg)

        self.errors.append(
            format_error(self.category, line, column, detail)
        )


# استخراج توکن‌ها
def get_tokens(stream, lexer):

    result = []

    symbolic = lexer.symbolicNames
    literal = lexer.literalNames

    for token in stream.tokens:

        if token.type == -1:
            continue

        name = (
            symbolic[token.type]
            if token.type < len(symbolic)
            else None
        )

        if not name or name.startswith('T__'):
            name = (
                literal[token.type]
                if token.type < len(literal)
                else str(token.type)
            )

        result.append({
            'type': name or 'UNKNOWN',
            'value': token.text,
            'line': token.line,
            'column': token.column
        })

    return result


# صفحه اصلی
@app.route('/')
def index():
    return render_template('index.html')


# اجرای کد و تحلیل خطاها
@app.route('/run', methods=['POST'])
def run_code():

    data = request.get_json(silent=True) or {}
    code = data.get('code', '')

    output = []
    memory = {}
    ast = ''
    tokens = []
    errors = []

    # بررسی ورودی
    if not isinstance(code, str) or not code.strip():

        return jsonify({
            'output': ['کدی برای بررسی وارد نشده است.'],
            'memory': {},
            'ast': '',
            'tokens': [],
            'errors': [],
            'status': 'error'
        })

    # -------------------------
    # مرحله اول: تحلیل واژگانی
    # -------------------------

    input_stream = InputStream(code)

    lexer = MathScriptLexer(input_stream)

    lex_listener = CollectingErrorListener('واژگانی')

    lexer.removeErrorListeners()
    lexer.addErrorListener(lex_listener)

    stream = CommonTokenStream(lexer)
    stream.fill()

    tokens = get_tokens(stream, lexer)

    # -------------------------
    # مرحله دوم: تحلیل نحوی
    # -------------------------

    parser = MathScriptParser(stream)

    parse_listener = CollectingErrorListener('نحوی')

    parser.removeErrorListeners()
    parser.addErrorListener(parse_listener)

    tree = parser.program()

    errors.extend(lex_listener.errors)
    errors.extend(parse_listener.errors)

    # -------------------------
    # مرحله سوم: تحلیل معنایی
    # -------------------------

    if not errors:

        ast = tree.toStringTree(recog=parser)

        analyzer = SemanticAnalyzer()
        analyzer.visit(tree)

        errors.extend(analyzer.errors)

    # -------------------------
    # بررسی خطاهای کامپایل
    # -------------------------

    if errors:

        output = [
            '❌ ' + err
            for err in errors
        ]

        status = 'error'

    # -------------------------
    # مرحله چهارم: اجرای برنامه
    # -------------------------

    else:

        visitor = EvalVisitor()

        try:

            visitor.visit(tree)

            memory = visitor.memory

            output = [
                f'>> نتیجه: {value}'
                for value in visitor.results
            ]

            if not output:

                output = [
                    '// بررسی موفق؛ برنامه بدون دستور خروجی است.'
                ]

            status = 'success'

        except Exception:

            memory = {}

            output = [
                '⚠️ برنامه به دلیل بروز مشکل در فرایند اجرا متوقف شد.'
            ]

            status = 'execution_failed'

    # -------------------------
    # ارسال پاسخ به رابط کاربری
    # -------------------------

    return jsonify({
        'output': output,
        'memory': memory,
        'ast': ast,
        'tokens': tokens,
        'errors': errors,
        'status': status
    })


# اجرای سرور
if __name__ == '__main__':

    app.run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000)),
        debug=False
    )
