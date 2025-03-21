"""DTOs para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de vuelos

"""

from gestionclientes.config.db import db
from gestionclientes.modulos.clientes.dominio.objetos_valor import EstadoPlan

Base = db.declarative_base()


class Cliente(db.Model):
    __tablename__ = "clientes"
    id = db.Column(db.String, primary_key=True)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
    nombre = db.Column(db.String, nullable=False)
    apellidos = db.Column(db.String, nullable=False)
    correo = db.Column(db.String, nullable=False)
    contrasena = db.Column(db.String, nullable=False)
    estado_plan = db.Column(db.Enum(EstadoPlan), nullable=False)
    