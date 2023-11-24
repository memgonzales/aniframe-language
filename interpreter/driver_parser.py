import subprocess
import argparse
import shutil
import os


def get_parse_tree(source_code, make_posix_compliant):
    # Parse POSIX-compliant version of the source code, with newline appended to the end
    #   of the last line

    # This is to ensure compliance with POSIX 3.206, which states that every line should
    #   end with a new line:
    #   https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_206

    # Relevant discussion can be found here:
    #   https://stackoverflow.com/questions/729692/why-should-text-files-end-with-a-newline

    file = source_code
    if make_posix_compliant:
        file = f'{source_code}.tmp'
        shutil.copy(source_code, file)
        with open(file, 'a') as f:
            f.write('\r\n')

    # Display the parse tree on  GUI
    output = subprocess.run(['grun', 'AniFrame', 'start_', file],
                            shell=True, stderr=subprocess.PIPE)

    errors = output.stderr.decode('cp1252')
    for error in errors.split('\n'):
        error_words = error.split(' ')
        try:
            error_location = error_words[1]

            # Change the column number to make it one-based
            # (Antlr uses zero-based indexing for the column number)
            line_num, col_num = error_location.split(':')
            error_words[1] = f'{line_num}:{int(col_num) + 1}'

            print(' '.join(error_words))
        except:
            pass

    subprocess.run(['grun', 'AniFrame', 'start_', '-gui', file],
                   shell=True, stderr=subprocess.DEVNULL)

    try:
        os.remove(f'{source_code}.tmp')
    except:
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('source_code', help='Source code to be parsed')
    parser.add_argument('-p', '--do_not_make_posix_compliant',
                        action='store_false',
                        required=False,
                        help='True to parse POSIX-compliant version of source code (that is, with newline appended to the end of the last line); False, otherwise')

    args = parser.parse_args()
    get_parse_tree(args.source_code, args.do_not_make_posix_compliant)
