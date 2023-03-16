grammar other_test;

// Parser Rules
entries: (TEXT | namespace)*;

namespace: '{' segments '}' ;
segments: SEGMENT_TEXT ('::' SEGMENT_TEXT)* ;


// Lexer Rules
SEGMENT_TEXT: IN_TEXT | IN_INDEX;
fragment IN_INDEX: '#' [0-9]+ ;
fragment IN_TEXT: [Aa-zZ]+;

TEXT: [ \t\r\n]* INNER_STR+ [ \t\r\n]*;
fragment INNER_STR: ~('\r' | '\n' | '{' | '}' | ':') ;


