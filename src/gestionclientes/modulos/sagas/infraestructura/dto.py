"""DTOs para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de vuelos

"""

from gestionclientes.config.db import db

Base = db.declarative_base()


class SagaLog(db.Model):
    __tablename__ = "saga_log"
    id = db.Column(db.String, primary_key=True)
    id_cliente = db.Column(db.String, nullable=False)
    id_correlacion = db.Column(db.String, nullable=False)
    nombre_paso = db.Column(db.String, nullable=False)
    estado = db.Column(db.String, nullable=False)
    index = db.Column(db.Integer, nullable=False)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    