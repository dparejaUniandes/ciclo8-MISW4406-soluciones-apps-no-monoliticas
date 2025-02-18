from aeroalpes.modulos.vuelos.dominio.entidades import Itinerario
from aeroalpes.modulos.vuelos.dominio.mixins import FiltradoItinerariosMixin
from aeroalpes.modulos.vuelos.dominio.objetos_valor import Odo, ParametroBusca
from aeroalpes.seedwork.dominio.servicios import Servicio


class ServicioBusqueda(Servicio, FiltradoItinerariosMixin):

    def buscar_itinerarios(self, odos: list[Odo], parametros: ParametroBusca) -> list[Itinerario]:
        pass