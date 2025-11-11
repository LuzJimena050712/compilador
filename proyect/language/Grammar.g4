grammar Grammar;

/*Asignación del programa*/
program : (statement NEWLINE)* EOF ;

/*Asignaciones*/  
statement : assing | print | if_statement | for_statement ;

assing : ID '=' expr ; /*Asignaciones de ID y operadores*/

/*Definición de print*/
print : 'print' '(' expr ')' ;

/*Definición de if*/
if_statement : 'if' '(' expr ')' block ;

/*Definición de for*/
for_statement : 'for' '(' assing ';' expr ';' assing ')' block ;

/*Definición de block*/
block : '{' (statement NEWLINE)* '}' ;

/*Definición expr*/
expr
    : expr ('*' | '/') expr
    | expr ('+' | '-') expr
    | expr ('>' | '<' | '>=' | '<=') expr
    | expr ('==' | '!=') expr
    | ID
    | '(' expr ')'
    ;

/*Definición de elementos finales*/
ID : [a-zA-Z][a-zA-Z_0-9]* ;
NEWLINE : [\r\n]+ ;
WS : [ \t]+ -> skip ;
SEMI : ';' ;