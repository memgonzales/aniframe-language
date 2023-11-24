# AniFrame

AniFrame is a domain-specific language for creating animations.

## Prerequsites

1. Download the parser generator ANTLR 4. Follow the instructions [here](https://www.antlr.org/) and [here](https://www.antlr.org/download.html).

2. Add a new system (environment) variable named `CLASSPATH` and set its value to `.;path/to/antlr/jar/antlr-version-complete.jar`.

    Replace `path/to/antlr/jar/antlr-version-complete.jar` with the path to your ANTLR Java binary. For example, if you saved `antlr-4.13.1-complete.jar` in `C:/antlr`, then the value of `CLASSPATH` should be set to `.;C:/antlr/antlr-4.13.1-complete.jar`

3. Make sure to install both ANTLR tools and runtime:

    ```
    python -m pip install antlr4-tools
    python -m pip install antlr4-python3-runtime
    ```

## Commands

The commands assume that the working directory is the root of this project.

Replace `<test_case>` with the path to your test case (source code). Sample test cases are provided in the directory `SAMPLE CODE`.

### Lexical Analysis

To print the token names (along with their line and column numbers), run the following commands:

```
cd "PARSER SRC"
util/py_lexer_parser.bat
python driver_lexer.py <test_case>
```

If you want to also display the actual tokens for operators, special symbols, and reserved words (e.g., `,` for `COMMA`), run the following commands:

```
cd "PARSER SRC"
util/py_lexer_parser.bat
python driver_lexer.py <test_case> -c True
```

### Parsing

To display the parse tree, run the following commands:

```
cd "PARSER SRC"
util/java_lexer_parser.bat
python driver_parser.py <test_case>
```

An example test case is `"../SAMPLE CODE/Sample1.anf"`.

## Authors

-   Mark Edward M. Gonzales <br>
    mark_gonzales@dlsu.edu.ph

-   Hans Oswald A. Ibrahim <br>
    hans_oswald_ibrahim@dlsu.edu.ph

-   Elyssia Barrie H. Ong <br>
    elyssia_ong@dlsu.edu.ph
