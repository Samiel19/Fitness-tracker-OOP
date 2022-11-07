class InfoMessage:
    """Информационное сообщение о тренировке."""
    


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
        speed = self.get_distance()/ self.duration
        return speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        training_type = self.__name__
        return (f'Тип тренировки: {training_type};'
        f'Длительность: {self.duration} ч;'
        f'Дистанция: {self.get_distance(self)} км;'
        f'Ср.скорость: {self.get_mean_speed(self)} км/ч;')
        


class Running(Training):
    """Тренировка: бег."""
    def __init__(self, action: int, duration: float, weight: float):
        super().__init__(action, duration, weight)
        self.CALORIES_MEAN_SPEED_MULTIPLIER = 18
        self.CALORIES_MEAN_SPEED_SHIFT = 1.79
        #Переводим время тренировки в минуты
        self.dur_min = self.duration * 60


    def get_spent_calories(self):
        calories = ((self.CALORIES_MEAN_SPEED_MULTIPLIER * super().get_mean_speed() 
        + self.CALORIES_MEAN_SPEED_SHIFT) * self.weight / self.M_IN_KM * self.dur_min)
        return calories

    


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(self, action: int, duration: float, weight: float, height: float):
        super().__init__(action, duration, weight)
        self.height = height
        self.CALORIES_WEIGHT_MULTIPLIER = 0.035
        self.CALORIES_WEIGHT_SHIFT = 0.029
        #Переводим время тренировки в минуты
        self.dur_min = self.duration * 60
        #Перерводим скорость в м/с2
        self.speed_ms = super().get_mean_speed() * 1000 / 3600
        #Переводим рост в метры
        self.height_m = self.height / 100

        
    def get_spent_calories(self) -> float:
        calories = ((self.CALORIES_WEIGHT_MULTIPLIER * self.weight + (self.speed_ms **2 / 
        self.height_m) * self.CALORIES_WEIGHT_SHIFT * self.weight) * self.dur_min) 
        return calories



class Swimming(Training):
    """Тренировка: плавание."""
    def __init__(self, action: int, duration: float, weight: float, length_pool: float, count_pool: float):
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool
        self.LEN_STEP = 1.38
        self.CALORIES_SPEED_SHIFT = 1.1
        self.CALORIES_WEIGHT_MULTIPLIER = 2


    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        speed = self.length_pool * self.count_pool / self.M_IN_KM / self.duration
        return speed   


    def get_spent_calories(self) -> float:
        calories = ((self.get_mean_speed() + self.CALORIES_SPEED_SHIFT) * 
        self.CALORIES_WEIGHT_MULTIPLIER * self.weight * self.duration)
        return calories


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
print(f'Расстояние {train.get_distance()}')
print(f'Средняя скорость {train.get_mean_speed()}')
print(f'Каллории {train.get_spent_calories()}')
train2 = SportsWalking(9000, 1, 75, 180)
print(train2.get_distance())
print(train2.get_mean_speed())
print(train2.get_spent_calories())
train3 = Swimming(720, 1, 80, 25, 40)
print(train3.get_distance())
print(train3.get_mean_speed())
print(train3.get_spent_calories())
print(train.show_training_info)