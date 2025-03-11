# 📌  ciclo8-MISW4406-soluciones-apps-no-monoliticas

Este proyecto es una solución basada en la arquitectura de microservicios utilizando Domain-Driven Design (DDD), y está enfocado en la creación de aplicaciones no monolíticas. El objetivo es proporcionar un conjunto de servicios para la gestión de clientes y facturación, utilizando tecnologías como Flask, PostgreSQL, y Docker.

# ENTREGA 5
por favor tener presente los comandos descritos en las entregas previas para ejecutar el proyecto en local.

## Arquitectura general
### Microservicios
* **BFF**: Permite la interacción con los usuarios, la acción a ejecutar es realizar pago
* **Gestión clientes**: Internamente contiene los módulos de clientes, facturación y sagas. El módulo de facturación procesa el comando de realizar pago emitido por el bff, la saga se encarga degestionar los pasos o transacciones realizadas en gestioncliestes, integracionpagos y notificaciones. Clientes se conserva como se menciona con la entrega 3.
* **Integración pagos**: Recibe el comando de realizar pago, guarda en bd el pago y emite un evento de pago confirmado.
* **Notificaciones**: Almacena las notificaciones que se deben enviar a los usuarios, emite eventos que permite conocer si la notificación fue correcta a hubo una notificación de reversión, estos eventos los escucha la saga.

<br>

<img width="1333" alt="image" src="https://github.com/user-attachments/assets/134e7e1e-ab56-4836-aa60-ffae8fc385f4" />

<br>

### Saga 

<img width="1642" alt="image" src="https://github.com/user-attachments/assets/4105bc0d-714c-403d-a7b3-a70b1cb1fc17" />



# ENTREGA 4

Este proyecto es una solución basada en la arquitectura de microservicios utilizando Domain-Driven Design (DDD), y está enfocado en la creación de aplicaciones no monolíticas. El objetivo es proporcionar un conjunto de servicios para la gestión de clientes y facturación, utilizando tecnologías como Flask, PostgreSQL, y Docker.

## ENLACE VIDEO

[Video](https://uniandes-my.sharepoint.com/:v:/g/personal/d_pareja_uniandes_edu_co/EVDgaw5ycNJNtgtH2uWm9JkBgejnmIoPSs3Cuk9pD_aHog?e=ausKOJ)

### 1. Arquitectura General
El proyecto está diseñado bajo el patrón de microservicios, dividido en módulos que permiten una gestión modularizada de los distintos aspectos del sistema. Los principales módulos son:

[Diagrama de arquitectura](https://excalidraw.com/#room=e5b32f4d90ffe8b83d7b,HzWcY7ddsq1vONTdtmts4A)

<br>

<img width="1234" alt="image" src="https://github.com/user-attachments/assets/9c8f5ba1-75e4-4eaa-b3dd-4a04a0bc01cc" />

<br>

*Imagen de la arquitectura realizada para la entrega 4*

<br>

- **bff_web**: Backend for Frontend (BFF), se encarga de manejar la comunicación entre el frontend y los microservicios del backend. Actúa como una capa intermedia para optimizar y simplificar la interacción entre la interfaz de usuario y los microservicios.

- **GestionClientes**: Responsable de la gestión de clientes, incluyendo funcionalidades como creación, consulta y actualización de clientes.
- **Facturación**: Gestiona el proceso de pagos, incluyendo la integración con los clientes para actualizar su estado de plan.
- **Notificaciones**: Envía notificaciones al sistema para alertar sobre eventos importantes.
- **IntegraciónPagos**: Encargado de gestionar la integración del pago, con eventos que se emiten al módulo de clientes para realizar actualizaciones en su estado.
- **Seedwork**: Un conjunto de clases y utilidades que definen comportamientos y servicios comunes utilizados por los demás módulos, como manejo de excepciones, comandos, consultas, etc.

### 2. Descripción de las Tecnologías Utilizadas

- **Flask**: Framework utilizado para la creación de la API RESTful.
- **PostgreSQL**: Base de datos utilizada para almacenar la información de clientes y facturación.
- **Docker**: Contenerización del proyecto, lo que facilita su ejecución en distintos entornos.
- **Python**: Lenguaje de programación utilizado para desarrollar los microservicios.

### 3. Estructura de Carpetas
El proyecto está organizado en módulos que contienen el código fuente y las configuraciones necesarias. Los módulos clave incluyen:

- **gestionclientes**: Módulo principal que gestiona la creación, consulta y actualización de clientes.
- **facturacion**: Módulo de facturación que gestiona los pagos y actualiza el estado de los clientes.
- **notificaciones**: Módulo que gestiona el envío de notificaciones dentro del sistema.
- **integracionpagos**: Módulo responsable de la integración con los pagos, emitiendo eventos hacia otros módulos.
- **seedwork**: Contiene clases y utilidades comunes como el manejo de excepciones, comandos y consultas.

### 4. Flujo de Datos y Comunicaciones Entre Módulos
- **API de Clientes**: Permite la creación y consulta de clientes, tanto de manera sincrónica como asincrónica, usando comandos y consultas.
- **Facturación**: Los pagos se gestionan mediante un servicio que interactúa con el módulo de clientes para actualizar su estado de plan.
- **Eventos Internos**: La comunicación entre los módulos se realiza mediante eventos. Por ejemplo, al realizar un pago, un evento es emitido para notificar al módulo de clientes que se debe actualizar el estado del plan.

## Instrucciones para Ejecutar el Proyecto

### 1. Ejecutar la Aplicación en un Entorno Local
Desde el directorio principal, puedes ejecutar la aplicación utilizando el siguiente comando:

```bash
flask --app src/gestionclientes/api run
```
Si deseas ejecutar en modo DEBUG, usa:

```bash
flask --app src/gestionclientes/api --debug run --reload
```

#### Ejecución de PULSAR
```bash
docker-compose --profile pulsar up
```

#### Ejecución de Notificaciones & Base de datos
```bash
flask --app src/notificaciones/api run --port 6000 --reload
```

#### Ejecutar Postgres con Docker
```
docker-compose -f docker-compose-db.yml up
```

Ingresar a la instancia de postgres y reemplazar `id_instancia_docker`
```
 docker exec -it id_instancia_docker bash
```

Ingresar a la BD
```
psql -U postgres -d notificaciones
```

#### Ejecución de Integración de pagos
```bash
flask --app src/integracionpagos/api run --port 7000 --reload
```


#### Ejecución de BFF
Se debe ingresar a la carpeta src y ejecutar <br>
```bash
uvicorn bff_web.main:app --host localhost --port 8003 --reload
```

### 2. Ejecutar la Aplicación con Docker
#### Construir y Levantar los Contenedores

Si deseas ejecutar la aplicación usando Docker Compose, ejecuta:


```bash
make run-compose
```

Esto construirá las imágenes de Docker y levantará los contenedores necesarios, incluyendo Flask y PostgreSQL. La aplicación estará disponible en http://localhost:5001/ y la base de datos en el puerto 5433.

Detener y Limpiar Contenedores
Para detener y eliminar los contenedores y volúmenes, utiliza:

```bash
make clean-compose
```

### 3. Ejecutar la Aplicación con Docker (sin Compose)
Para construir y ejecutar la aplicación en un contenedor Docker:

```bash
docker build --no-cache -t flask_app .
docker run -d -p 5001:5000 --name monolitica_flask_app flask_app
```

Para detener y eliminar el contenedor:


```bash
docker stop monolitica_flask_app && docker rm monolitica_flask_app
```

### Documentación de Endpoints

Los endpoints principales de la API están documentados a través de la colección de Postman, ubicada en el archivo Entrega 3.postman_collection.json. Algunos de los endpoints más importantes incluyen:

/clientes/cliente (POST): Crea un nuevo cliente.
/clientes/cliente/<id> (GET): Consulta un cliente por su ID.
/facturacion/realizar-pago (POST): Realiza un pago utilizando el servicio de facturación.

Puedes importar esta colección en Postman para probar los endpoints directamente.

## Notas Finales
Este proyecto está diseñado para ser fácil de implementar en entornos locales o en contenedores Docker, y sigue principios de Domain-Driven Design (DDD) y microservicios para garantizar una arquitectura escalable y mantenible. Asegúrate de revisar los logs y seguir las instrucciones del Dockerfile para facilitar la instalación.




_____________________________________________


# ENTREGA 1

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


# ENTREGA 2

### Correr docker-compose usando profiles
```bash
docker-compose --profile pulsar up
```

## Ejecutar Aplicación

Desde el directorio principal ejecute el siguiente comando. (ver en la entrega 1 para la ejecución de gestionclientes)

```bash
python src/integracionpagos/main.py 
flask --app src/integracionpagos/api run 
```

Siempre puede ejecutarlo en modo DEBUG:

```bash
python src/integracionpagos/main.py 
flask --app src/integracionpagos/api --debug run
```




# ENTREGA 3

## Explicación
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
