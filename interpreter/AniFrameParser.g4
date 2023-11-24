parser grammar AniFrameParser;

options {
	tokenVocab = AniFrameLexer;
}

start_: (NEWLINE | config_statement)* (
		NEWLINE
		| simple_statement
		| compound_statement
	)* (NEWLINE | draw_statement)* EOF;

simple_statement: (
		(IDENTIFIER DOT_SYMBOL)? function_call
		| variable_declaration
		| assignment_statement
	) NEWLINE;

// Do not add NEWLINE since it is handled by the unindentation in 'block'
compound_statement:
	conditional
	| loop
	| function_declaration_definition;

draw_statement:
	IDENTIFIER DOT_SYMBOL DRAW OPEN_PAREN_SYMBOL actual_parameters CLOSE_PAREN_SYMBOL;

// ================ SIMPLE STATEMENTS ================

// Expression
expression:
	atom
	| OPEN_PAREN_SYMBOL expression CLOSE_PAREN_SYMBOL
	| coordinates
	| list
	| member
	| (IDENTIFIER DOT_SYMBOL)? function_call
	| unary_operator expression
	| expression EXPONENT_OP expression
	| expression (TIMES_OP | DIVIDE_OP | MOD_OP) expression
	| expression (PLUS_OP | MINUS_OP) expression
	| expression (relational_operator | IN) expression
	| expression (AND_OP) expression
	| expression (OR_OP) expression;

coordinates:
	OPEN_BRACE_SYMBOL expression COMMA_SYMBOL expression CLOSE_BRACE_SYMBOL
	| OPEN_BRACE_SYMBOL COMMA_SYMBOL expression? CLOSE_BRACE_SYMBOL {notifyErrorListeners(_input.LT(-1), "Missing x-coordinate", null);
		}
	| OPEN_BRACE_SYMBOL expression COMMA_SYMBOL CLOSE_BRACE_SYMBOL {notifyErrorListeners(_input.LT(-1), "Missing y-coordinate", null);
		}
	| OPEN_BRACE_SYMBOL expression COMMA_SYMBOL expression COMMA_SYMBOL (
		expression COMMA_SYMBOL?
	)* CLOSE_BRACE_SYMBOL {notifyErrorListeners(_input.LT(-1), "Only two coordinates can be specified (x- and y-coordinates)", null);
		};

list:
	OPEN_BRACKET_SYMBOL ((expression COMMA_SYMBOL)* expression)? CLOSE_BRACKET_SYMBOL
	| OPEN_BRACKET_SYMBOL COMMA_SYMBOL (expression COMMA_SYMBOL?)* CLOSE_BRACKET_SYMBOL {notifyErrorListeners(_input.LT(-1), "Missing first list element", null);
		}
	| OPEN_BRACKET_SYMBOL (expression COMMA_SYMBOL)+ CLOSE_BRACKET_SYMBOL {notifyErrorListeners(_input.LT(-1), "Missing list element after comma", null);
		};
member:
	IDENTIFIER (
		OPEN_BRACKET_SYMBOL expression CLOSE_BRACKET_SYMBOL
	)? OPEN_BRACKET_SYMBOL expression CLOSE_BRACKET_SYMBOL;

// Function call
function_call:
	function_name OPEN_PAREN_SYMBOL actual_parameters? CLOSE_PAREN_SYMBOL
	| function_name OPEN_PAREN_SYMBOL COMMA_SYMBOL actual_parameters? CLOSE_PAREN_SYMBOL {notifyErrorListeners(_input.LT(-1), "Missing first argument", null);
		}
	| function_name OPEN_PAREN_SYMBOL actual_parameters? COMMA_SYMBOL CLOSE_PAREN_SYMBOL {notifyErrorListeners(_input.LT(-1), "Missing argument after comma", null);
		};

actual_parameters: (actual_parameter COMMA_SYMBOL)* actual_parameter;
actual_parameter: positional_argument | keyword_argument;
positional_argument: expression;
keyword_argument:
	IDENTIFIER ASSIGN_OP expression
	| IDENTIFIER compound_assignment_operator expression {notifyErrorListeners(_input.LT(-2), "Compound assignment operators are not allowed", null);
		};

// Variable declaration and initialization
variable_declaration: IDENTIFIER COLON_SYMBOL DATA_TYPE;

// Assignment statement
assignment_statement:
	CONST? (variable_declaration | IDENTIFIER) assignment_operator expression
	| IDENTIFIER OPEN_BRACKET_SYMBOL expression CLOSE_BRACKET_SYMBOL assignment_operator expression;

// Configuration statement
config_statement: SET configurable TO expression;

// Flow control statement
flow_control_statement: return_statement | break_statement;
return_statement: RETURN expression;
break_statement: BREAK;

// ================ COMPOUND STATEMENTS ================

// Conditional
conditional: if_statement else_if_statement* else_statement?;

if_statement: if_line conditional_block;
if_line: IF expression COLON_SYMBOL;

else_if_statement: else_if_line conditional_block;
else_if_line: ELSE_IF expression COLON_SYMBOL;

else_statement: else_line conditional_block;
else_line: ELSE COLON_SYMBOL;

// Loop
loop: for_loop | while_loop | repeat_loop;

// for loop
for_loop: for_line loop_block;
for_line:
	FOR (IDENTIFIER COMMA_SYMBOL)? IDENTIFIER IN expression COLON_SYMBOL;

// while loop
while_loop: while_line loop_block;
while_line: WHILE expression COLON_SYMBOL;

// repeat loop
repeat_loop: repeat_line loop_block;
repeat_line: REPEAT expression COLON_SYMBOL;

// Function declaration and definition
function_declaration_definition:
	function_declaration function_block;

function_declaration:
	FUNCTION function_name (
		OPEN_PAREN_SYMBOL formal_parameters? CLOSE_PAREN_SYMBOL
	) (RETURNS return_value_data_type)? COLON_SYMBOL
	| FUNCTION function_name (
		OPEN_PAREN_SYMBOL COMMA_SYMBOL formal_parameters? CLOSE_PAREN_SYMBOL
	) (RETURNS return_value_data_types)? COLON_SYMBOL {notifyErrorListeners(_input.LT(-1), "Missing first parameter", null);
		}
	| FUNCTION function_name (
		OPEN_PAREN_SYMBOL formal_parameters? COMMA_SYMBOL CLOSE_PAREN_SYMBOL
	) (RETURNS return_value_data_types)? COLON_SYMBOL {notifyErrorListeners(_input.LT(-1), "Missing parameter after comma", null);
		}
	| FUNCTION function_name (
		OPEN_PAREN_SYMBOL formal_parameters? CLOSE_PAREN_SYMBOL
	) (RETURNS COMMA_SYMBOL return_value_data_types?)? COLON_SYMBOL {notifyErrorListeners(_input.LT(-1), "Missing first return value data type", null);
		}
	| FUNCTION function_name (
		OPEN_PAREN_SYMBOL formal_parameters? CLOSE_PAREN_SYMBOL
	) (RETURNS return_value_data_types COMMA_SYMBOL)? COLON_SYMBOL {notifyErrorListeners(_input.LT(-1), "Missing return value data type after comma", null);
		}
	| FUNCTION function_name (
		OPEN_PAREN_SYMBOL formal_parameters? CLOSE_PAREN_SYMBOL
	) RETURNS COLON_SYMBOL {notifyErrorListeners(_input.LT(-1), "Missing return value data type", null);
		};

formal_parameters: (formal_parameter COMMA_SYMBOL)* formal_parameter;
formal_parameter: IDENTIFIER (COLON_SYMBOL DATA_TYPE)?;

return_value_data_types: (return_value_data_type COMMA_SYMBOL)* return_value_data_type;
return_value_data_type: DATA_TYPE;

// Miscellaneous
function_name: built_in_function | IDENTIFIER;

conditional_block:
	NEWLINE INDENT (simple_statement | loop | conditional)+ UNINDENT;

conditional_with_break:
	if_statement_with_break else_if_statement_with_break* else_statement_with_break?;
if_statement_with_break: if_line conditional_block_with_break;
else_if_statement_with_break:
	else_if_line conditional_block_with_break;
else_statement_with_break:
	else_line conditional_block_with_break;

conditional_block_with_break:
	NEWLINE INDENT (
		simple_statement
		| break_statement NEWLINE
		| loop
		| conditional_with_break
	)+ UNINDENT;

conditional_with_return:
	if_statement_with_return else_if_statement_with_return* else_statement_with_return?;
if_statement_with_return: if_line conditional_block_with_return;
else_if_statement_with_return:
	else_if_line conditional_block_with_return;
else_statement_with_return:
	else_line conditional_block_with_return;

conditional_block_with_return:
	NEWLINE INDENT (
		simple_statement
		| return_statement NEWLINE
		| loop_with_return
		| conditional_with_return
	)+ UNINDENT;

conditional_with_break_return:
	if_statement_with_break_return else_if_statement_with_break_return*
		else_statement_with_break_return?;
if_statement_with_break_return:
	if_line conditional_block_with_break_return;
else_if_statement_with_break_return:
	else_if_line conditional_block_with_break_return;
else_statement_with_break_return:
	else_line conditional_block_with_break_return;

conditional_block_with_break_return:
	NEWLINE INDENT (
		simple_statement
		| (flow_control_statement) NEWLINE
		| loop_with_return
		| conditional_with_break_return
	)+ UNINDENT;

loop_block:
	NEWLINE INDENT (
		simple_statement
		| (break_statement) NEWLINE
		| loop
		| conditional_with_break
	)+ UNINDENT;

loop_with_return:
	for_loop_with_return
	| while_loop_with_return
	| repeat_loop_with_return;
for_loop_with_return: for_line loop_block_with_return;
while_loop_with_return: while_line loop_block_with_return;
repeat_loop_with_return: repeat_line loop_block_with_return;

loop_block_with_return:
	NEWLINE INDENT (
		simple_statement
		| flow_control_statement NEWLINE
		| loop_with_return
		| conditional_with_break_return
	)+ UNINDENT;

function_block:
	NEWLINE INDENT (
		simple_statement
		| return_statement NEWLINE
		| loop_with_return
		| conditional_with_return
	)+ UNINDENT;

// ================ TOKEN GROUPINGS ================
configurable:
	FRAME_RATE
	| NUM_FRAMES
	| CANVAS_WIDTH
	| CANVAS_HEIGHT
	| CANVAS_BACKGROUND;

built_in_function:
	POINT
	| LINE
	| CURVE
	| CIRCLE
	| ELLIPSE
	| TRIANGLE
	| RECTANGLE
	| QUADRILATERAL
	| POLYGON
	| WRITE
	| MOVE
	| MOVEX
	| MOVEY
	| TURN
	| TURNC
	| TURNCC
	| SHEAR
	| SHEARX
	| SHEARY
	| RESIZE
	| RESIZEX
	| RESIZEY
	| FILL
	| STROKE
	| ADD
	| REMOVE
	| RAND_NUM
	| RAND_INT
	| SQRT
	| SIN
	| COS
	| TAN
	| ASIN
	| ACOS
	| ATAN
	| ATAN2
	| TO_RADIANS
	| TO_DEGREES
	| TYPE
	| INFO;

unary_operator: NOT_OP | PLUS_OP | MINUS_OP;
binary_logical_operator: AND_OP | OR_OP;

relational_operator:
	LESS_THAN_OR_EQUAL_OP
	| GREATER_THAN_OR_EQUAL_OP
	| LESS_THAN_OP
	| GREATER_THAN_OP
	| EQUAL_OP
	| NOT_EQUAL_OP;

assignment_operator: compound_assignment_operator | ASSIGN_OP;

compound_assignment_operator:
	PLUS_ASSIGN_OP
	| MINUS_ASSIGN_OP
	| TIMES_ASSIGN_OP
	| DIVIDE_ASSIGN_OP
	| MOD_ASSIGN_OP;

atom: IDENTIFIER | literal | configurable | FRAME;
literal: FLOAT_LITERAL | INTEGER_LITERAL | STRING_LITERAL;