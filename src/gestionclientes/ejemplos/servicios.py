from gestionclientes.modulos.clientes.dominio.entidades import Itinerario
from gestionclientes.modulos.clientes.dominio.mixins import \
    FiltradoItinerariosMixin
from gestionclientes.modulos.clientes.dominio.objetos_valor import (
    Odo, ParametroBusca)
from gestionclientes.seedwork.dominio.servicios import Servicio


class ServicioBusqueda(Servicio, FiltradoItinerariosMixin):

    def buscar_itinerarios(self, odos: list[Odo], parametros: ParametroBusca) -> list[Itinerario]:
        pass