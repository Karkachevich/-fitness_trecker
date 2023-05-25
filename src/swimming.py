from dataclasses import dataclass
from typing import ClassVar

from training import Training


@dataclass
class Swimming(Training):
    """Класс тренировки: Плавание."""
    LEN_STEP: ClassVar[int] = 1.38
    K_1: ClassVar[int] = 1.1  # Константа для подсчета калорий
    K_2: ClassVar[int] = 2  # Константа для подсчета калорий

    length_pool: int
    count_pool: int

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return (self.length_pool
                * self.count_pool / self.M_IN_KM / self.duration)

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        return ((self.get_mean_speed() + self.K_1)
                * self.K_2 * self.weight * self.duration)
