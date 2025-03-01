""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de vuelos

"""

from dataclasses import dataclass, field

from gestionclientes.modulos.clientes.dominio.repositorios import \
    RepositorioClientes
from gestionclientes.seedwork.dominio.fabricas import Fabrica
from gestionclientes.seedwork.dominio.repositorios import Repositorio

from .excepciones import ExcepcionFabrica
from .repositorios import RepositorioNotificacionesSQLite


@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioClientes.__class__:
            return RepositorioNotificacionesSQLite()
        else:
            raise ExcepcionFabrica()