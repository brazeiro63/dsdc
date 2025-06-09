# app.py
from flask import Flask
from flask_cors import CORS
from app.config import Config
from app.models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Inicializa extensões
    CORS(app)
    db.init_app(app)
    
    # Registra blueprints
    from routes import lead_bp
    app.register_blueprint(lead_bp, url_prefix='/api')
    
    # Cria tabelas do banco de dados
    with app.app_context():
        db.create_all()
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)