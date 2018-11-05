#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Convierte un archivo markdown en pdf según el estilo de la DNDIP"""

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import with_statement
import os
import sys

import markdown
import pdfkit


def main(input_path, output_path):
    with open(input_path) as input_file:
        html = markdown.markdown(input_file.read())
        pdfkit.from_string(html, output_path, options={"encoding": "utf8"},
                           css="docs/css/pdf.css")


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
