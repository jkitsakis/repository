# plugins/language_switcher.py
from pelican import signals
from markupsafe import Markup

# Global variable to store the generator context
global_generator = None


def add_language_switcher(generator):
    """Add the language switcher to the context."""
    global global_generator
    global_generator = generator  # Store the generator globally

    # Add available languages and current language to context
    generator.context['languages'] = ['en', 'el']
    generator.context['current_language'] = generator.settings.get('DEFAULT_LANG', 'el')
    # Add language switcher to the context
    generator.context['language_switcher'] = get_language_switcher(generator)


def get_language_switcher(generator):
    """Generate the HTML for the language switcher."""
    current_language = generator.context.get('current_language', 'en')
    if current_language == 'en':
        language_switcher = '<a href="?lang=el" class="language-switcher">Ελληνικά</a>'
    elif current_language == 'el':
        language_switcher = '<a href="?lang=en" class="language-switcher">English</a>'
    else:
        language_switcher = ''
    return Markup(language_switcher)


def modify_content_for_language(content):
    """Modify content based on selected language."""
    # Access the stored global generator
    global global_generator
    if global_generator is None:
        return content

    lang = global_generator.context.get('current_language', 'en')

    if lang == 'el':
        # Modify content specific to the Greek version
        if hasattr(content, 'title'):
            content.title = f"Greek version of {content.title}"
        if hasattr(content, 'slug'):
            content.slug = f"el/{content.slug}"

    return content


def register():
    """Register the plugin functions with Pelican signals."""
    signals.generator_init.connect(add_language_switcher)  # Set up the context for language switcher
    signals.content_object_init.connect(modify_content_for_language)  # Modify content for language
    """add   <li class="nav-item">{{ language_switcher }}</li> in navigation.html"""
    """PLUGINS = ['sitemap', 'inject_constants', 'article_order_navigation', 'minify', 'language_switcher', 'i18n_subsites']"""
