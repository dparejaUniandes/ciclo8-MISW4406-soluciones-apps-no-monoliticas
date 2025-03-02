"""DTOs para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de vuelos

"""

from integracionpagos.config.db import db

Base = db.declarative_base()


class Pago(db.Model):
    __tablename__ = "pagos"
    id = db.Column(db.String, primary_key=True)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
    id_cliente = db.Column(db.String, nullable=False)
    monto = db.Column(db.Float, nullable=False)
    estado_pago = db.Column(db.String, nullable=False)
    pasarela_pago = db.Column(db.String, nullable=False)