# 📌  ciclo8-MISW4406-soluciones-apps-no-monoliticas
En la materia de la maestría se aprenden conceptos relacionados a DDD y cómo crear aplicación no monolíticas

- Este proyecto utiliza Flask como framework web y PostgreSQL como base de datos. La aplicación puede ejecutarse tanto en un entorno local como en contenedores Docker.

## Vídeo

[Vídeo entrega]([https://uniandes-my.sharepoint.com/:v:/g/personal/d_pareja_uniandes_edu_co/EXrh8fZ4i5NMgyrcaS-AcxMBh1PMV-VZmhzlsWdOU0WrIg?e=lN80mg](https://uniandes-my.sharepoint.com/:v:/g/personal/l_mendozah_uniandes_edu_co/EcDCkehzhjJKr4mbspneXVkBIEJNxTC0OL0OqjNPW6kRsQ?e=vz5cfN))

https://uniandes-my.sharepoint.com/:v:/g/personal/l_mendozah_uniandes_edu_co/EcDCkehzhjJKr4mbspneXVkBIEJNxTC0OL0OqjNPW6kRsQ?e=vz5cfN

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
Para recrear el contenedor, usa:
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
```


# Explicación
Para la entrega 3 hemos decidido crear el microservicio para la gestión de clientes, en este se encuentran los módulos de clientes y facturación.
En el módulo de clientes podemos realizar varias acciones como:
* Crear un cliente
* Consultar un cliente por id
* Consultar el listado de todos los clientes

En el módulo de facturación podemos realizar un pago del cliente, este módulo permite el envío de un evento interno para que el módulo de clientes los pueda recibir, con esto, se pretenden que el cliente pueda actualizar el estado del plan con el estado que emite el módulo de facturación.

## Documentación de endpoints

En la raíz del proyecto se encuentra el archivo `Entrega 3.postman_collection.json` el cual se puede exportar en postman para probar los siguientes endpoints:

**Endpoint:** `/clientes/cliente` <br>
**Método:** POST <br>
**Descripción:** Permite la creación de un cliente, este endpoint hace uso de servicios para la integración interna de las acciones a realizar en el flujo de creación <br>
**Cuerpo:** 
```
{
    "nombre": "Pepito",
    "apellidos": "Pérez",
    "correo": "pepito@gmail.com",
    "contrasena": "12345"
}
```
<br>

**Endpoint:** `/clientes/cliente/<:id>` <br>
**Método:** GET <br>
**Descripción:** Permite la consulta de un cliente por id, este endpoint hace uso de servicios para la integración interna de las acciones a realizar en el flujo de consulta por id <br>
**Cuerpo:** N/A

<br>

**Endpoint:** `/clientes/cliente-query` <br>
**Método:** GET <br>
**Descripción:** Permite la consulta de todos los clientes almacenados en la base de datos, este endpoint hace uso de query para la integración interna de las acciones a realizar en el flujo de consulta <br>
**Cuerpo:** N/A

<br>

**Endpoint:** `/clientes/cliente-comando` <br>
**Método:** POST <br>
**Descripción:** Permite la creación de un cliente, este endpoint hace uso de comandos para la integración interna de las acciones a realizar en el flujo de creación <br>
**Cuerpo:** 
```
{
    "nombre": "Pepito",
    "apellidos": "Pérez",
    "correo": "pepito@gmail.com",
    "contrasena": "12345"
}
```

<br>

**Endpoint:** `/clientes/cliente-query/<:id>` <br>
**Método:** GET <br>
**Descripción:** Permite la consulta de un cliente por id, este endpoint hace uso de query para la integración interna de las acciones a realizar en el flujo de consulta por id <br>
**Cuerpo:** N/A

<br>

**Endpoint:** `/facturacion/realizar-pago-comando` <br>
**Método:** POST <br>
**Descripción:** Permite la realización de un pago, este endpoint hace uso de comando para la integración interna de las acciones a realizar en el flujo de realización de pago <br>
**Cuerpo:** 
```
{
    "medioPago": "TarjetaCredito",
    "idCliente": "17d00874-4d13-4613-8d22-ef905472b7c7",
    "monto": 24
}
```

<br>

**Endpoint:** `/facturacion/realizar-pago` <br>
**Método:** POST <br>
**Descripción:** Permite la realización de un pago, este endpoint hace uso de servicio para la integración interna de las acciones a realizar en el flujo de realización de pago <br>
**Cuerpo:** 
```
{
    "medioPago": "TarjetaCredito",
    "idCliente": "17d00874-4d13-4613-8d22-ef905472b7c7",
    "monto": 24
}
```


