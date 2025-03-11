from gestionclientes.modulos.clientes.aplicacion.comandos.actualizar_cliente import \
    ActualizarCliente
from gestionclientes.seedwork.aplicacion.comandos import ejecutar_commando
from gestionclientes.seedwork.aplicacion.handlers import Handler


class HandlerClienteDominio(Handler):

    @staticmethod
    def handle_pago_realizado(sender, evento):
        print("Desde cliente: ", evento)
        print('================ PAGO REALIZADO desde clientes, se emite evento desde facturación ===========')
        comando = ActualizarCliente(
            id=evento.id_cliente,
            estadoPlan=evento.estado
        )
        ejecutar_commando(comando)

    