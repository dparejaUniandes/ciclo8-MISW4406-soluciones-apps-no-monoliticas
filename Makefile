# Variables
VENV_DIR=venv
PYTHON=$(VENV_DIR)/bin/python
PIP=$(VENV_DIR)/bin/pip

# Crear y activar el entorno virtual
venv:
	python3 -m venv $(VENV_DIR)
	$(PIP) install --upgrade pip --extra-index-url https://pypi.org/simple
# Instalar dependencias
install: venv
	$(PIP) install -r requirements.txt --extra-index-url https://pypi.org/simple
# Ejecutar la API en local con recarga automática
run:
	. $(VENV_DIR)/bin/activate && flask --app src/gestionclientes/api run
# Eliminar el entorno virtual
clean:
	rm -rf $(VENV_DIR) __pycache__
# Regenerar el entorno virtual y reinstalar dependencias
reset: clean venv install