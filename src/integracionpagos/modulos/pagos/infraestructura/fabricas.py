""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de vuelos

"""

from dataclasses import dataclass, field

from integracionpagos.modulos.pagos.dominio.repositorios import (
    RepositorioPagos, RepositorioPagosNoSQLAlchemy)
from integracionpagos.seedwork.dominio.fabricas import Fabrica
from integracionpagos.seedwork.dominio.repositorios import Repositorio

from .excepciones import ExcepcionFabrica
from .repositorios import RepositorioPagosPostgresql
from .repositorios_no_sqlalchemy import RepositorioPagosPostgresqlNoSQLAlchemy


@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioPagosNoSQLAlchemy.__class__:
            return RepositorioPagosPostgresqlNoSQLAlchemy()
        else:
            raise ExcepcionFabrica()