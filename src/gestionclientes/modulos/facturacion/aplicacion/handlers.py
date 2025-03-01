from gestionclientes.modulos.clientes.aplicacion.comandos.actualizar_cliente import \
    ActualizarCliente
from gestionclientes.seedwork.aplicacion.comandos import ejecutar_commando
from gestionclientes.seedwork.aplicacion.handlers import Handler


class HandlerPagoIntegracion(Handler):

    @staticmethod
    def handle_pago_realizado(evento):
        print("Evento integración facturación: ", evento)
        print('================ PAGO REALIZADO INTEGRACIÓN ===========')

    