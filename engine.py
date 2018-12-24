#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Regular expression replacer engine."""

import os, re

class RegexpReplacer(object):
    """Regular expression replacer."""
    def __init__(self):
        self._rules = []

    def feed_rules(self, file_name, add=False):
        """Loads rules for replacing."""
        if not add and len(self._rules) > 0:
            print("Release!")
            del self._rules
            self._rules = []
        with open(str(file_name), mode='r', encoding='utf-8') as in_file:
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
        lines = ''
        if file_name != None:
            with open(file_name, mode='r', encoding='utf-8') as in_file:
                lines = ''.join(in_file.readlines())
        else:
            import sys
            lines = ''.join(sys.stdin.readlines())
        for rule in self._rules:
            lines = rule[0].sub(rule[1], lines)
        return lines
