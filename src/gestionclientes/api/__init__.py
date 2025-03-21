import os

from flask import Flask, jsonify
from flask_swagger import swagger

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))

def registrar_handlers():
    import gestionclientes.modulos.clientes.aplicacion
    import gestionclientes.modulos.facturacion.aplicacion
    import gestionclientes.modulos.sagas.aplicacion

def importar_modelos_alchemy():
    import gestionclientes.modulos.clientes.infraestructura.dto
    import gestionclientes.modulos.facturacion.infraestructura.dto

def comenzar_consumidor(app):

    import threading

    import gestionclientes.modulos.facturacion.infraestructura.consumidores as facturacion
    import gestionclientes.modulos.sagas.infraestructura.consumidores as saga


    def run_with_context(target):
        with app.app_context():
            target()

    # Suscripción a eventos
    threading.Thread(target=lambda: run_with_context(facturacion.suscribirse_a_eventos), daemon=True).start()
    threading.Thread(target=lambda: run_with_context(facturacion.suscribirse_a_comandos_saga), daemon=True).start()
    threading.Thread(target=lambda: run_with_context(saga.suscribirse_a_eventos), daemon=True).start()
    threading.Thread(target=lambda: run_with_context(saga.suscribirse_a_eventos_facturacion), daemon=True).start()
    threading.Thread(target=lambda: run_with_context(saga.suscribirse_a_eventos_notificacion), daemon=True).start()

    # Suscripción a comandos
    threading.Thread(target=lambda: run_with_context(facturacion.suscribirse_a_comandos), daemon=True).start()
    threading.Thread(target=lambda: run_with_context(facturacion.suscribirse_a_comandos_bff), daemon=True).start()

def create_app(configuracion={}):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)

    route = basedir
    if configuracion.get('TESTING'):
        route = configuracion["DATABASE"]

    # Configuracion de BD
    # app.config['SQLALCHEMY_DATABASE_URI'] =\
    #         'sqlite:///' + os.path.join(route, 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['TESTING'] = configuracion.get('TESTING')

     # Inicializa la DB
    from gestionclientes.config.db import init_db
    init_db(app)

    from gestionclientes.config.db import db

    importar_modelos_alchemy()
    registrar_handlers()

    app_context = app.app_context()
    app_context.push()
    with app.app_context():
        db.create_all()
        if not app.config.get('TESTING'):
            comenzar_consumidor(app) 

     # Importa Blueprints
    from . import clientes, facturacion

    # Registro de Blueprints
    app.register_blueprint(clientes.bp)
    app.register_blueprint(facturacion.bp)
    
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
