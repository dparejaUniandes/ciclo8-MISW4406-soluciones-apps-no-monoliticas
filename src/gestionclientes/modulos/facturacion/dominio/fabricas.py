""" Fábricas para la creación de objetos del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de vuelos

"""

from dataclasses import dataclass

from gestionclientes.seedwork.dominio.entidades import Entidad
from gestionclientes.seedwork.dominio.fabricas import Fabrica
from gestionclientes.seedwork.dominio.repositorios import Mapeador, Repositorio

from .entidades import Facturacion
from .excepciones import TipoObjetoNoExisteEnDominioFacturacionExcepcion


@dataclass
class _FabricaFacturacion(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if type(obj) is list and len(obj) == 0:
            return []
        if isinstance(obj, Entidad) or (type(obj) is list and isinstance(obj[0], Entidad)):
            return mapeador.entidad_a_dto(obj)
        else:
            facturacion: Facturacion = mapeador.dto_a_entidad(obj)
            return facturacion

@dataclass
class FabricaFacturacion(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Facturacion.__class__:
            fabrica_facturacion = _FabricaFacturacion()
            return fabrica_facturacion.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioFacturacionExcepcion()

