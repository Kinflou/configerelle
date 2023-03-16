grammar expr;

// Entry root rule
// TODO: Move the 'TEXT' rule from expression to this one, which also require changing the visitor code
//       Just uncomment this one and remove the 'expressions' and 'expression' lines in use
// expressions: (TEXT | expression)* ;
expressions: expression* ;

// TODO: Move the 'TEXT' rule to expressions, just like described above
expression: TEXT | namespace | literal_namespace ;
// expression: namespace | literal_namespace ;

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
fragment IN_TEXT: ([Aa-zZ] | '_' | '-')+;

TEXT: [ \t\r\n]* INNER_STR+ [ \t\r\n]*;
fragment INNER_STR: ~('\r' | '\n' | '{' | '}' | ':') ;

