from training import Training


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP: int = 1.38
    K_1 = 1.1  # Константа для подсчета калорий
    K_2 = 2  # Константа для подсчета калорий

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: int,
                 count_pool: int):
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

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
