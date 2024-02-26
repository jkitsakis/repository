#!/bin/bash
pandoc -s header.md CV.md -f markdown -t pdf --pdf-engine=wkhtmltopdf --pdf-engine-opt=--enable-local-file-access -c resume-stylesheet.css  -o resume.pdf

#pandoc CV.md --template=template.tex --pdf-engine=xelatex -o index.pdf
