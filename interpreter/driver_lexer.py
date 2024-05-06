import argparse

from AniFrameLexer import AniFrameLexer
from antlr4 import *


def should_display_token_text(complete_display_mode, token_type):
    return (
        complete_display_mode
        or token_type in ["IDENTIFIER", "DATA_TYPE"]
        or token_type.endswith("LITERAL")
    )


def tokenize(source_code, complete_display_mode):
    input_stream = FileStream(source_code)

    # AniFrameLexer.__bases__ = (ModifiedAntlrLexer, )
    lexer = AniFrameLexer(input_stream)
    tokens = lexer.getAllTokens()

    for token in tokens:
        display = f"<{lexer.symbolicNames[token.type]}, "

        if should_display_token_text(
            complete_display_mode, lexer.symbolicNames[token.type]
        ):
            display += f"{token.text}, "

        # Follow one-based indexing for column
        display += f"Line {token.line}, Column {token.column + 1}>"

        print(display)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("source_code", help="Source code to be tokenized")
    parser.add_argument(
        "-c",
        "--complete",
        type=bool,
        default=False,
        required=False,
        help="True to display not only token names but also the actual tokens; False, otherwise",
    )

    args = parser.parse_args()
    tokenize(args.source_code, args.complete)
