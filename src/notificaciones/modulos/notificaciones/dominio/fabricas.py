""" Fábricas para la creación de objetos del dominio de notificaciones

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de notificaciones

"""

from dataclasses import dataclass

from notificaciones.seedwork.dominio.entidades import Entidad
from notificaciones.seedwork.dominio.fabricas import Fabrica
from notificaciones.seedwork.dominio.repositorios import Mapeador

from .entidades import Notificacion
from .excepciones import TipoObjetoNoExisteEnDominioVuelosExcepcion


@dataclass
class _FabricaNotificacion(Fabrica):
    def crear_objeto(self, obj: any, 
                     mapeador: Mapeador) -> any:
        """ Crea un objeto del dominio de notificaciones """
        if type(obj) is list and len(obj) == 0:
            return []
        if isinstance(obj, Entidad) or (type(obj) is list and isinstance(obj[0], Entidad)):
            return mapeador.entidad_a_dto(obj)
        else:
            notificacion: Notificacion = mapeador.dto_a_entidad(obj)
            return notificacion


@dataclass
class FabricaNotificaciones(Fabrica):
    """ Fábrica de notificaciones """

    def crear_objeto(self, obj: any, 
                     mapeador: Mapeador) -> any:
        """ Crea un objeto del dominio de notificaciones """
        if mapeador.obtener_tipo() == Notificacion.__class__:
            fabrica_notificacion = _FabricaNotificacion()
            return fabrica_notificacion.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioVuelosExcepcion()
