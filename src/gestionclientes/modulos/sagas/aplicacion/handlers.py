from gestionclientes.modulos.sagas.aplicacion.coordinadores.saga_sta import \
    oir_mensaje
from gestionclientes.seedwork.aplicacion.handlers import Handler


class HandlerSagaDominio(Handler):

    @staticmethod
    def handle_pago_realizado_correcto(evento):
        print("Saga Handler handle_pago_realizado_correcto: ", evento)
        print('================ PAGO REALIZADO correcto, se emite evento desde integracionpagos ===========')
        oir_mensaje(evento)
    
    @staticmethod
    def handle_pago_realizado_revertido(evento):
        print("Saga Handler handle_pago_realizado_revertido: ", evento)
        print('================ PAGO REALIZADO revertido, se emite evento desde integracionpagos ===========')
        oir_mensaje(evento)

    @staticmethod
    def handle_factura_creada_correcto(evento):
        print("Saga Handler handle_pago_realizado_correcto: ", evento)
        print('================ PAGO REALIZADO correcto, se emite evento desde integracionpagos ===========')
        oir_mensaje(evento)
    
    @staticmethod
    def handle_factura_creada_revertido(evento):
        print("Saga Handler handle_pago_realizado_revertido: ", evento)
        print('================ PAGO REALIZADO revertido, se emite evento desde integracionpagos ===========')
        oir_mensaje(evento)

    