#!/usr/bin/env python
# coding=utf-8
from optparse import OptionParser


def main(option, args):

    """
    Examples
    -------
    >>  python parser_args.py
    option: {'csv': '', 'db': '', 'verbose': True}
    args: []

    >>  python parser_args.py --csv aaa
    option:  {'csv': 'aaa', 'db': '', 'verbose': True}
    args: []
    csv: aaa

    >>  python parser_args.py  123456
    option: {'csv': '', 'db': '', 'verbose': True}
    args: ['123456']

    """
    print 'option:', option
    print 'args:', args
    if option.csv:
        print 'csv:', option.csv


def parse_args():
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.set_defaults(verbose=True)
    parser.add_option("--csv", default='', dest="csv", type="str", help="the csv file to load")
    parser.add_option("--db", default='', dest="db", type="str", help="the db file to write")
    (options, args) = parser.parse_args()
    return options, args


if __name__ == '__main__':
    option, args = parse_args()
    main(option, args)