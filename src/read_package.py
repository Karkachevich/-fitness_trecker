from running import Running
from swimming import Swimming
from training import Training
from walking import SportsWalking


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    workout = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }
    if workout_type in workout:
        return workout[workout_type](*data)
    raise ValueError(f'<{workout_type}> - нет такой тренировки.')
