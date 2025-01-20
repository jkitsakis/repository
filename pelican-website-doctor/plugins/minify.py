import os
from pelican import signals
from bs4 import BeautifulSoup
from rcssmin import cssmin
from rjsmin import jsmin
import logging

logger = logging.getLogger(__name__)

def minify_html(content):
    """Minify HTML using BeautifulSoup."""
    soup = BeautifulSoup(content, "html.parser")
    return soup.prettify(formatter="minimal").replace("\n", "")

def minify_file(file_path, minify_func):
    """Utility function to minify a file with a given minify function."""
    with open(file_path, 'r', encoding='utf-8') as f:
        original_content = f.read()

    minified_content = minify_func(original_content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(minified_content)
    logger.info(f"Minified: {file_path}")

def minify_output(generator):
    """Minify HTML, CSS, and JS files in the output directory."""
    output_path = generator.output_path
    logger.info(f"Starting minification in: {output_path}")

    for root, _, files in os.walk(output_path):
        for file in files:
            file_path = os.path.join(root, file)

            try:
                if file.endswith('.html'):
                    minify_file(file_path, minify_html)
                elif file.endswith('.css'):
                    minify_file(file_path, cssmin)
                elif file.endswith('.js'):
                    minify_file(file_path, jsmin)
            except Exception as e:
                logger.error(f"Error processing {file_path}: {e}")

def register():
    """Register the plugin with Pelican."""
    signals.finalized.connect(minify_output)
