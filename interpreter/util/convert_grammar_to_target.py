import argparse
import os
import shutil


def convert_grammar(lexer_grammar, parser_grammar, target):
    shutil.copy(lexer_grammar, f"{lexer_grammar}.tmp")
    shutil.copy(parser_grammar, f"{parser_grammar}.tmp")

    with open(lexer_grammar, "w") as lexer, open(parser_grammar, "w") as parser, open(
        f"{lexer_grammar}.tmp"
    ) as lexer_temp, open(f"{parser_grammar}.tmp") as parser_temp:
        for line in lexer_temp:
            if "self" in line and target == "java":
                line = line.replace("self", "this")
            elif "this" in line and target == "py":
                line = line.replace("this", "self")

            lexer.write(line)

        for line in parser_temp:
            if "self" in line and target == "java":
                line = line.replace("self", "this")
            elif "this" in line and target == "py":
                line = line.replace("this", "self")

            parser.write(line)

    os.remove(f"{lexer_grammar}.tmp")
    os.remove(f"{parser_grammar}.tmp")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("lexer_grammar", help="Lexer grammar")
    parser.add_argument("parser_grammar", help="Parser grammar")
    parser.add_argument(
        "target", help='Target language: "py" for Python or "java" for Java'
    )

    args = parser.parse_args()
    convert_grammar(args.lexer_grammar, args.parser_grammar, args.target)
