grammar expr_test;

// Entry root rule
expressions: (TEXT | expression)* ;

expression: namespace
          | literal_namespace
          ;

namespace: LCB segments RCB;
segments: SEGMENT_TEXT ('::' (SEGMENT_TEXT | literal_namespace))* ;

literal_namespace: LLCB segments LRCB ;

// Lexer Rules
LCB : '{' ;
RCB : '}' ;

LLCB: '-{' ;
LRCB: '}-' ;

SEGMENT_TEXT: IN_TEXT | IN_INDEX;
fragment IN_INDEX: '#' [0-9]+ ;
fragment IN_TEXT: [Aa-zZ]+;

TEXT: [ \t\r\n]* INNER_STR+ [ \t\r\n]*;
fragment INNER_STR: ~('\r' | '\n' | '{' | '}' | ':') ;

