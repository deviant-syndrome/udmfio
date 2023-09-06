import os

from typing import List, Tuple, Union, TextIO, Any

import ply.lex as lex
import ply.yacc as yacc

# Define the UDMF grammar tokens
tokens = [
    'INTEGER',
    'FLOAT',
    'QUOTED_STRING',
    'TRUE',
    'FALSE',
    'IDENTIFIER',
    'ASSIGN',
    'SEMICOLON',
    'LBRACE',
    'RBRACE',
    'COMMENT',
    'BLOCK_COMMENT'
]

# Regular expression rules for tokens
t_ASSIGN = r'='
t_SEMICOLON = r';'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_TRUE = r'true'
t_FALSE = r'false'

# Reserved words
reserved = {
    'true': 'TRUE',
    'false': 'FALSE',
}


# Regular expression for line comments
def t_COMMENT(t):
    r'\/\/.*'
    pass  # Discard comments


# Regular expression for block comments
def t_BLOCK_COMMENT(t):
    r'\/\*.*?\*\/'
    pass  # Discard comments


def t_FLOAT(t):
    r'[+-]?[0-9]+\.[0-9]*([eE][+-]?[0-9]+)?'
    t.value = float(t.value)
    return t


def t_INTEGER(t):
    r'[+-]?([0-9][0-9]*|0[0-9]+|0x[0-9A-Fa-f]+)'
    if t.value.startswith(('0x', '0X')):
        t.value = int(t.value, 16)
    else:
        t.value = int(t.value)
    return t


def t_QUOTED_STRING(t):
    r'"([^"\\]*(\\.[^"\\]*)*)"'
    t.value = t.value[1:-1]  # Remove quotes
    return t


def t_BOOLEAN(t):
    r'^(?:true|false)$'
    t.value = bool(t.value)
    return t


def t_IDENTIFIER(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # check for reserved words
    return t


# Ignored characters (whitespace)
t_ignore = ' \t\n'


# Error handling rule
def t_error(t):
    raise SyntaxError("Illegal character: '%s'" % t.value[0])


# Build the lexer
lexer = lex.lex()


def p_translation_unit(p):
    'translation_unit : global_expr_list'
    p[0] = p[1]


def p_global_expr_list(p):
    'global_expr_list : global_expr global_expr_list'
    p[0] = [p[1]] + p[2]


def p_global_expr_list_empty(p):
    'global_expr_list : '
    p[0] = []


def p_global_expr_block(p):
    'global_expr : block'
    p[0] = p[1]


def p_global_expr_assignment(p):
    'global_expr : assignment_expr'
    p[0] = p[1]


def p_block(p):
    'block : IDENTIFIER LBRACE expr_list RBRACE'
    p[0] = (p[1], p[3])


def p_expr_list(p):
    'expr_list : assignment_expr expr_list'
    p[0] = [p[1]] + p[2]


def p_expr_list_empty(p):
    'expr_list : '
    p[0] = []


def p_assignment_expr(p):
    'assignment_expr : IDENTIFIER ASSIGN value SEMICOLON'
    p[0] = (p[1], p[3])


def p_assignment_expr_nil(p):
    'assignment_expr : IDENTIFIER SEMICOLON'
    p[0] = (p[1], None)


def p_value_integer(p):
    'value : INTEGER'
    p[0] = p[1]


def p_value_float(p):
    'value : FLOAT'
    p[0] = p[1]


def p_value_quoted_string(p):
    'value : QUOTED_STRING'
    p[0] = p[1]


def p_value_boolean_true(p):
    'value : TRUE'
    p[0] = True


def p_value_boolean_false(p):
    'value : FALSE'
    p[0] = False


# Error rule for syntax errors
def p_error(p):
    raise SyntaxError("Syntax error in input! {}".format(p))


# Build the parser
parser = yacc.yacc()

UDMFOutputType = List[Tuple[str, List[Tuple[str, Any]]]]


def parse_udmf(data_source: Union[str, bytes, os.PathLike, TextIO]) -> UDMFOutputType:
    """
    Parses the provided UDMF data source (raw text, like TEXTMAP lump) and returns a structured representation,
    according to UDMF's grammar specification.

    Args:
        data_source (Union[str, bytes, os.PathLike, TextIO]): The UDMF data source. This can be a path to a file
        (as string, bytes, or os.PathLike) or a file-like object with a read() method (like an open file or StringIO).

    Returns:
        UDMFOutputType: A list of tuples where each tuple represents a UDMF block.
        The first element of the tuple is the block name (e.g., "thing") and the second element is a list of key-value
        pairs representing the block's attributes.

    Example:
        Input:
        ```
        thing {
            id = 1;
            type = 3004;
            x = -64.0;
            y = 64.0;
            angle = 90;
        }
        ```

        Output:
        ```
        [('thing', [('id', 1), ('type', 3004), ('x', -64.0), ('y', 64.0), ('angle', 90)])]
        ```

    Raises:
        TypeError: If the provided data source is of an unsupported type.
        SyntaxError: If there is a syntax error in the UDMF data.
    """

    if isinstance(data_source, (str, bytes, os.PathLike)):
        with open(data_source, 'r') as f:
            data = f.read()
    else:
        data = data_source.read()

    parser_output = parser.parse(data)
    return parser_output
