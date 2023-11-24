import sys
from antlr4 import *
from AniFrameLexer import AniFrameLexer
from AniFrameParser import AniFrameParser
from AniFrameParserVisitor import AniFrameParserVisitor

import shutil
import os

def make_posix_compliant(source_code):
    file = f'{source_code}.tmp'
    shutil.copy(source_code, file)
    with open(file, 'a') as f:
        f.write('\r\n')

    return file


def main(argv):
    input_stream = FileStream(make_posix_compliant(argv[1]))
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

    try:
        os.remove(f'{argv[1]}.tmp')
    except Exception as e:
        pass


if __name__ == '__main__':
    main(sys.argv)