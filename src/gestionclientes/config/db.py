import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DB_PORT = os.environ.get("DB_PORT", "5432")
DB_HOST_URL = os.environ.get("DB_HOST_URL", "127.0.0.1")
DB_NAME = os.environ.get("DB_NAME", "gestionclientes")
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "12345")

def init_db(app: Flask):
    app.config['SQLALCHEMY_DATABASE_URI'] =  f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST_URL}:{DB_PORT}/{DB_NAME}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking for better performance
    
    db.init_app(app)