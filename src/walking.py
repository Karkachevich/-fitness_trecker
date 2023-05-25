from dataclasses import dataclass
from typing import ClassVar

from training import Training


@dataclass
class SportsWalking(Training):
    """Класс тренировки: Спортивная ходьба."""
    CALORIES_MEAN_SPEED_MULTIPLIER: ClassVar[int] = 0.035
    CALORIES_MEAN_SPEED_SHIFT: ClassVar[int] = 0.029
    M_IN_SM: ClassVar[int] = 100  # Константа перевода из метров в сантиметры
    KMH_IN_MS: ClassVar[int] = 0.278  # Константа для перевода из км/ч в м/с
    K_1: ClassVar[int] = 2  # Константа для перевода в степень.

    height: float

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        speed_mc = self.get_mean_speed() * self.KMH_IN_MS
        height_cm = self.height / self.M_IN_SM
        return ((self.CALORIES_MEAN_SPEED_MULTIPLIER * self.weight
                 + (speed_mc ** self.K_1 / height_cm)
                 * self.CALORIES_MEAN_SPEED_SHIFT * self.weight)
                * (self.duration * self.H_IN_M))
