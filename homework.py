class InfoMessage:
    """Информационное сообщение о тренировке."""
    pass


class Training:
    """Базовый класс тренировки."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight
        

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * self.LEN_STEP / self.M_IN_KM 
        return distance


    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        speed = Training.get_distance(self)/ self.duration
        return speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        pass


class Running(Training):
    """Тренировка: бег."""
    def __init__(self, action: int, duration: float, weight: float):
        super().__init__(action, duration, weight)
        self.LEN_STEP = 0.65
        self.M_IN_KM = 1000
        self.CALORIES_MEAN_SPEED_MULTIPLIER = 18
        self.CALORIES_MEAN_SPEED_SHIFT = 1.79 


    def get_spent_calories(self):
        calories = (self.CALORIES_MEAN_SPEED_MULTIPLIER * super().get_mean_speed() + self.CALORIES_MEAN_SPEED_SHIFT) * self.weight / self.M_IN_KM * self.duration
        return calories

    


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(self, action: int, duration: float, weight: float):
        super().__init__(action, duration, weight)
        self.action = action
        self.duration = duration
        self.weight = weight
        self.LEN_STEP = 0.65
        self.M_IN_KM = 1000


class Swimming(Training):
    """Тренировка: плавание."""
    def __init__(self, action: int, duration: float, weight: float):
        super().__init__(action, duration, weight)
        self.action = action
        self.duration = duration
        self.weight = weight
        self.LEN_STEP = 1.38
        self.M_IN_KM = 1000


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

train = Running(15000, 1, 75)
print(train.get_distance())
print(train.get_mean_speed())
print(train.get_spent_calories())