#!/bin/bash
# doctoc genera los anchors al estilo GitHub, que conserva los acentos
# (%C3%A9 = e). mkdocs los quita. Esto normaliza los links del indice.
# El flag /g es necesario: hay lineas con varios acentos.
sed -i.bu \
    -e 's/%C3%A1/a/g' \
    -e 's/%C3%A9/e/g' \
    -e 's/%C3%AD/i/g' \
    -e 's/%C3%B3/o/g' \
    -e 's/%C3%BA/u/g' \
    -e 's/%C3%B1/n/g' \
    -e 's/%C3%BC/u/g' \
    -e 's/%C2%BF//g' \
    -e 's/%C2%A1//g' \
    -e 's/---/-/g' \
    "$1"
rm -f "$1.bu"
