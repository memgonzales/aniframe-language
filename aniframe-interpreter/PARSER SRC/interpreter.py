import sys
from antlr4 import *
from AniFrameLexer import AniFrameLexer
from AniFrameParser import AniFrameParser
from AniFrameParserVisitor import AniFrameParserVisitor

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = AniFrameLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = AniFrameParser(stream)
    tree = parser.start_()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
    else:
        vinterp = AniFrameParserVisitor()
        try:
            vinterp.visit(tree)
        except:
            raise Exception
            pass

if __name__ == '__main__':
    main(sys.argv)