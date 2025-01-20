import json
import os
import re
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

def extract_placeholder(text):
    match = re.search(r'{{\s*(.*?)\s*}}', text)  # Match content inside {{ }}
    if match:
        return match.group(1)  # Return the content inside {{ }}
    return text  # Return the original text if no match

def inject_constants(content):
    """Inject constants into the content and metadata of each article/page."""
    constants = load_constants()
    return constants.get(content)


def set_article_navigation(generator):
    """Set prev_article and next_article based on Order metadata."""
    # Filter articles that have 'Order' metadata and sort by it
    ordered_articles = sorted(
        (article for article in generator.articles if 'order' in article.metadata and article.category == 'services'),
        key=lambda a: int(a.metadata['order'])  # Correctly reference the lambda's argument
    )
    # Assign prev_article and next_article
    for i, article in enumerate(ordered_articles):
        article.prev_article = ordered_articles[i - 1] if i > 0 else None
        article.next_article = ordered_articles[i + 1] if (len(ordered_articles) - 1) > i >= 0 else None

        logger.info(f"Index: {i}, article: {article.title} - {inject_constants(extract_placeholder(article.title))}")
        # Inject constants or modify titles only if the articles exist
        if article.prev_article and article.prev_article.title:
            if article.prev_article and 'title' in article.prev_article.metadata :
                article.prev_article.metadata['title'] = inject_constants(
                    extract_placeholder(article.prev_article.title))
            else: None


        if article.next_article and article.next_article.title:
            if article.next_article and 'title' in article.next_article.metadata:
                article.next_article.metadata['title'] = inject_constants(
                    extract_placeholder(article.next_article.title))
            else:
                None


def register():
    """Register the plugin with Pelican."""
    signals.article_generator_finalized.connect(set_article_navigation)
