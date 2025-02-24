# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# db = None

# def init_db(app: Flask):
#     global db 
#     db = SQLAlchemy(app)


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

DB_HOST_URL = os.environ.get("DB_HOST_URL", "127.0.0.1:5432")
DB_NAME = os.environ.get("DB_NAME", "gestionclientes")
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "29062013")


def init_db(app: Flask):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'DATABASE_URL', f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST_URL}/{DB_NAME}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking for better performance
    
    db.init_app(app)