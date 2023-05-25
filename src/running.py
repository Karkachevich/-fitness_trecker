from dataclasses import dataclass
from typing import ClassVar

from training import Training


@dataclass
class Running(Training):
    """Класс тренировки: Бег."""
    CALORIES_MEAN_SPEED_MULTIPLIER: ClassVar[int] = 18
    CALORIES_MEAN_SPEED_SHIFT: ClassVar[int] = 1.79

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        return ((self.CALORIES_MEAN_SPEED_MULTIPLIER
                 * self.get_mean_speed()
                 + self.CALORIES_MEAN_SPEED_SHIFT)
                * self.weight / self.M_IN_KM
                * (self.duration * self.H_IN_M))
