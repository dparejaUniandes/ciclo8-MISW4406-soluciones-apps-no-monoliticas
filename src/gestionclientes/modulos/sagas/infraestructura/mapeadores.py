""" Mapeadores para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from gestionclientes.modulos.sagas.dominio.entidades import Saga

from gestionclientes.seedwork.dominio.repositorios import Mapeador

from .dto import SagaLog as SagaLogDTO


class MapeadorSagaLog(Mapeador):
    """ Mapeador de sagaLog a DTOs """
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Saga.__class__

    def entidad_a_dto(self, entidad: Saga) -> SagaLogDTO:

        saga_dto = SagaLogDTO()
        saga_dto.id = str(entidad.id)
        saga_dto.id_cliente = entidad.id_cliente
        saga_dto.id_correlacion = entidad.id_correlacion
        saga_dto.nombre_paso = entidad.nombre_paso
        saga_dto.estado = entidad.estado
        saga_dto.index = entidad.index

        return saga_dto

    def dto_a_entidad(self, dto: SagaLogDTO) -> any:
        try:
            print(type(dto))
            print(SagaLogDTO)
            if type(dto) is Saga:
          
                print("Medio DTO n\"", dto.medio)

                saga_log = Saga(
                    id=dto.id,
                    id_cliente=dto.id_cliente,
                    id_correlacion=dto.id_correlacion,
                    nombre_paso=dto.nombre_paso,
                    estado=dto.estado,
                    index=dto.index,
                    fecha_creacion=dto.fecha_creacion,
                )
                return saga_log

            saga_logs = []

            for SagaLogDTO in dto:

                saga_logs.append(Saga(
                    id=SagaLogDTO.id,
                    id_cliente=SagaLogDTO.id_cliente,
                    id_correlacion=SagaLogDTO.id_correlacion,
                    nombre_paso=SagaLogDTO.nombre_paso,
                    estado=SagaLogDTO.estado,
                    index=SagaLogDTO.index,
                    fecha_creacion=SagaLogDTO.fecha_creacion,
                ))
            return saga_logs
        except Exception as e:
            print(f'Error en mapeador: {e}')
