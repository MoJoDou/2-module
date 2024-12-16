# TODO Написать 3 класса с документацией и аннотацией типов
# TODO работоспособность экземпляров класса проверить с помощью doctest
from typing import Union
import doctest

class Table:
    def __init__(self, length: float, width: float, material: str):
        """
        Создание и подготовка объекта "Стол"
        :param length: Длина стола
        :param width: Ширина стола
        :param material: Материал стола
        Примеры:
        >>> table = Table(120, 80, "wood")
        """
        if not isinstance(length, (int, float)) or length <= 0:
            raise ValueError("Длина должна быть положительным числом")
        if not isinstance(width, (int, float)) or width <= 0:
            raise ValueError("Ширина должна быть положительным числом")
        if not isinstance(material, str) or not material:
            raise ValueError("Материал должен быть строкой")
        self.length = length
        self.width = width
        self.material = material

    def calculate_area(self) -> float:
        """
        Вычисляет площадь стола.
        :return: Возвращает площадь стола в квадратных сантиметрах
        Примеры:
        >>> table = Table(120, 80, "wood")
        >>> table.calculate_area()
        9600.0
        """
        return float(self.length * self.width)
    def describe_material(self) -> str:
        """
        Возвращает строку с описанием материала стола.
        :return:
        Примеры:
        >>> table = Table(120, 80, "wood")
        >>> table.describe_material()
        'Материал стола: wood'
        """
        return f"Материал стола: {self.material}"


class Tree:
    def __init__(self, height: float, age: int, species: str):
        """
        Создание и подготовка объекта "Дерево"
        :param height: Высота дерева
        :param age: Возраст дерева
        :param species: Вид дерева
        Примеры:
        >>> tree = Tree(15.5, 100, "oak")
        """
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Высота должна быть положительным числом")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Возраст должен быть неотрицательным целым числом")
        if not isinstance(species, str) or not species:
            raise ValueError("Вид дерева должен быть строкой")
        self.height = height
        self.age = age
        self.species = species

    def grow(self, years: int) -> None:
        """
        Увеличивает возраст и высоту дерева.
        :param years: Количество лет роста
        Примеры:
        >>> tree = Tree(15.5, 100, "oak")
        >>> tree.grow(10)
        >>> tree.age
        110
        """
        if not isinstance(years, int) or years <= 0:
            raise ValueError("Количество лет должно быть положительным целым числом")
        self.age += years
        self.height += years * 0.5  # Предположим, что дерево растет на 0.5 метра в год

    def describe(self) -> str:
        """
        Описание дерева.
        :return: Строка с описанием дерева
        Примеры:
        >>> tree = Tree(15.5, 100, "oak")
        >>> tree.describe()
        'Дерево вида oak высотой 15.5 м и возрастом 100 лет'
        """
        return f"Дерево вида {self.species} высотой {self.height} м и возрастом {self.age} лет"


class Stack:
    """
    Класс для описания структуры данных "Стек"
    Атрибуты:
     items (list): список элементов в стеке
    """
    def __init__(self):
        """
        Создание и подготовка объекта "Стек"
        Примеры:
        >>> stack = Stack()
        """
        self.items = []

    def push(self, item: Union[int, str, float]) -> None:
        """
        Добавляет элемент в стек.
        :param item: Элемент для добавления
        Примеры:
        >>> stack = Stack()
        >>> stack.push(5)
        >>> stack.items
        [5]
        """
        self.items.append(item)

    def pop(self) -> Union[int, str, float]:
        """
        Удаляет и возвращает верхний элемент стека.
        :return:
        Примеры:
        >>> stack = Stack()
        >>> stack.push(5)
        >>> stack.push(10)
        >>> stack.pop()
        10
        """
        if not self.items:
            raise IndexError("Стек пуст")
        return self.items.pop()

    def is_empty(self) -> bool:
        """
        Проверяет, пуст ли стек.
        :return: True, если стек пуст, иначе False
        Примеры:
        >>> stack = Stack()
        >>> stack.is_empty()
        True
        """
        return len(self.items) == 0


if __name__ == "__main__":
    doctest.testmod()
