import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_babel import Babel
from app.config import Config
from app.models import db

config_object = Config()

# Crie a instância do SQLAlchemy aqui para ser compartilhada
db = SQLAlchemy()
migrate = Migrate()
babel = Babel()


def get_locale():
    # Retorna o idioma padrão (você pode personalizar esta lógica)
    return "pt"  # ou request.accept_languages.best_match(['en', 'pt', 'es'])


def create_app(config_object=None):
    app = Flask(__name__)

    # Configuração
    if config_object:
        app.config.from_object(config_object)
    else:
        # Configuração padrão
        app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
        app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config["BABEL_DEFAULT_LOCALE"] = "pt"
        app.config["BABEL_SUPPORTED_LOCALES"] = ["pt", "en"]

    # Inicializa extensões com o app
    db.init_app(app)
    migrate.init_app(app, db)
    babel.init_app(app, locale_selector=get_locale)

    # Importa e registra blueprints
    from app.routes import main_bp

    app.register_blueprint(main_bp)

    # Cria tabelas do banco de dados
    with app.app_context():
        db.create_all()

    @app.context_processor
    def inject_functions():
        return dict(get_locale=lambda: "pt-BR")

    return app
