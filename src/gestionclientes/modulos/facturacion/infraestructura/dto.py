"""DTOs para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de vuelos

"""

from gestionclientes.config.db import db

Base = db.declarative_base()


class Facturacion(db.Model):
    __tablename__ = "facturacion"
    id = db.Column(db.String, primary_key=True)
    medio_pago = db.Column(db.String, nullable=False)
    id_cliente = db.Column(db.String, nullable=False)
    monto = db.Column(db.Float, nullable=False)
    