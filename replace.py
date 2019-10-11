#!/usr/bin/python3
import re
import sys


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description="Script to find-and-replace text in files using regex.",
        epilog="For more informations refer to Python documentation on regular expression. "
               "This script uses the 're.sub' function to perform the substitution.",
        )

    parser.add_argument("-c", "--count", type=int,
                        help="the maximum number of replacements to perform "
                             "(all occurrences are replaced by default)",
                        )
    parser.add_argument("-m", "--multiline", action='store_true',
                        help="makes '^' also match the beginning of lines and '$' match the end of lines "
                             "(both of them doesn't include the newline character)",
                        )
    parser.add_argument("-i", "--ignorecase", action='store_true',
                        help="ignore case when performing the search",
                        )
    parser.add_argument("-s", "--dotall", action='store_true',
                        help="make the '.' special char match any character including newlines",
                        )

    parser.add_argument("-I", "--inplace", action='store_true',
                        help="use this flag to do an in-place substitution",
                        )
    parser.add_argument("-e", "--encoding", type=str, default="utf-8",
                        help="the encoding to use when reading and writing files",
                        )

    parser.add_argument("search",
                        help="the regex pattern to search",
                        )
    parser.add_argument("replace",
                        help="the replacement text",
                        )
    parser.add_argument("path",
                        help="the path to the file to perform the substitution",
                        )

    args = parser.parse_args()

    if not args.search or not args.replace or not args.path:
        parser.print_help(sys.stderr)
        print('search, replace and path arguments should be passed')
        sys.exit(1)

    # SETUP re.sub KEYWORD ARGUMENTS

    sub_kwargs = {'flags': 0}

    if args.count:
        sub_kwargs['count'] = args.count

    if args.multiline:
        sub_kwargs['flags'] |= re.MULTILINE

    if args.ignorecase:
        sub_kwargs['flags'] |= re.IGNORECASE

    if args.dotall:
        sub_kwargs['flags'] |= re.DOTALL

    # EXECUTES THE REPLACEMENT

    with open(args.path, encoding=args.encoding, mode='r') as f:
        data = f.read()

    data = re.sub(args.search, args.replace, data, **sub_kwargs)

    if args.inplace:
        with open(args.path, encoding=args.encoding, mode='w') as f:
            f.write(data)

    else:
        print(data)
