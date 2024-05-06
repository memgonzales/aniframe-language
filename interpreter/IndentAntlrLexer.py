# ======================================================================
# MODIFIED VERSION OF Python3LexerBase CLASS IN ANTLR'S GRAMMAR LIBRARY
# ======================================================================
#
# The original Python3LexerBase class allows for the recognition of code block indentation and unindentation
# This modified version inherits the ModifiedAntlrLexer class, which implements one-based indexing
#   when printing the column number in case of a lexical error

# ===============================================
# LICENSE OF THE ORIGINAL Python3LexerBase CLASS
# ===============================================
#
# The MIT License (MIT)
#
# Copyright (c) 2014 by Bart Kiers
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# Project      : python3-parser; an ANTLR4 grammar for Python 3
#                https://github.com/bkiers/python3-parser
# Developed by : Bart Kiers, bart@big-o.nl
# ==================================================================


import re
import sys
from typing import TextIO

from AniFrameParser import AniFrameParser
from antlr4 import *
from antlr4.Token import CommonToken
from ModifiedAntlrLexer import ModifiedAntlrLexer


class IndentAntlrLexer(ModifiedAntlrLexer):
    NEWLINE_PATTERN = re.compile("[^\r\n\f]+")
    SPACES_PATTERN = re.compile("[\r\n\f]+")

    def __init__(self, input: InputStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.tokens = []
        self.indents = []
        self.opened = 0

    def reset(self):
        self.tokens = []
        self.indents = []
        self.opened = 0
        super().reset()

    def emitToken(self, token):
        self._token = token
        self.tokens.append(token)

    def nextToken(self):
        # Check if the end-of-file is ahead and there are still some DEDENTS expected.
        if self._input.LA(1) == AniFrameParser.EOF and len(self.indents) != 0:
            # Remove any trailing EOF tokens from our buffer.
            self.tokens = [
                token for token in self.tokens if token.type != AniFrameParser.EOF
            ]

            # First emit an extra line break that serves as the end of the statement.
            self.emitToken(self.commonToken(AniFrameParser.NEWLINE, "\n"))

            # Now emit as much DEDENT tokens as needed.
            while len(self.indents) != 0:
                self.emitToken(self.createUnindent())
                self.indents.pop()

            # Put the EOF back on the token stream.
            self.emitToken(self.commonToken(AniFrameParser.EOF, "<EOF>"))

        next_ = super().nextToken()
        return next_ if len(self.tokens) == 0 else self.tokens.pop(0)

    def createUnindent(self):
        return self.commonToken(AniFrameParser.UNINDENT, "")

    def commonToken(self, type_: int, text: str):
        stop = self.getCharIndex() - 1
        start = stop if text == "" else stop - len(text) + 1
        return CommonToken(
            self._tokenFactorySourcePair,
            type_,
            Lexer.DEFAULT_TOKEN_CHANNEL,
            start,
            stop,
        )

    def getIndentationCount(self, whitespace: str):
        count = 0
        for c in whitespace:
            if c == "\t":
                count += 8 - count % 8
            else:
                count += 1
        return count

    def atStartOfInput(self):
        return self.getCharIndex() == 0

    def openBrace(self):
        self.opened += 1

    def closeBrace(self):
        self.opened -= 1

    def onNewLine(self):
        new_line = self.NEWLINE_PATTERN.sub("", self.text)
        spaces = self.SPACES_PATTERN.sub("", self.text)

        # Strip newlines inside open clauses except if we are near EOF. We keep NEWLINEs near EOF to
        # satisfy the final newline needed by the single_put rule used by the REPL.
        next_ = self._input.LA(1)
        next_next = self._input.LA(2)

        if self.opened > 0 or (next_next != -1 and next_ in (10, 13, 35)):
            self.skip()
        else:
            self.emitToken(self.commonToken(AniFrameParser.NEWLINE, new_line))
            indent = self.getIndentationCount(spaces)
            previous = 0 if len(self.indents) == 0 else self.indents[-1]

            if indent == previous:
                self.skip()
            elif indent > previous:
                self.indents.append(indent)
                self.emitToken(self.commonToken(AniFrameParser.INDENT, spaces))
            else:
                while len(self.indents) > 0 and self.indents[-1] > indent:
                    self.emitToken(self.createUnindent())
                    self.indents.pop()
