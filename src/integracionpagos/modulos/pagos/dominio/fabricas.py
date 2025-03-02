""" Fábricas para la creación de objetos del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de vuelos

"""

from dataclasses import dataclass

from integracionpagos.seedwork.dominio.entidades import Entidad
from integracionpagos.seedwork.dominio.fabricas import Fabrica
from integracionpagos.seedwork.dominio.repositorios import (Mapeador,
                                                            Repositorio)

from .entidades import Pago
from .excepciones import TipoObjetoNoExisteEnDominioPagosExcepcion


@dataclass
class _FabricaPago(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            pago: Pago = mapeador.dto_a_entidad(obj)
            return pago

@dataclass
class FabricaPago(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Pago.__class__:
            fabrica_pago = _FabricaPago()
            return fabrica_pago.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioPagosExcepcion()

