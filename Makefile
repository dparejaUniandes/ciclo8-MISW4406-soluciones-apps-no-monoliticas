# Variables de Entorno
# Estas variables permiten gestionar el entorno virtual y las dependencias del proyecto.
VENV_DIR=venv
PYTHON=$(VENV_DIR)/bin/python
PIP=$(VENV_DIR)/bin/pip

# Crear y activar el entorno virtual
# Crea un entorno virtual en el directorio venv.
# Luego, actualiza pip para asegurar que se usen las últimas versiones de los paquetes.
venv:
	python3 -m venv $(VENV_DIR)
	$(PIP) install --upgrade pip --extra-index-url https://pypi.org/simple

# Instalar dependencias
# Instala las dependencias del proyecto desde el archivo requirements.txt.	
# Evita el uso de la caché para asegurar que se instalen las últimas versiones de los paquetes.
install: venv
	$(PIP) install --no-cache-dir -r requirements.txt --extra-index-url https://pypi.org/simple


#  Ejecutar la API Localmente con Recarga Automática
#  Activa el entorno virtual.
#  Ejecuta la aplicación Flask con autorecarga.
run:
	export FLASK_APP=src/gestionclientes/api; \
	. $(VENV_DIR)/bin/activate && flask --app src/gestionclientes/api run


# Eliminar el entorno virtual
# Elimina el directorio venv y los archivos __pycache__.
clean:
	rm -rf $(VENV_DIR) __pycache__


# Regenerar el entorno virtual y reinstalar dependencias
# Borra el entorno virtual, lo recrea e instala las dependencias desde cero.
reset: clean venv install


# Eliminar volumnes de docker
# Detiene y elimina los contenedores junto con los volúmenes persistentes.
clean-compose:	
	docker-compose down -v


#  Ejecutar la Aplicación con Docker Compose
#  Levanta los servicios con docker-compose.
#  Fuerza la reconstrucción de las imágenes antes de ejecutarlas.
run-compose:
	docker-compose up --build
