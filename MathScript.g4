grammar MathScript;

program: stat+ EOF;

stat:
      ID ASSIGN expr SEMI                  # assignStat
    | PRINT expr SEMI                      # printStat
    | expr SEMI?                           # expressionStat
    ;

expr:
      MINUS expr                           # unaryMinusExpr
    | expr op=POWER expr                   # powerExpr
    | expr op=(MULTIPLY | DIVIDE | MODULO) expr # mulDivModExpr
    | expr op=(PLUS | MINUS) expr          # addSubExpr
    | expr op=(LESS | GREATER | EQUAL | NOT_EQUAL) expr # comparisonExpr
    | ID LPAREN expr (COMMA expr)* RPAREN  # funcCallExpr
    | FLOAT                                # floatExpr
    | INT                                  # intExpr
    | ID                                   # idExpr
    | LPAREN expr RPAREN                   # parenExpr
    ;

PRINT     : 'print';
ASSIGN    : '=';
SEMI      : ';';
LPAREN    : '(';
RPAREN    : ')';
COMMA     : ',';
POWER     : '^';
MULTIPLY  : '*';
DIVIDE    : '/';
MODULO    : '%';
PLUS      : '+';
MINUS     : '-';
LESS      : '<';
GREATER   : '>';
EQUAL     : '==';
NOT_EQUAL : '!=';
FLOAT     : [0-9]+ '.' [0-9]+;
INT       : [0-9]+;
ID        : [a-zA-Z_] [a-zA-Z_0-9]*;
LINE_COMMENT : '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
WS        : [ \t\r\n]+ -> skip;
