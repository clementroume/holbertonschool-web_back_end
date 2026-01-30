# i18n - Holberton School

Welcome to the **i18n** project repository. This project is part of the **Holberton School Full-Stack** curriculum and focuses on internationalizing a Flask web application using the **Flask-Babel** extension.

---

## Table of Contents

- [Description](#description)
- [Project Structure](#project-structure)
- [Learning Objectives](#learning-objectives)

---

## Description

This project introduces the fundamental concepts of **internationalization (i18n)** and **localization (l10n)** within a web application. Using the **Flask-Babel** extension, we will develop a Flask app capable of serving content in multiple languages and adapting to user-specific settings.

The project covers several key aspects of i18n:

- Parametrizing templates to support multiple languages.
- Inferring the appropriate locale using different strategies: URL parameters, user settings, or request headers.
- Localizing timestamps to reflect the user's timezone.

---

## Project Structure

The `i18n` directory includes the following files, which are developed incrementally through the project tasks:

|File(s)|Description|
|---|---|
|`0-app.py`, `templates/0-index.html`|Sets up a basic Flask application with a single route and template.|
|`1-app.py`, `templates/1-index.html`|Integrates Flask-Babel and configures supported languages, a default locale, and timezone.|
|`2-app.py`, `templates/2-index.html`|Implements a `get_locale` function to determine the best language match from the `Accept-Language` request header.|
|`3-app.py`, `templates/3-index.html`, `babel.cfg`, `translations/`|Parametrizes templates using `gettext` and creates translation files (`.po`, `.mo`) for English and French.|
|`4-app.py`, `templates/4-index.html`|Enhances `get_locale` to force a language by using a `locale` URL parameter.|
|`5-app.py`, `templates/5-index.html`|Mocks a user login system and displays a personalized welcome message.|
|`6-app.py`, `templates/6-index.html`|Updates `get_locale` to prioritize the user's preferred locale from their settings.|
|`7-app.py`, `templates/7-index.html`|Implements a `get_timezone` function to infer and validate the user's timezone with `pytz`.|
|`app.py`, `templates/index.html`|Displays the current time, formatted and localized according to the inferred locale and timezone (final version of the app).|

---

## Learning Objectives

Upon completing this project, you will be able to understand and implement the following concepts:

- How to **internationalize** a Flask application.
- Parametrizing Flask templates to display content in different **languages**.
- Using **Flask-Babel** and `gettext` for translation.
- Managing translation catalogs (`.pot`, `.po`, `.mo` files).
- Inferring the correct **locale** based on:
  - URL parameters
  - User settings
  - `Accept-Language` request headers
- Inferring and validating a user's **timezone** with `pytz`.
- **Localizing** timestamps and dates.
- Adhering to Python best practices, including `pycodestyle`, documentation, and type-hinting.

---
