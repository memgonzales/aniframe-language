# =====================================================================================
# MODIFIED VERSION OF ANTLR'S Lexer CLASS
# @authors      Mark Edward M. Gonzales, Hans Oswald A. Ibrahim, Elyssia Barrie H. Ong
# =====================================================================================
#
# This extends Antlr's Lexer class to implement one-based indexing when printing the column number
#   in case of a lexical error

import sys

if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO
from antlr4 import *
from antlr4.error.Errors import LexerNoViableAltException


class ModifiedAntlrLexer(Lexer):
    def __init__(self, input: InputStream, output: TextIO = sys.stdout):
        super().__init__(input, output)

    def notifyListeners(self, e: LexerNoViableAltException):
        start = self._tokenStartCharIndex
        stop = self._input.index
        text = self._input.getText(start, stop)
        msg = "token recognition error at: '" + self.getErrorDisplay(text) + "'"
        listener = self.getErrorListenerDispatch()

        # Add 1 to tokenStartColumn for one-based column indexing
        listener.syntaxError(
            self, None, self._tokenStartLine, self._tokenStartColumn + 1, msg, e
        )
