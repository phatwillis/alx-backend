#!/usr/bin/env python3
"""basic flask app"""
from typing import Dict

import flask
import pytz
from flask import Flask, render_template, request, g
from flask_babel import Babel

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """config class that handles languages"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)


def get_user() -> Dict:
    """gets user logged in"""
    user_id = request.args.get('login_as')
    try:
        return users.get(int(user_id))
    except Exception:
        return None


@app.before_request
def before_request() -> None:
    """called before request"""
    logged_user = get_user()
    if logged_user:
        g.user = logged_user


def get_locale() -> str:
    """get locale function"""

    # if preferred language is in the request
    # get the argument passed as locale
    preferred_lang = request.args.get('locale')
    if preferred_lang and preferred_lang in app.config["LANGUAGES"]:
        return preferred_lang  # return that preferred language.

    # if it is not a url parameter,
    # get it from user data
    user = get_user()
    if user:
        preferred_lang = user.get('locale')
        if preferred_lang in app.config["LANGUAGES"]:
            return preferred_lang
    # try getting it from request header
    if request.headers.get("locale"):
        preferred_lang = request.headers.get("locale")
        if preferred_lang in app.config["LANGUAGES"]:
            return preferred_lang
    else:
        # return default
        return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_timezone() -> str:
    """gets the timezone"""
    # if timezone is in the request
    # get the argument passed as timezone
    time_zone = request.args.get("timezone")
    if time_zone:
        try:
            return pytz.timezone(time_zone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # if it is not a url parameter,
    # get it from user data
    user = get_user()
    if user:
        time_zone = user.get("timezone")
        if time_zone:
            try:
                return pytz.timezone(time_zone).zone
            except pytz.exceptions.UnknownTimeZoneError:
                pass

    # Default
    return Config.BABEL_DEFAULT_TIMEZONE


babel = Babel(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.route("/")
def index() -> str:
    """renders index.html"""
    user = get_user()
    if user:
        username = flask.g.user.get("name")
    else:
        username = None

    return render_template("6-index.html", username=username)


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
