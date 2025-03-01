from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class DTO():
    """ DTO base """


class Mapeador(ABC):
    """ Mapeador de DTOs """
    @abstractmethod
    def externo_a_dto(self, externo: any) -> DTO:
        """ Convierte un objeto externo a un DTO """

    @abstractmethod
    def dto_a_externo(self, dto: DTO) -> any:
        """ Convierte un DTO a un objeto externo """
    