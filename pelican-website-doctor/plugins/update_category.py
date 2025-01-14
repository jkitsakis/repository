from pelican import signals

def update_category(generator):
    for article in generator.articles:
        if article.category == 'services':
            article.category.name = 'SERVICES'
            article.category.title = 'SERVICES'


def register():
    signals.article_generator_finalized.connect(update_category)
