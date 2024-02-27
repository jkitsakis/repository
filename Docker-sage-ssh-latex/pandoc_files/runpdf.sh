#!/bin/bash
pandoc -s input/header.md input/CV.md -f markdown -t pdf --pdf-engine=wkhtmltopdf --pdf-engine-opt=--enable-local-file-access -c template/style.css  -o CV.pdf