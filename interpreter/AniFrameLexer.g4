lexer grammar AniFrameLexer;

// Special tokens to signal indented code blocks
tokens {
	INDENT,
	UNINDENT
}

options {
	superClass = IndentAntlrLexer;
}

// Reserved words
CONST: 'const';
IF: 'if';
ELSE: 'else';
ELSE_IF: 'else if';
FOR: 'for';
WHILE: 'while';
REPEAT: 'repeat';
IN: 'in';
TO: 'to';
BREAK: 'break';
FUNCTION: 'func';
RETURN: 'return';
RETURNS: 'returns';
FRAME: 'FRAME';
SET: 'set';
FRAME_RATE: 'FRAME_RATE';
NUM_FRAMES: 'MAX_NUM_OF_FRAMES';
CANVAS_WIDTH: 'CANVAS_WIDTH';
CANVAS_HEIGHT: 'CANVAS_HEIGHT';
CANVAS_BACKGROUND: 'CANVAS_BACKGROUND';

// Built-in functions
POINT: 'point';
LINE: 'line';
CURVE: 'curve';
CIRCLE: 'circle';
ELLIPSE: 'ellipse';
TRIANGLE: 'triangle';
RECTANGLE: 'rectangle';
QUADRILATERAL: 'quad';
POLYGON: 'polygon';
WRITE: 'write';
MOVE: 'move';
MOVEX: 'moveX';
MOVEY: 'moveY';
TURN: 'turn';
TURNC: 'turnC';
TURNCC: 'turnCC';
SHEAR: 'shear';
SHEARX: 'shearX';
SHEARY: 'shearY';
RESIZE: 'resize';
RESIZEX: 'resizeX';
RESIZEY: 'resizeY';
FILL: 'fill';
STROKE: 'stroke';
ADD: 'add';
REMOVE: 'remove';
RAND_NUM: 'rand_num';
RAND_INT: 'rand_int';
SQRT: 'sqrt';
SIN: 'sin';
COS: 'cos';
TAN: 'tan';
ASIN: 'asin';
ACOS: 'acos';
ATAN: 'atan';
ATAN2: 'atan2';
TO_RADIANS: 'to_rad';
TO_DEGREES: 'to_deg';
GET_INPUT: 'get_input';
TYPE: 'type';
INFO: 'info';
DRAW: 'draw';

// Operators
AND_OP: '&&';
OR_OP: '||';
PLUS_ASSIGN_OP: '+=';
MINUS_ASSIGN_OP: '-=';
TIMES_ASSIGN_OP: '*=';
DIVIDE_ASSIGN_OP: '/=';
MOD_ASSIGN_OP: '%=';
EXPONENT_ASSIGN_OP: '^=';
LESS_THAN_OR_EQUAL_OP: '<=';
GREATER_THAN_OR_EQUAL_OP: '>=';
EQUAL_OP: '==';
NOT_EQUAL_OP: '!=';
PLUS_OP: '+';
MINUS_OP: '-';
TIMES_OP: '*';
DIVIDE_OP: '/';
MOD_OP: '%';
EXPONENT_OP: '^';
NOT_OP: '!';
LESS_THAN_OP: '<';
GREATER_THAN_OP: '>';
ASSIGN_OP: '=';

// Special symbols
OPEN_PAREN_SYMBOL: '(' {self.openBrace();};
CLOSE_PAREN_SYMBOL: ')' {self.closeBrace();};
OPEN_BRACKET_SYMBOL: '[' {self.openBrace();};
CLOSE_BRACKET_SYMBOL: ']' {self.closeBrace();};
OPEN_BRACE_SYMBOL: '{' {self.openBrace();};
CLOSE_BRACE_SYMBOL: '}' {self.closeBrace();};
COMMA_SYMBOL: ',';
DOT_SYMBOL: '.';
COLON_SYMBOL: ':';

DATA_TYPE:
	OBJECT_TYPE
	| NUMBER_TYPE
	| TEXT_TYPE
	| COLOR_TYPE
	| COORD_TYPE
	| LIST_TYPE;

OBJECT_TYPE: 'Object';
NUMBER_TYPE: 'Number';
TEXT_TYPE: 'Text';
COLOR_TYPE: 'Color';
COORD_TYPE: 'Coord';
LIST_TYPE: 'List';

FLOAT_LITERAL:
	(
		FLOAT_WITH_NUMBER_AFTER_DEC_POINT
		| FLOAT_WITHOUT_NUMBER_AFTER_DEC_POINT
	) (EXPONENT_SHORTHAND SIGN? INTEGER_LITERAL)?
	| DIGIT+ EXPONENT_SHORTHAND SIGN? INTEGER_LITERAL;

INTEGER_LITERAL: DIGIT+;

STRING_LITERAL:
	'"' (
		NEGATE_ESCAPE_SEQUENCES_CHAR
		| ESCAPE_SEQUENCES_CHAR
		| '\\' (
			NEGATE_ESCAPE_SEQUENCES_CHAR
			| ESCAPE_SEQUENCES_CHAR
			| '"'
			| '\\'
		)
	)* '"';

IDENTIFIER: ALPHA_WITH_UNDERSCORE ALPHANUMERIC_WITH_UNDERSCORE*;

COMMENT: '#' NEGATE_LINE_BREAK* -> skip;
WHITESPACE: [ \t]+ -> skip;

// Do not use LINE_BREAK+. self.onNewLine() skips subsequent line breaks after the first one,
// essentially collapsing multiple line breaks into a single one.
NEWLINE: (
		{self.atStartOfInput()}? WHITESPACE
		| LINE_BREAK WHITESPACE?
	) {self.onNewLine();};

fragment DIGIT: [0-9];
fragment ALPHA: [A-Za-z];
fragment ALPHA_WITH_UNDERSCORE: [A-Za-z_];
fragment ALPHANUMERIC_WITH_UNDERSCORE: [A-Za-z0-9_];

fragment NEGATE_ESCAPE_SEQUENCES_CHAR: ~[abfvrnst"\\];
fragment ESCAPE_SEQUENCES_CHAR: [abfvrnst];

fragment SIGN: [+-];
fragment EXPONENT_SHORTHAND: [eE];

fragment FLOAT_WITH_NUMBER_AFTER_DEC_POINT: DIGIT* '.' DIGIT+;
fragment FLOAT_WITHOUT_NUMBER_AFTER_DEC_POINT: DIGIT+ '.';

fragment NEGATE_LINE_BREAK: ~[\r\n\f];
fragment LINE_BREAK: ([\r\n\f] | '\r'? '\n');