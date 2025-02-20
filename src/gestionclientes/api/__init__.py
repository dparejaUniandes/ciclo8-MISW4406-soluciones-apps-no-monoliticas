import os

from flask import Flask, jsonify
from flask_swagger import swagger

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))

def importar_modelos_alchemy():
    import gestionclientes.modulos.clientes.infraestructura.dto

def create_app(configuracion=None):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)

    route = basedir
    if configuracion is not None and configuracion["TESTING"]:
        route = configuracion["DATABASE"]

    # Configuracion de BD
    app.config['SQLALCHEMY_DATABASE_URI'] =\
            'sqlite:///' + os.path.join(route, 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    print("***Config: ", app.config['SQLALCHEMY_DATABASE_URI'])
     # Inicializa la DB
    from gestionclientes.config.db import init_db
    init_db(app)

    from gestionclientes.config.db import db

    importar_modelos_alchemy()

    app_context = app.app_context()
    app_context.push()
    # with app.app_context():
    db.create_all()

     # Importa Blueprints
    from . import clientes

    # Registro de Blueprints
    app.register_blueprint(clientes.bp)

    @app.route("/spec")
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "My API"
        return jsonify(swag)

    @app.route("/health")
    def health():
        return {"status": "up"}

    return app
