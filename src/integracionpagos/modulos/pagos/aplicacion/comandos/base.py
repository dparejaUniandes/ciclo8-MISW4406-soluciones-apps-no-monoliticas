from integracionpagos.modulos.pagos.dominio.fabricas import FabricaPago
from integracionpagos.modulos.pagos.infraestructura.fabricas import \
    FabricaRepositorio
from integracionpagos.seedwork.aplicacion.comandos import ComandoHandler


class PagoBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_pagos: FabricaPago = FabricaPago()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_pagos(self):
        return self._fabrica_pagos    
    