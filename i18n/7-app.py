#!/usr/bin/env python3
"""
Flask application with timezone support.
"""
from datetime import datetime
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz
from pytz.exceptions import UnknownTimeZoneError


class Config:
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
    login_id = request.args.get('login_as')
    if login_id:
        try:
            return users.get(int(login_id))
        except (ValueError, TypeError):
            return None
    return None


@app.before_request
def before_request():
    g.user = get_user()


def get_locale():
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_timezone():
    """
    Determines the best timezone for a request based on a priority order.
    """
    tz_from_url = request.args.get('timezone')
    if tz_from_url:
        try:
            return pytz.timezone(tz_from_url).zone
        except UnknownTimeZoneError:
            pass

    if g.user and g.user.get('timezone'):
        try:
            pytz.timezone(g.user.get('timezone')).zone
        except UnknownTimeZoneError:
            pass

    return app.config['BABEL_DEFAULT_TIMEZONE']


babel.init_app(
    app,
    locale_selector=get_locale,
    timezone_selector=get_timezone)


@app.route('/')
def index():
    """
    Renders the index page.
    """
    current_time = datetime.datetime.now()
    return render_template('7-index.html', current_time=current_time)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
