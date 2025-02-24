# ciclo8-MISW4406-soluciones-apps-no-monoliticas
En la materia de la maestría se aprenden conceptos relacionados a DDD y cómo crear aplicación no monolíticas

## Ejecutar Aplicación

Desde el directorio principal ejecute el siguiente comando.

```bash
flask --app src/gestionclientes/api run
```

Siempre puede ejecutarlo en modo DEBUG:

```bash
flask --app src/gestionclientes/api --debug run
```

### Nota
Existía un problema con la versión 3.0.2 de Flask-SQLAlchemy, por lo que se procede a bajar la versión a 2.5.1, esto porque los tests unitarios obtenían un problema `KeyError: <weakref at 0x00000251C4B1DAD0; to 'Flask' at 0x00000251C0ED3FA0>`, como se menciona en [Stack overflow](https://stackoverflow.com/questions/74366188/why-do-i-get-a-flask-weakref-error-when-importing-my-sqlalchemy-db-from-a-submod)


### Construcción de la Imagen Docker
Para construir la imagen sin utilizar caché, ejecuta:
```
docker build --no-cache -t flask_app .
```

### Ejecución del Contenedor
Para correr el contenedor en segundo plano (-d) y exponerlo en el puerto 5001, usa:
```
docker run -d -p 5001:5000 --name monolitica_flask_app flask_app
```

### Detener y Eliminar el Contenedor
Si necesitas detener y eliminar el contenedor, ejecuta:
```
docker stop monolitica_flask_app && docker rm monolitica_flask_app
```

### Recrear el Contenedor
```
docker stop monolitica_flask_app && docker rm monolitica_flask_app
docker build --no-cache -t flask_app .
docker run -d -p 5001:5000 --name monolitica_flask_app flask_app
```

### Ver Logs del Contenedor
Para inspeccionar los registros del contenedor en ejecución:
```
docker logs -f monolitica_flask_app
```

### Eliminar la Imagen Docker
Si necesitas eliminar la imagen de Docker completamente:
```
docker rmi flask_app

```

📌 Nota: Asegúrate de que no haya contenedores en ejecución usando esa imagen antes de eliminarla.