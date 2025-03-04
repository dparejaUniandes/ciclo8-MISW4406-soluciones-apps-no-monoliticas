import os
import threading
from flask import Flask, jsonify
from flask_swagger import swagger

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))


def registrar_handlers():
    """Registra los handlers de la aplicación."""
    import notificaciones.modulos.notificaciones.aplicacion


def importar_modelos_alchemy():
    """Importa los modelos de SQLAlchemy."""
    import notificaciones.modulos.notificaciones.infraestructura.dto


def comenzar_consumidor(app):
    """Comienza el consumidor dentro del contexto de la aplicación."""
    import notificaciones.modulos.notificaciones.infraestructura.consumidores as notificacion

    def run_with_context(target):
        with app.app_context():
            target()

    # Suscripción a eventos y comandos en hilos separados
    threading.Thread(target=lambda: run_with_context(notificacion.suscribirse_a_eventos), daemon=True).start()
    threading.Thread(target=lambda: run_with_context(notificacion.suscribirse_a_comandos), daemon=True).start()


def create_app(configuracion={}):
    """Crea y configura la aplicación Flask."""
    app = Flask(__name__, instance_relative_config=True)

    route = basedir
    if configuracion.get('TESTING'):
        route = configuracion["DATABASE"]

    # Configuración de la base de datos
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['TESTING'] = configuracion.get('TESTING')

    # Inicializa la base de datos
    from notificaciones.config.db import init_db, db
    init_db(app)

    # Importa modelos y handlers
    importar_modelos_alchemy()
    registrar_handlers()

    # Ejecuta en el contexto de la aplicación
    with app.app_context():
        db.create_all()
        if not app.config.get('TESTING'):
            comenzar_consumidor(app)

    # Rutas de la API
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