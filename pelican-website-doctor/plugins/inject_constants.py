import json
import os
from pelican import signals
import logging

logger = logging.getLogger(__name__)


def load_constants():
    """Load constants from the JSON file."""
    constants_file = os.path.join(os.path.dirname(__file__), 'resources.json')
    if os.path.exists(constants_file):
        with open(constants_file, 'r', encoding="utf-8", errors="replace") as f:
            return json.load(f)
    else:
        return {}

def inject_constants(generator, content):
    """Inject constants into the content and metadata of each article/page."""
    constants = load_constants()

    # Substitute values from constants in the content
    for key, value in constants.items():
        placeholder = f'{{{{ {key} }}}}'
        logger.info(f"placeholder: {placeholder}")

        if hasattr(content, '_content') and content._content:
            content._content = content._content.replace(placeholder, value)

        if hasattr(content, 'metadata') and 'title' in content.metadata and content.metadata['title'] == placeholder:
            content.metadata.update({'title': value})

        if hasattr(content, 'metadata') and 'image_url' in content.metadata and content.metadata['image_url'] == placeholder:
            content.metadata.update({'image_url': value})



def register():
    """Register the plugin with Pelican."""
    signals.article_generator_write_article.connect(inject_constants)
    signals.page_generator_write_page.connect(inject_constants)
