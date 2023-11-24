python util/convert_grammar_to_target.py AniFrameLexer.g4 AniFrameParser.g4 java
antlr4 AniFrameLexer.g4 && antlr4 AniFrameParser.g4 && javac *.java