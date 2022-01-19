#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Module entry point."""

from argparse import ArgumentParser

from .engine import RegexpReplacer

parser = ArgumentParser(
    description='Regular expression replacer.',
    prog='python -m regexp_replacer')
parser.add_argument(
    '-r', '--rules', metavar='RULES_FILE', required=True,
    help='File with rules')
input_group = parser.add_mutually_exclusive_group(required=True)
input_group.add_argument(
    '-f', '--file', metavar='INPUT_FILE', help='Read data from file')
input_group.add_argument(
    '-s', '--stdin', action='store_true', help='Read data from stdin')
parser.add_argument(
    '-d', '--debug', action='store_true', help='Print result in console')

args = parser.parse_args()
replacer = RegexpReplacer()
replacer.feed_rules(args.rules)

filename = None if args.stdin else args.file
result = replacer.feed_data(filename)

if args.debug or filename is None:
    print(result)
else:
    with open(filename, 'w', encoding='utf-8') as out:
        out.write(result)
