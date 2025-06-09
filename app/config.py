# config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'chave-secreta-temporaria'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://dsdc_user:deumaoito@localhost:5433/dsdc_database'
    SQLALCHEMY_TRACK_MODIFICATIONS = False