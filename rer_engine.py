#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Regular expression replacer engine."""

import os
import re

class RegexpReplacer(object):
    """Regular expression replacer."""
    def __init__(self):
        self._rules = []

    def feed_rules(self, file_name, add=False):
        """Loads rules for replacing."""
        if not add and len(self._rules) > 0:
            print "Release!"
            del self._rules
            self._rules = []
        with open(str(file_name), 'r') as in_file:
            lines = in_file.readlines()
            tmp = ''
            for line in lines:
                cmd = line[:3].rstrip('\r\n')
                if cmd == ':: ':
                    tmp += line[3:].rstrip('\r\n')
                elif cmd == 'p: ': # pattern
                    self._rules.append(
                        [re.compile(tmp + line[3:].rstrip('\r\n')), ])
                    tmp = ''
                elif cmd == 'p:':
                    self._rules.append([re.compile(tmp), ])
                elif cmd == 'r: ': # replace
                    self._rules[-1].append(tmp + line[3:].strip())
                    tmp = ''
                elif cmd == 'r:':
                    self._rules[-1].append(tmp)
                elif cmd == '>> ': # use file
                    new_file = os.path.join(os.path.dirname(file_name),
                                            line[3:].strip())
                    self.feed_rules(new_file, add=True)
                elif cmd == 'x:': # interrupt file reading
                    break

    def feed_data(self, file_name):
        """Load data to replace."""
        with open(file_name, 'r') as in_file:
            lines = ''.join(in_file.readlines())
        print "Rules count:", len(self._rules)
        for rule in self._rules:
            lines = rule[0].sub(rule[1], lines)
        return lines

def _main():
    """Script entry point."""
    import argparse
    parser = argparse.ArgumentParser(description='Regular expression replacer.',
                                     usage='%(prog)s <rules> <path> [--debug]')
    parser.add_argument('rules', metavar='RULES_FILE', type=str, nargs=1,
                        help='File with rules.')
    parser.add_argument('input', metavar='INPUT_DATA', type=str, nargs=1,
                        help='Input data file.')
    parser.add_argument('--debug', '-d', action='store_true', default=False,
                        help='Prints interpreter result in console.')
    args = parser.parse_args()
    replacer = RegexpReplacer()
    replacer.feed_rules(args.rules[0])
    result = replacer.feed_data(args.input[0])
    if args.debug:
        print result
    else:
        with open(args.input[0], 'w') as out:
            out.write(result)

if __name__ == '__main__':
    _main()
