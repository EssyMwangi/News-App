from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    message = 'News App'
    return render_template('index.html',message = message)

@app.route('/articles/<int:article_id>')
def source_articles(article_id):

    '''
    View source articles page function that returns the articles details page and its data
    '''
    return render_template('source_articles.html',id = article_id)