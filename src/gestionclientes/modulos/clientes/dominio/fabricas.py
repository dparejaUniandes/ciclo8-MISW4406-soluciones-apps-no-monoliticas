""" Fábricas para la creación de objetos del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de vuelos

"""

from dataclasses import dataclass

from gestionclientes.seedwork.dominio.entidades import Entidad
from gestionclientes.seedwork.dominio.fabricas import Fabrica
from gestionclientes.seedwork.dominio.repositorios import Mapeador, Repositorio

from .entidades import Cliente
from .excepciones import TipoObjetoNoExisteEnDominioVuelosExcepcion


@dataclass
class _FabricaCliente(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            cliente: Cliente = mapeador.dto_a_entidad(obj)
            return cliente

@dataclass
class FabricaClientes(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Cliente.__class__:
            fabrica_cliente = _FabricaCliente()
            return fabrica_cliente.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioVuelosExcepcion()

