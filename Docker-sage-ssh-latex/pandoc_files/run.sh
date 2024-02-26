#!/bin/bash

pandoc CV.md -f markdown -t pdf --pdf-engine=wkhtmltopdf --pdf-engine-opt=--enable-local-file-access -c resume-stylesheet.css -s -o resume.pdf
