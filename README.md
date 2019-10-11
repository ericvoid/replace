# Command Help

    usage: replace.py [-h] [-c COUNT] [-m] [-i] [-s] [-I] [-e ENCODING]
                      search replace path

    Script to find-and-replace text in files using regex.

    positional arguments:
      search                the regex pattern to search
      replace               the replacement text
      path                  the path to the file to perform the substitution

    optional arguments:
      -h, --help            show this help message and exit
      -c COUNT, --count COUNT
                            the maximum number of replacements to perform (all
                            occurrences are replaced by default)
      -m, --multiline       makes '^' also match the beginning of lines and '$'
                            match the end of lines (both of them doesn't include
                            the newline character)
      -i, --ignorecase      ignore case when performing the search
      -s, --dotall          make the '.' special char match any character
                            including newlines
      -I, --inplace         use this flag to do an in-place substitution
      -e ENCODING, --encoding ENCODING
                            the encoding to use when reading and writing files

    For more informations refer to Python documentation on regular expression.
    This script uses the 're.sub' function to perform the substitution.
