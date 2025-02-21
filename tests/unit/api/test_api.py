import json
import os
import tempfile

import pytest

from gestionclientes.api import create_app, importar_modelos_alchemy
from gestionclientes.config.db import init_db

db_dir = os.path.abspath(os.path.dirname(__file__))

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # create a temporary file to isolate the database for each test
    db_fd, db_path = tempfile.mkstemp()
    # create the app with common test config
    app = create_app({"TESTING": True, "DATABASE": db_dir})

    importar_modelos_alchemy()

    # create the database and load test data
    with app.app_context():
        init_db(app)

        from gestionclientes.config.db import db

        importar_modelos_alchemy()
        db.create_all()

    yield app

    # close and remove the temporary database
    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()

def test_servidor_levanta(client):

    # Dado un cliente a endpoint health
    rv = client.get('/health')

    # Devuelve estados the UP el servidor
    assert rv.data is not None
    assert rv.status_code == 200

    response = json.loads(rv.data)

    assert response['status'] == 'up'


def cliente_correcto():
    return {
        "nombre": "Pepe"
    }

def test_cliente(client):
    rv = client.post('/clientes/cliente', data=json.dumps(cliente_correcto()), content_type='application/json')
    print("Resp***: ", rv)
    response = rv.json
    assert rv is not None
    assert response['nombre'] == 'Pepe'
