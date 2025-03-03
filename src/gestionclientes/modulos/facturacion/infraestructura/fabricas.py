""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de vuelos

"""

from dataclasses import dataclass, field

from gestionclientes.modulos.facturacion.dominio.repositorios import (
    RepositorioFacturacion, RepositorioFacturacionNoSQLAlchemy)
from gestionclientes.seedwork.dominio.fabricas import Fabrica
from gestionclientes.seedwork.dominio.repositorios import Repositorio

from .excepciones import ExcepcionFabrica
from .repositorios import RepositorioFacturacionPosgresql
from .repositorios_no_sqlalchemy import \
    RepositorioFacturacionPostgresqlNoSQLAlchemy


@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj.__name__ == RepositorioFacturacion.__name__:
            return RepositorioFacturacionPosgresql()
        elif obj.__name__ == RepositorioFacturacionNoSQLAlchemy.__name__:
            return RepositorioFacturacionPostgresqlNoSQLAlchemy()
        else:
            raise ExcepcionFabrica()