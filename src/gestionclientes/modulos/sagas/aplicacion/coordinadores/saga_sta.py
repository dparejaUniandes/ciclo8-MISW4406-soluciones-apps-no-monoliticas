from gestionclientes.modulos.sagas.aplicacion.comandos.facturacion import (
    CrearFacturacion, RevertirFacturacion)
from gestionclientes.modulos.sagas.aplicacion.comandos.notificaciones import (
    CrearNotificacion, RevertirNotificacion)
from gestionclientes.modulos.sagas.aplicacion.comandos.pagos import (
    RealizarPago, RevertirPago)
from gestionclientes.modulos.sagas.dominio.eventos.facturacion import (
    FacturacionCreada, FacturacionFallida, FacturacionRevertida)
from gestionclientes.modulos.sagas.dominio.eventos.notificacion import (
    NotificacionCreada, NotificacionFallida, NotificacionRevertida)
from gestionclientes.modulos.sagas.dominio.eventos.pagos import (PagoFallido,
                                                                 PagoRealizado,
                                                                 PagoRevertido)
from gestionclientes.seedwork.aplicacion.comandos import Comando
from gestionclientes.seedwork.aplicacion.sagas import (CoordinadorOrquestacion,
                                                       Fin, Inicio,
                                                       Transaccion)
from gestionclientes.seedwork.dominio.eventos import EventoDominio


class CoordinadorReservas(CoordinadorOrquestacion):

    def inicializar_pasos(self, id_correlacion):
        self.pasos = [
            Inicio(index=0, id_correlacion=id_correlacion),
            Transaccion(
                index=1, 
                comando=CrearFacturacion, 
                evento=FacturacionCreada, 
                error=FacturacionFallida, 
                compensacion=RevertirFacturacion, 
                id_correlacion=id_correlacion
            ),
            Transaccion(
                index=2, 
                comando=RealizarPago, 
                evento=PagoRealizado, 
                error=PagoFallido, 
                compensacion=RevertirPago,
                id_correlacion=id_correlacion
            ),
            Transaccion(
                index=3, 
                comando=CrearNotificacion, 
                evento=NotificacionCreada, 
                error=NotificacionFallida, 
                compensacion=RevertirNotificacion,
                id_correlacion=id_correlacion
            ),
            Fin(index=4, id_correlacion=id_correlacion)
        ]

    def iniciar(self):
        self.persistir_en_saga_log(self.pasos[0])
    
    def terminar(self):
        self.persistir_en_saga_log(self.pasos[-1])

    def persistir_en_saga_log(self, mensaje):
        # TODO Persistir estado en DB
        # Probablemente usted podría usar un repositorio para ello
        ...

    def construir_comando(self, evento: EventoDominio, tipo_comando: type):
        # TODO Transforma un evento en la entrada de un comando
        # Por ejemplo si el evento que llega es ReservaCreada y el tipo_comando es PagarReserva
        # Debemos usar los atributos de ReservaCreada para crear el comando PagarReserva
        comando=Comando()
        if tipo_comando == RevertirFacturacion:
            comando=RevertirFacturacion(
                
            )
        elif tipo_comando == RevertirPago:
            comando=RevertirPago(
                id_correlacion = evento.id_correlacion,
                id_cliente = evento.id_cliente,
                estado = evento.estado
            )
        elif tipo_comando == RevertirNotificacion:
            comando=RevertirNotificacion(
                
            )
        return comando


# TODO Agregue un Listener/Handler para que se puedan redireccionar eventos de dominio
def oir_mensaje(mensaje):
    if isinstance(mensaje, EventoDominio):
        coordinador = CoordinadorReservas()
        coordinador.inicializar_pasos(mensaje.id_correlacion)
        coordinador.procesar_evento(mensaje)
    else:
        raise NotImplementedError("El mensaje no es evento de Dominio")
