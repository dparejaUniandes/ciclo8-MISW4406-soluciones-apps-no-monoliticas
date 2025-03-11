from gestionclientes.modulos.sagas.aplicacion.comandos.crear_facturacion import \
    CrearFacturacion
from gestionclientes.modulos.sagas.aplicacion.comandos.crear_notificacion import \
    CrearNotificacion
from gestionclientes.modulos.sagas.aplicacion.comandos.realizar_pago import \
    RealizarPago
from gestionclientes.modulos.sagas.aplicacion.comandos.revertir_facturacion import \
    RevertirFacturacion
from gestionclientes.modulos.sagas.aplicacion.comandos.revertir_notificacion import \
    RevertirNotificacion
from gestionclientes.modulos.sagas.aplicacion.comandos.revertir_pago import \
    RevertirPago
from gestionclientes.modulos.sagas.dominio.entidades import Saga
from gestionclientes.modulos.sagas.dominio.eventos.facturacion import (
    FacturacionCreada, FacturacionFallida, FacturacionRevertida)
from gestionclientes.modulos.sagas.dominio.eventos.notificacion import (
    NotificacionCreada, NotificacionFallida, NotificacionRevertida)
from gestionclientes.modulos.sagas.dominio.eventos.pagos import (PagoFallido,
                                                                 PagoRealizado,
                                                                 PagoRevertido)
from gestionclientes.modulos.sagas.dominio.repositorios import RepositorioSagas
from gestionclientes.modulos.sagas.infraestructura.fabricas import \
    FabricaRepositorio
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
        # self.persistir_en_saga_log(self.pasos[0])
        ...
    
    def terminar(self):
        # self.persistir_en_saga_log(self.pasos[-1])
        ...

    def persistir_en_saga_log(self, evento, paso, index):
        # TODO Persistir estado en DB
        # Probablemente usted podría usar un repositorio para ello
        nombre_paso = ""
        estado = ""
        if type(evento) == FacturacionCreada or type(evento) == FacturacionFallida:
            nombre_paso = FacturacionCreada.__name__ if type(evento) == FacturacionCreada else RevertirFacturacion.__name__,
            estado = "INICIO"
        elif type(evento) == PagoRealizado or type(evento) == PagoFallido:
            nombre_paso = PagoRealizado.__name__ if type(evento) == PagoRealizado else RevertirPago.__name__,
            estado = "MEDIO"
        elif type(evento) == NotificacionCreada or type(evento) == NotificacionFallida:
            nombre_paso = NotificacionCreada.__name__ if type(evento) == NotificacionCreada else RevertirNotificacion.__name__,
            estado = "FIN"
        saga = Saga(
            id_correlacion = evento.id_correlacion,
            id_cliente = evento.id_cliente,
            nombre_paso = nombre_paso[0],
            estado = estado,
            index = index
        )
        fabrica = FabricaRepositorio()
        repositorio=fabrica.crear_objeto(RepositorioSagas)
        repositorio.agregar(saga)
        

    def construir_comando(self, evento: EventoDominio, tipo_comando: type, index: int):
        # TODO Transforma un evento en la entrada de un comando
        # Por ejemplo si el evento que llega es ReservaCreada y el tipo_comando es PagarReserva
        # Debemos usar los atributos de ReservaCreada para crear el comando PagarReserva
        comando=Comando()
        if tipo_comando == RevertirFacturacion:
            comando=RevertirFacturacion(
                id_correlacion = evento.id_correlacion,
                id_cliente = evento.id_cliente,
                nombre_paso = RevertirFacturacion.__name__,
                estado = "INICIO",
                index = index
            )
        elif tipo_comando == RevertirPago:
            comando=RevertirPago(
                id_correlacion = evento.id_correlacion,
                id_cliente = evento.id_cliente,
                nombre_paso = RevertirPago.__name__,
                estado = "MEDIO",
                index = index
            )
        elif tipo_comando == RevertirNotificacion:
            comando=RevertirNotificacion(
                id_correlacion = evento.id_correlacion,
                id_cliente = evento.id_cliente,
                nombre_paso = RevertirNotificacion.__name__,
                estado = "FIN",
                index = index
            )
        if tipo_comando == CrearFacturacion:
            comando=CrearFacturacion(
                id_correlacion = evento.id_correlacion,
                id_cliente = evento.id_cliente,
                nombre_paso = CrearFacturacion.__name__,
                estado = "INICIO",
                index = index
            )
        elif tipo_comando == RealizarPago:
            comando=RealizarPago(
                id_correlacion = evento.id_correlacion,
                id_cliente = evento.id_cliente,
                nombre_paso = RealizarPago.__name__,
                estado = "MEDIO",
                index = index
            )
        elif tipo_comando == CrearNotificacion:
            comando=CrearNotificacion(
                id_correlacion = evento.id_correlacion,
                id_cliente = evento.id_cliente,
                nombre_paso = CrearNotificacion.__name__,
                estado = "FIN",
                index = index
            )
        return comando


# TODO Agregue un Listener/Handler para que se puedan redireccionar eventos de dominio
def oir_mensaje(evento):
    print("EVENTO***: ", evento, isinstance(evento, EventoDominio))
    if isinstance(evento, EventoDominio):
        coordinador = CoordinadorReservas()
        coordinador.inicializar_pasos(evento.id_correlacion)
        paso, index = coordinador.obtener_paso_dado_un_evento(evento)
        coordinador.persistir_en_saga_log(evento, paso, index)
        if type(evento) != FacturacionFallida and type(evento) != NotificacionFallida:
            coordinador.procesar_evento(evento)
    else:
        raise NotImplementedError("El mensaje no es evento de Dominio")
