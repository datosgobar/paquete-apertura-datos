#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Métodos para la actualización de especificaciones de datasets sugeridos

Actualiza a partir de planillas de Google Spreadsheet los ejemplos y
definiciones en markdown, csv y xlsx de especificaciones técnicas de datasets
sugeridos.

    python dataset_specs.py # actualiza todas las especificaciones
    python dataset_specs.py elecciones # actualiza solo "elecciones"
"""

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import with_statement
import os
import sys
import traceback

import json
import re
import requests
import pandas as pd
from unidecode import unidecode
import urllib.parse

PROJECT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
SPECS_DIR = os.path.join(
    PROJECT_DIR, "docs", "src", "datasets-especificaciones")
DOCS_DOWNLOAD_URL = "https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/"

STOP_WORDS = [
    "el", "la", "los", "las",
    "de", "del",
    "y", "a",
    "un", "una", "en"
]


def _df_cols_to_th(df):
    th_cols = ["        <th>{}</th>".format(col) for col in df.columns]
    return "\n".join(th_cols)


def _df_rows_to_tr(df):

    td_rows = []
    for row in df.iterrows():
        td_row = "\n        ".join([
            "<td>{}</td>".format(element)
            for element in list(row[1])
        ])
        td_rows.append(td_row)

    tr_rows = [
        """
    <tr>
        {}
    </tr>
        """.format(td_row) for td_row in td_rows
    ]

    return "".join(tr_rows)


def df_to_html(df):

    df = df.fillna("")

    html = """
<table>
    <tr>
{columns}
    </tr>
{rows}
</table>""".format(
        columns=_df_cols_to_th(df),
        rows=_df_rows_to_tr(df)
    )

    return html


def generate_specs_tables(df, resource_field="recurso"):
    text_elements = []

    for recurso in df[resource_field].unique():
        text_elements.append("### Recurso: {}".format(recurso.ljust(10)))
        text_elements.append(df_to_html(
            df[df.recurso == recurso].drop("recurso", axis=1)
        ))

    return "\n".join(text_elements)


def get_example_from_fields(df, filename):
    df_transposed = df[["titulo", "ejemplo"]].transpose()
    df_transposed.columns = df.titulo
    df_transposed = df_transposed.drop("titulo")

    df_transposed.to_csv(filename, encoding="utf8", index=False)
    df_transposed.to_excel(filename.replace(
        ".csv", ".xlsx"), encoding="utf8", index=False)

    return df_transposed


def title_to_name(title, decode=True, max_len=None, use_complete_words=True):
    """Convierte un título en un nombre normalizado para generar urls."""
    # decodifica y pasa a minúsculas
    if decode:
        title = unidecode(title)
    title = title.lower()

    # remueve caracteres no permitidos
    filtered_title = re.sub(r'[^a-z0-9- ]+', '', title)

    # remueve stop words y espacios y une palabras sólo con un "-"
    normalized_title = '-'.join([word for word in filtered_title.split()
                                 if word not in STOP_WORDS])

    # recorto el titulo normalizado si excede la longitud máxima
    if max_len and len(normalized_title) > max_len:

        # busco la última palabra completa
        if use_complete_words:
            last_word_index = normalized_title.rindex("-", 0, max_len)
            normalized_title = normalized_title[:last_word_index]

        # corto en el último caracter
        else:
            normalized_title = normalized_title[:max_len]

    return normalized_title


def generate_example(df, specs_name, resource_field="recurso"):

    specs_dataset_dir = os.path.join(SPECS_DIR, specs_name)
    if not os.path.exists(specs_dataset_dir):
        os.makedirs(specs_dataset_dir)

    text_elements = []
    for recurso in df[resource_field].unique():
        example_filename = os.path.join(
            specs_dataset_dir,
            title_to_name(recurso) + ".csv"
        )
        example_filename_url = urllib.parse.urljoin(
            DOCS_DOWNLOAD_URL,
            specs_name,
            os.path.basename(example_filename)
        )

        text_elements.append("### Recurso: {}".format(recurso.ljust(10)))
        text_elements.append("**[CSV]({})** | **[XLSX]({})**".format(
            example_filename_url,
            example_filename_url.replace(".csv", ".xlsx")
        ))
        text_elements.append(df_to_html(
            get_example_from_fields(
                df[df.recurso == recurso].drop("recurso", axis=1),
                example_filename
            )
        ))

    return "\n".join(text_elements)


def generate_example_section(specs_name):
    specs_fields_csv = os.path.join(SPECS_DIR, specs_name + "-campos.csv")

    df = pd.read_csv(specs_fields_csv)
    md_example_tables = generate_example(df, specs_name)

    md_example = """## Ejemplos

{}""".format(md_example_tables)

    return md_example


def generate_field_section(specs_name):
    specs_fields_csv = os.path.join(SPECS_DIR, specs_name + "-campos.csv")
    specs_fields_xlsx = os.path.join(SPECS_DIR, specs_name + "-campos.xlsx")
    specs_fields_csv_url = urllib.parse.urljoin(
        DOCS_DOWNLOAD_URL,
        specs_name,
        os.path.basename(specs_fields_csv)
    )
    specs_fields_xlsx_url = urllib.parse.urljoin(
        DOCS_DOWNLOAD_URL,
        specs_name,
        os.path.basename(specs_fields_xlsx)
    )

    df = pd.read_csv(specs_fields_csv)
    df.to_excel(specs_fields_xlsx, encoding="utf8", index=False)

    fields_section = """## Campos

Descargar campos en **[CSV]({})** | **[XLSX]({})**

{}""".format(
        specs_fields_csv_url,
        specs_fields_xlsx_url,
        generate_specs_tables(df)
    )

    return fields_section


def generate_class_section(specs_name, class_explain):
    specs_class_csv = os.path.join(SPECS_DIR, specs_name + "-clases.csv")
    specs_class_xlsx = os.path.join(SPECS_DIR, specs_name + "-clases.xlsx")
    specs_class_csv_url = urllib.parse.urljoin(
        DOCS_DOWNLOAD_URL,
        specs_name,
        os.path.basename(specs_class_csv)
    )
    specs_class_xlsx_url = urllib.parse.urljoin(
        DOCS_DOWNLOAD_URL,
        specs_name,
        os.path.basename(specs_class_xlsx)
    )

    df = pd.read_csv(specs_class_csv)
    df.to_excel(specs_class_xlsx, encoding="utf8", index=False)

    class_section = """## Clases

{}

Descargar clases en **[CSV]({})** | **[XLSX]({})**

{}""".format(
        class_explain,
        specs_class_csv_url,
        specs_class_xlsx_url,
        df_to_html(df)
    )

    return class_section


def download_specs(specs_name, url, suffix):
    specs_filename = os.path.join(
        SPECS_DIR, "{}-{}.csv".format(specs_name, suffix))

    print("Descargando {} desde\n{}...\n".format(
        os.path.basename(specs_filename),
        url
    ))
    specs_response = requests.get(url, allow_redirects=True)
    with open(specs_filename, 'wb') as f:
        f.write(specs_response.content)


def replace_field_section(specs_md, md_field, all_params):
    before_tag = all_params["tags"]["field_before"]
    after_tag = all_params["tags"]["field_after"]

    before_text = specs_md.split(before_tag)[0]
    after_text = specs_md.split(after_tag)[1]

    new_specs_md = """{before_text}{before_tag}

{md_field}

{after_tag}{after_text}""".format(
        before_text=before_text,
        before_tag=before_tag,
        md_field=md_field,
        after_tag=after_tag,
        after_text=after_text
    )

    return new_specs_md


def replace_class_section(specs_md, md_class, all_params):
    before_tag = all_params["tags"]["class_before"]
    after_tag = all_params["tags"]["class_after"]

    before_text = specs_md.split(before_tag)[0]
    after_text = specs_md.split(after_tag)[1]

    new_specs_md = """{before_text}{before_tag}

{md_class}

{after_tag}{after_text}""".format(
        before_text=before_text,
        before_tag=before_tag,
        md_class=md_class,
        after_tag=after_tag,
        after_text=after_text
    )

    return new_specs_md


def replace_example_table(specs_md, md_example, all_params):
    before_tag = all_params["tags"]["example_before"]
    after_tag = all_params["tags"]["example_after"]

    before_text = specs_md.split(before_tag)[0]
    after_text = specs_md.split(after_tag)[1]

    new_specs_md = """{before_text}{before_tag}

{md_example}

{after_tag}{after_text}""".format(
        before_text=before_text,
        before_tag=before_tag,
        md_example=md_example,
        after_tag=after_tag,
        after_text=after_text
    )

    return new_specs_md


def update_dataset_specs(specs_name, config="config-specs.json"):

    # lee el archivo de configuración
    with open(config, "r") as f:
        all_params = json.load(f)
        specs_params = all_params["specs"][specs_name]

    # descarga las tablas de campos y clases de Google Spreadsheet en CSV
    download_specs(specs_name, specs_params["gsheet_fields"], "campos")
    if "gsheet_classes" in specs_params:
        download_specs(specs_name, specs_params["gsheet_classes"], "clases")

    # re-genera las secciones en base a los CSVs descargados
    md_example = generate_example_section(specs_name)
    if "gsheet_classes" in specs_params:
        md_class = generate_class_section(
            specs_name, specs_params.get("class_explain", ""))
    md_field = generate_field_section(specs_name)

    # reemplaza las secciones viejas por las nuevas
    specs_md_file = os.path.join(SPECS_DIR, specs_name + ".md")
    with open(specs_md_file, "r") as f:
        specs_md = f.read()

    specs_md = replace_example_table(specs_md, md_example, all_params)
    if "gsheet_classes" in specs_params:
        specs_md = replace_class_section(specs_md, md_class, all_params)
    specs_md = replace_field_section(specs_md, md_field, all_params)

    # escribe el .md de especificación actualizado
    with open(specs_md_file, "w") as f:
        f.write(specs_md)


def main(specs_name=None):

    # lee el archivo de configuración
    config_path = os.path.join(os.path.dirname(__file__), "config-specs.json")
    with open(config_path, "r") as f:
        params = json.load(f)

    specs_to_update = [specs_name] if specs_name else params["specs"]
    for specs_name in specs_to_update:
        print("=== Actualizando {} ===".format(specs_name))
        try:
            update_dataset_specs(specs_name, config_path)
        except Exception as exc:
            print(exc)
            # print(traceback.print_exc())
        print()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
