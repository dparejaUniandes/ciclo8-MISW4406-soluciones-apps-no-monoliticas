from gestionclientes.modulos.sagas.aplicacion.coordinadores.saga_sta import \
    oir_mensaje
from gestionclientes.seedwork.aplicacion.handlers import Handler


class HandlerSagaDominio(Handler):

    @staticmethod
    def handle_pago_realizado_correcto(evento):
        print("Saga Handler handle_pago_realizado_correcto: ", evento)
        oir_mensaje(evento)
    
    @staticmethod
    def handle_pago_realizado_revertido(evento):
        print("Saga Handler handle_pago_realizado_revertido: ", evento)
        oir_mensaje(evento)

    @staticmethod
    def handle_factura_creada_correcto(evento):
        print("Saga Handler handle_factura_creada_correcto: ", evento)
        oir_mensaje(evento)
    
    @staticmethod
    def handle_factura_creada_revertido(evento):
        print("Saga Handler handle_factura_creada_revertido: ", evento)
        oir_mensaje(evento)
    
    @staticmethod
    def handle_notificacion_creada_correcto(evento):
        print("Saga Handler handle_notificacion_creada_correcto: ", evento)
        oir_mensaje(evento)
    
    @staticmethod
    def handle_notificacion_creada_revertido(evento):
        print("Saga Handler handle_notificacion_creada_revertido: ", evento)
        oir_mensaje(evento)

    