"""DTOs para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de vuelos

"""

from notificaciones.config.db import db
from notificaciones.modulos.notificaciones.dominio.objetos_valor import TipoMedio

Base = db.declarative_base()


class Notificacion(db.Model):
    __tablename__ = "notificaciones"
    id = db.Column(db.String, primary_key=True)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
    tipo = db.Column(db.String, nullable=False)
    valor = db.Column(db.String, nullable=False)
    medio = db.Column(db.Enum(TipoMedio), nullable=False)
