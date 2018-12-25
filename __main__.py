#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Module entry point."""

from .engine import RegexpReplacer
from argparse import ArgumentParser

parser = ArgumentParser(
    description='Regular expression replacer.',
    prog='python -m regexp_replacer')
parser.add_argument(
    '-r', '--rules', metavar='RULES_FILE', nargs=1, required=True,
    help='File with rules.')
input_group = parser.add_mutually_exclusive_group(required=True)
input_group.add_argument(
    '-f', '--file', metavar='INPUT_FILE', nargs=1,
    help='Read data from file.')
input_group.add_argument(
    '-s', '--stdin', action='store_true',
    help='Read data from stdin')
parser.add_argument(
    '-d', '--debug', action='store_true',
    help='print result in console')

args = parser.parse_args()
replacer = RegexpReplacer()
replacer.feed_rules(args.rules[0])

file_name = None if args.stdin else args.file[0]
result = replacer.feed_data(file_name)

if args.debug or file_name == None:
    print(result)
else:
    with open(file_name, mode='w', encoding='utf-8') as out:
        out.write(result)
