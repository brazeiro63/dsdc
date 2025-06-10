import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_babel import Babel
from flask_cors import CORS
from app.config import Config

# Crie as instâncias das extensões para serem compartilhadas
db = SQLAlchemy()
migrate = Migrate()
babel = Babel()

def get_locale():
    # Retorna o idioma com base nas preferências do navegador
    return request.accept_languages.best_match(['pt', 'en'])

def create_app(config_object=Config):
    app = Flask(__name__)
    
    # Configuração
    app.config.from_object(config_object)
    
    # Inicializa extensões
    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)
    babel.init_app(app, locale_selector=get_locale)
    
    # Importa e registra blueprints
    from app.routes import main_bp
    from app.routes import lead_bp  # Ajuste o caminho de importação conforme necessário
    
    app.register_blueprint(main_bp)
    app.register_blueprint(lead_bp)
    
    # Cria tabelas do banco de dados
    with app.app_context():
        db.create_all()
    
    @app.context_processor
    def inject_functions():
        return dict(get_locale=lambda: "pt-BR")
    
    return app