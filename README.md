# MathInterpreter

A small mathematical-language interpreter built with Python, Flask and ANTLR 4.13.2.

## Features

- **Lexical analysis:** recognizes identifiers, numbers, operators and punctuation; reports illegal characters.
- **Syntax analysis:** validates assignments, print statements, expressions, function-call syntax and parentheses.
- **Semantic analysis:** detects use of variables before assignment, unknown function names and incorrect built-in function argument counts.
- Displays tokens, parse tree (AST-style ANTLR tree), output and variable memory in the web interface.
- Supports `//` line comments and `/* ... */` block comments.

Runtime-error handling and logical-error detection are intentionally outside this project's scope.

## Built-in functions

`sqrt(x)`, `sin(x)`, `cos(x)`, `tan(x)`, `abs(x)`, `log(x)`, `ln(x)`, `floor(x)`, `ceil(x)`.

All built-in functions take exactly one numeric argument. Trigonometric functions use degrees.

## Windows setup

Open CMD in this folder and run:

```bat
py -m venv .venv
.venv\Scripts\activate
py -m pip install -r requirements.txt
py app.py
```

Then open `http://127.0.0.1:5000` in your browser.

If `py` is unavailable, install Python 3.10+ from python.org and enable **Add Python to PATH** during installation.

## Regenerate ANTLR files (optional)

Java is required. From this folder run:

```bat
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -no-listener MathScript.g4
```

## Example

```text
x = 10;
y = sqrt(x);
print y;
```

Examples of detected errors:

```text
print unknownVar;  // undefined variable (semantic)
x = 2 + ;          // malformed expression (syntax)
x = 4 @ 2;         // illegal character (lexical)
sqrt(1, 2);        // wrong function argument count (semantic)
```
