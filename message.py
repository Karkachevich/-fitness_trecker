from dataclasses import dataclass, asdict
from typing import ClassVar


@dataclass()
class InfoMessage:
    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float

    TEXT_INFO: ClassVar[str] = ('Тип тренировки: {training_type}; '
                                'Длительность: {duration:.3f} ч.; '
                                'Дистанция: {distance:.3f} км; '
                                'Ср. скорость: {speed:.3f} км/ч; '
                                'Потрачено ккал: {calories:.3f}.')

    def get_message(self) -> str:
        return self.TEXT_INFO.format(**asdict(self))
