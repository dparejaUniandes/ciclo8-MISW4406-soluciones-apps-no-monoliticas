""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de vuelos

"""

from dataclasses import dataclass, field

from notificaciones.modulos.notificaciones.dominio.repositorios import \
    RepositorioNotificaciones
from notificaciones.seedwork.dominio.fabricas import Fabrica
from notificaciones.seedwork.dominio.repositorios import Repositorio

from .excepciones import ExcepcionFabrica
from .repositorios import RepositorioNotificacionesSQLite
# from .repositorios_no_sqlalchemy import RepositorioNotificacionesPostgresqlNoSQLAlchemy
from .repositorios import RepositorioNotificaciones


@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioNotificaciones.__class__:
            return RepositorioNotificacionesSQLite()
        else:
            raise ExcepcionFabrica()