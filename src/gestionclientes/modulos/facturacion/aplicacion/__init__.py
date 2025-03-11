from pydispatch import dispatcher

from gestionclientes.modulos.facturacion.dominio.eventos import \
    FacturacionCreada

from .handlers import HandlerPagoIntegracion

dispatcher.connect(HandlerPagoIntegracion.handle_pago_realizado, signal=f'{FacturacionCreada.__name__}Integracion')
