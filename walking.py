from training import Training


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    CALORIES_MEAN_SPEED_MULTIPLIER: int = 0.035
    CALORIES_MEAN_SPEED_SHIFT: int = 0.029
    M_IN_SM: int = 100  # Константа для перевода из метров в сантиметры
    KMH_IN_MS: int = 0.278  # Константа для перевода из км/ч в м/с
    K_1 = 2  # Константа для перевода в степень.

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float):
        super().__init__(action, duration, weight)
        self.height = height / self.M_IN_SM

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        speed_mc = self.get_mean_speed() * self.KMH_IN_MS
        return ((self.CALORIES_MEAN_SPEED_MULTIPLIER * self.weight
                 + (speed_mc ** self.K_1 / self.height)
                 * self.CALORIES_MEAN_SPEED_SHIFT * self.weight)
                * (self.duration * self.H_IN_M))
