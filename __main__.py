#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Module entry point."""

from .engine import RegexpReplacer
from argparse import ArgumentParser

parser = ArgumentParser(
    description='Regular expression replacer.',
    prog='python -m regexp_replacer')
parser.add_argument(
    'rules', metavar='RULES_FILE', type=str, nargs=1,
    help='File with rules.')
parser.add_argument(
    'input', metavar='INPUT_DATA', type=str, nargs='?',
    help='Input data file.')
parser.add_argument(
    '--debug', '-d', action='store_true', default=False,
    help='print result in console')
args = parser.parse_args()

replacer = RegexpReplacer()
replacer.feed_rules(args.rules[0])
file_name = args.input

result = replacer.feed_data(file_name)
if args.debug or file_name == None:
    print(result)
else:
    with open(file_name, 'w') as out:
        out.write(result)
