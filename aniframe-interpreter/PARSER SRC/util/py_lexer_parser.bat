python util/convert_grammar_to_target.py AniFrameLexer.g4 AniFrameParser.g4 py
antlr4 -Dlanguage=Python3 AniFrameLexer.g4 && antlr4 -Dlanguage=Python3 -visitor AniFrameParser.g4