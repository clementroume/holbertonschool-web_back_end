#!/usr/bin/env python3
"""
Flask application for Task 3.
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """Configuration class for Flask-Babel."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel()


def get_locale():
    """
    Determines the best match for supported languages, checking the URL
    parameter first.
    """
    if 'locale' in request.args:
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index():
    """
    Renders the index page.
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
