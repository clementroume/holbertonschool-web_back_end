#!/usr/bin/env python3
"""
Flask application for Task 3.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """Configuration class for Flask-Babel."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel()

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    Returns a user dictionary based on the 'login_as' URL parameter.
    Returns None if the ID is not found or the parameter is missing.
    """
    login_id = request.args.get('login_as')
    if login_id:
        try:
            user_id = int(login_id)
            return users.get(user_id)
        except (ValueError, TypeError):
            return None
    return None


@app.before_request
def before_request():
    """
    Function to be executed before all other functions.
    Sets the user as a global on flask.g.
    """
    user = get_user()
    g.user = user


def get_locale():
    """
    Determines the best match for supported languages, checking the URL
    parameter first.
    """
    locale_from_url = request.args.get('locale')
    if locale_from_url and locale_from_url in app.config['LANGUAGES']:
        return locale_from_url

    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')

    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index():
    """
    Renders the index page.
    """
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
