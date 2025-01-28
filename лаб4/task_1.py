class Transport:
    """
    Базовый класс для описания транспортных средств.
    """
    def __init__(self, brand: str, model_name: str, production_year: int):
        """
        Конструктор базового класса.
        """
        self.brand = brand  # Производитель
        self.model_name = model_name  # Модель
        self.production_year = production_year  # Год выпуска

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта в читаемом виде.
        """
        return f"{self.production_year} {self.brand} {self.model_name}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта для разработчика.
        """
        return f"Transport(brand='{self.brand}', model_name='{self.model_name}', production_year={self.production_year})"

    def start(self) -> str:
        """
        Метод для запуска транспортного средства.
        return: Сообщение о запуске.
        """
        return f"Двигатель {self.model_name} запускается плавно."


class PassengerCar(Transport):
    """
    Дочерний класс для легковых автомобилей.
    """
    def __init__(self, brand: str, model_name: str, production_year: int, seat_count: int):
        """
        Расширение конструктора базового класса для легковых автомобилей.
        """
        super().__init__(brand, model_name, production_year)
        self.__seat_count = seat_count  # Инкапсуляция количества мест

    def __str__(self) -> str:
        """
        Перегрузка метода для представления объекта в читаемом виде.
        """
        return f"{super().__str__()} с {self.__seat_count} сиденьями"

    def play_radio(self, radio_station: str) -> str:
        """
        Метод для воспроизведения радиостанции.
        return: Сообщение о воспроизведении радиостанции.
        """
        return f"Сейчас играет радиостанция {radio_station} в {self.model_name}."


class FreightTruck(Transport):
    """
    Дочерний класс для грузовых автомобилей.
    """
    def __init__(self, brand: str, model_name: str, production_year: int, max_weight: float):
        """
        Расширение конструктора базового класса для грузовиков.
        """
        super().__init__(brand, model_name, production_year)
        self.max_weight = max_weight  # Грузоподъёмность

    def __str__(self) -> str:
        """
        Перегрузка метода для представления объекта с указанием грузоподъёмности.
        """
        return f"{super().__str__()} с максимальной грузоподъёмностью {self.max_weight} тонн"

    def start(self) -> str:
        """
        Перегрузка метода запуска двигателя для грузовика.
        Причина: Грузовики требуют особого внимания к мощности двигателя.
        return: Сообщение о запуске двигателя.
        """
        return f"Двигатель грузовика {self.model_name} рычит, мощно заводясь."


if __name__ == "__main__":
    # Примеры использования классов
    passenger_car = PassengerCar("Ford", "Focus", 2020, 5)
    freight_truck = FreightTruck("Scania", "R500", 2022, 18.0)

    print(passenger_car)
    print(passenger_car.start())
    print(passenger_car.play_radio("Рок FM"))

    print(freight_truck)
    print(freight_truck.start())
