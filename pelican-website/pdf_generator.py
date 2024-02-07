import os

from weasyprint import HTML
from markdown2 import markdown_path
from pelican import signals

def generate_pdf(generator):
    for article in generator.articles:
        pdf_filename = f"{article.slug}.pdf"
        convert_md_2_pdf(article.source_path, pdf_filename)

def register():
    signals.article_generator_finalized.connect(generate_pdf)

def convert_md_2_pdf(filename, output=None, theme=None):
    html = markdown_path(filename)
    if not output:
        output = '.'.join([filename.rsplit('.')[0], 'pdf'])

    if theme is not None:
        BASE_DIR = os.path.abspath(os.path.dirname(__file__))
        css_file = theme
        if not os.path.exists(css_file):
            css_file = os.path.join(BASE_DIR, 'themes/'+theme+'.css')

        print (css_file)
        HTML(string=html).write_pdf(output, stylesheets=[css_file])
    else:
        HTML(string=html).write_pdf(output)
