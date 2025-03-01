from gestionclientes.modulos.facturacion.infraestructura.despachadores import \
    Despachador
from gestionclientes.seedwork.aplicacion.handlers import Handler


class HandlerPagoIntegracion(Handler):

    @staticmethod
    def handle_pago_realizado(evento):
        print("Evento integración facturación: ", evento)
        print('================ PAGO REALIZADO INTEGRACIÓN ===========')
        despachador = Despachador()
        despachador.publicar_comando(evento, 'comandos-pago')
        
