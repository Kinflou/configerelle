grammar expr;

// Entry root rule
expressions: expression*;

expression: TEXT
          | namespace
          | literal_namespace
          ;

namespace: LCB segments RCB;
segments: segment ('::' segment | literal_namespace)* ;
segment: (TEXT)*? ;

literal_namespace: LLCB segments LRCB ;

LCB : '{' ;
RCB : '}' ;

LLCB: '-{' ;
LRCB: '}-' ;

TEXT: [Aa-zZ]+ ;
WS : [ \t\r\n]+ -> skip ;
NL : '\r'? '\n' ;
