import os

from flask import Flask, jsonify
from flask_swagger import swagger

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))


def registrar_handlers():
    """ Registra los handlers de la aplicacion """
    import notificaciones.modulos.notificaciones.aplicacion


def importar_modelos_alchemy():
    """ Importa los modelos de alchemy """
    import notificaciones.modulos.notificaciones.infraestructura.dto


def comenzar_consumidor():
    """ Comienza el consumidor """
    import threading

    import notificaciones.modulos.notificaciones.infraestructura.consumidores as notificacion

    # Suscripción a eventos
    threading.Thread(target=notificacion.suscribirse_a_eventos).start()

    # Suscripción a comandos
    threading.Thread(target=notificacion.suscribirse_a_comandos).start()


def create_app(configuracion={}):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)

    route = basedir
    if configuracion.get('TESTING'):
        route = configuracion["DATABASE"]

    # Configuracion de BD
    app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(route, 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['TESTING'] = configuracion.get('TESTING')

    # Inicializa la DB
    from notificaciones.config.db import init_db
    from notificaciones.config.db import db

    init_db(app)

    # importar_modelos_alchemy()
    # registrar_handlers()

    # app_context = app.app_context()
    # app_context.push()
    # # with app.app_context():
    # db.create_all()

    # # Importa Blueprints
    # from . import notificacion

    # # Registro de Blueprints
    # app.register_blueprint(notificacion.bp)
    importar_modelos_alchemy()
    registrar_handlers()

    app_context = app.app_context()
    app_context.push()
    with app.app_context():
        db.create_all()
        if not app.config.get('TESTING'):
            comenzar_consumidor()

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
