from flask import Flask, request
from flask_babel import Babel
from flask_wtf.csrf import CSRFProtect

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'troque-por-uma-chave-segura'
    app.config['BABEL_DEFAULT_LOCALE'] = 'pt'
    app.config['BABEL_SUPPORTED_LOCALES'] = ['pt', 'en']
    csrf = CSRFProtect(app)
    babel = Babel(app)

    def get_locale():
        lang = request.args.get('lang')
        if lang in app.config['BABEL_SUPPORTED_LOCALES']:
            return lang
        return request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES'])

    app.jinja_env.globals['get_locale'] = get_locale
    babel.locale_selector_func = get_locale

    from . import routes
    app.register_blueprint(routes.bp)

    return app
