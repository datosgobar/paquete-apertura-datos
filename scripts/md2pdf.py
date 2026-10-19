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
import re
import shutil

PDF_CSS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pdf.css")


def main(input_path, output_path):
    with open(input_path) as input_file:
        # saca el frontmatter de Starlight (--- title: ... ---)
        html = markdown.markdown(re.sub(r"\A---\n.*?\n---\n", "", input_file.read(), flags=re.S))

        # guarda html
        with open(output_path.replace(".pdf", ".html"), "wb") as output_html:
            html_with_style = """
            <link rel="stylesheet" href="pdf.css" type="text/css"/>
            """ + html
            output_html.write(html_with_style.encode("utf-8"))
            shutil.copyfile(
                PDF_CSS,
                os.path.join(os.path.dirname(output_path), "pdf.css")
            )

        # guarda pdf
        pdfkit.from_string(html, output_path, options={"encoding": "utf8"},
                           css=PDF_CSS)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
