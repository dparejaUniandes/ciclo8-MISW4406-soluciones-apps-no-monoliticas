# 📌  ciclo8-MISW4406-soluciones-apps-no-monoliticas
En la materia de la maestría se aprenden conceptos relacionados a DDD y cómo crear aplicación no monolíticas

- Este proyecto utiliza Flask como framework web y PostgreSQL como base de datos. La aplicación puede ejecutarse tanto en un entorno local como en contenedores Docker.

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


## 🐳 Ejecución con Docker Compose

- ### 🔹 Construir y Levantar los Contenedores

    Si deseas ejecutar la aplicación usando Docker Compose, puedes hacerlo con el siguiente comando:
    - ```
        make run-compose
    ```

    Esto construirá las imágenes y levantará los contenedores de Flask y PostgreSQL.

    📝 Nota: La aplicación se ejecutará en http://localhost:5001/ y la base de datos en el puerto 5433.

- ### 🔹 Detener y Limpiar Contenedores

    Si deseas detener los contenedores y eliminar los volúmenes de la base de datos, usa:
    - ```
        make clean-compose
    ```
    Esto eliminará los datos almacenados en postgres_data.


## Ejecución del API con docker 
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

docker run -d -p 5001:5000 \
  -e FLASK_APP=src/gestionclientes/api \
  -e FLASK_ENV=development \
  -e DB_HOST_URL=db-postgres \
  -e DB_NAME=gestionclientes \
  -e DB_USER=postgres \
  -e DB_PASSWORD=12345 \
  -e DB_PORT=5432 \
  --name monolitica_flask_app flask_app
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




```
📄 Notas Finales


📌 Esta documentación está diseñada para facilitar la instalación y ejecución de la aplicación tanto en entornos locales como en Docker.

- Asegúrate de que no haya contenedores en ejecución usando una imagen antes de eliminarla.

- Si tienes problemas o dudas, revisa los logs con:
    docker container logs <nombre_del_contenedor>