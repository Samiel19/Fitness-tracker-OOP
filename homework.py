class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float
                 ) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self):
        """Получить информационное сообщение."""
        info = (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.duration} ч; '
                f'Дистанция: {self.distance} км; '
                f'Ср.скорость: {self.speed} км/ч; '
                f'Потрачено ккал: {self.calories}.')
        return info


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
        self.LEN_STEP = 0.65
        self.M_IN_KM = 1000

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения в км/ч."""
        speed = self.get_distance() / self.duration
        return speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        training_type = self.__class__.__name__
        duration = round(self.duration, 3)
        distance = round(self.get_distance(), 3)
        speed = round(self.get_mean_speed(), 3)
        calories = round(self.get_spent_calories(), 3)
        return InfoMessage(training_type, duration, distance, speed, calories)


class Running(Training):
    """Тренировка: бег."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float) -> None:
        super().__init__(action, duration, weight)
        self.CALORIES_MEAN_SPEED_MULTIPLIER = 18
        self.CALORIES_MEAN_SPEED_SHIFT = 1.79
        # Переводим время тренировки в минуты
        self.dur_min = self.duration * 60

    def get_spent_calories(self) -> float:
        """Получить потраченые калории."""
        calories = ((self.CALORIES_MEAN_SPEED_MULTIPLIER
                    * super().get_mean_speed()
                    + self.CALORIES_MEAN_SPEED_SHIFT)
                    * self.weight / self.M_IN_KM * self.dur_min)
        return calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height
        self.CALORIES_WEIGHT_MULTIPLIER_1 = 0.035
        self.CALORIES_WEIGHT_MULTIPLUER_2 = 0.029
        # Переводим время тренировки в минуты
        self.dur_min = self.duration * 60
        # Перерводим скорость в м/с2
        self.speed_ms = super().get_mean_speed() * 1000 / 3600
        # Переводим рост в метры
        self.height_m = self.height / 100

    def get_spent_calories(self) -> float:
        """Получить потраченые каллории."""
        calories = ((self.CALORIES_WEIGHT_MULTIPLIER_1 * self.weight
                    + (self.speed_ms ** 2 / self.height_m)
                    * self.CALORIES_WEIGHT_MULTIPLUER_2
                    * self.weight) * self.dur_min)
        return calories


class Swimming(Training):
    """Тренировка: плавание."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: float) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool
        self.LEN_STEP = 1.38
        self.CALORIES_SPEED_SHIFT = 1.1
        self.CALORIES_WEIGHT_MULTIPLIER = 2

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        speed = (self.length_pool * self.count_pool
                 / self.M_IN_KM / self.duration)
        return speed

    def get_spent_calories(self) -> float:
        """Получить потраченые калории."""
        calories = ((self.get_mean_speed() + self.CALORIES_SPEED_SHIFT)
                    * self.CALORIES_WEIGHT_MULTIPLIER
                    * self.weight * self.duration)
        return calories


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    workouts = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }
    return workouts[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
