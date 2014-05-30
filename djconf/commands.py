# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from optparse import OptionParser

from .core import generate_settings

def generate():
    parser = OptionParser()
    parser.add_option('-d', '--directory', dest='source_dir', help='Source DIRECTORY', metavar='DIRECTORY')
    parser.add_option('-o', '--output', dest='output_filename', help='Write settings.py to FILE', metavar='FILE')
    options, args = parser.parse_args()

    generate_settings(
        source_dir=options.source_dir,
        output_filename=options.output_filename)


if __name__ == '__main__':
    generate()
