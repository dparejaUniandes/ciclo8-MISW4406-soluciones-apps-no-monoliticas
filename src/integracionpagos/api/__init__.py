import os

from flask import Flask, jsonify
from flask_swagger import swagger


def registrar_handlers():
    import integracionpagos.modulos.pagos.aplicacion

def importar_modelos_alchemy():
    import integracionpagos.modulos.pagos.infraestructura.dto

def comenzar_consumidor(app):

    import threading

    import integracionpagos.modulos.pagos.infraestructura.consumidores as pago

    def run_with_context(target):
        with app.app_context():
            target()

    # Suscripción a eventos
    threading.Thread(target=lambda: run_with_context(pago.suscribirse_a_eventos), daemon=True).start()

    # Suscripción a comandos
    threading.Thread(target=lambda: run_with_context(pago.suscribirse_a_comandos), daemon=True).start()

def create_app(configuracion={}):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['TESTING'] = configuracion.get('TESTING')

     # Inicializa la DB
    from integracionpagos.config.db import init_db
    init_db(app)

    from integracionpagos.config.db import db

    importar_modelos_alchemy()
    registrar_handlers()

    app_context = app.app_context()
    app_context.push()
    with app.app_context():
        db.create_all()
        if not app.config.get('TESTING'):
            comenzar_consumidor(app) 

    # Importa Blueprints
    from . import pagos

    # Registro de Blueprints
    app.register_blueprint(pagos.bp)
    
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
