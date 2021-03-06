#!/usr/bin/python3
#
# This tool displays an entry from the latin-greek-roots.json
# file. It is meant to be a simple study tool.
#
# Its noteworthy features are: it uses ANSI escape sequences to
# produce colored output; it uses Python's format mini language
# to display its output.
#
# To run it, type the following at the command line:
#
#   python3 WordRoots.py
#

from random import choice
import json
import re

# The colors class contains the ANSI escape codes for
# colored text in the terminal
class colors:
    BLUE  = '\033[94m'
    GREEN = '\033[92m'
    ENDC  = '\033[0m'    # ENDC means 'end color'


class WordRoots():

    datafile = 'latin-greek-roots.json'

    def __init__(self):

        self.entries = []
        with open(WordRoots.datafile, 'r') as df:
            data = json.load(df)

            for record in data:
                # Used to delete footnote data from the root field:
                footnote = re.compile(r'\[\d+\]')

                self.entries.append(
                  {
                    'root' : re.sub(footnote, '', record['root']),
                    'eng'  : record['english'],
                    'org'  : record['origin'],
                    'ety'  : record['etymology'],
                    'exs'  : record['examples']
                    #'examples' : record['examples'].split(', ')
                  }
                )

    def rand(self):
        return choice(self.entries)

    def show(self, entry):
        # The following uses ANSI escape codes to print colored text in the terminal.
        # The colored text is for the titles of the fields in the entry.
        titles = { 'root' : colors.BLUE + 'Root'      + colors.ENDC,
                   'eng'  : colors.BLUE + 'English'   + colors.ENDC,
                   'org'  : colors.BLUE + 'Origin'    + colors.ENDC,
                   'ety'  : colors.BLUE + 'Etymology' + colors.ENDC,
                   'exs'  : colors.BLUE + 'Examples'  + colors.ENDC
                 }

        # Creates a multi-line format for the output. The very succinct syntax
        # of the format mini-language reminds me of similar feature in Perl.
        print('''
{0[root]:34}{0[eng]:34}{0[org]}
{1[root]:25}{1[eng]:25}{1[org]}

{0[ety]}
{1[ety]}

{0[exs]}
{1[exs]}'''.format(titles, entry) )


if __name__ == '__main__':
    wr = WordRoots()
    wr.show(wr.rand())

