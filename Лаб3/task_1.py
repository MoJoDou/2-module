class Book:
    """Базовый класс книги.
    Хранит общую информацию о книге, такую как название и автор. Метод __str__ используется для
    получения строкового представления книги с учетом ее типа. Метод __repr__ предоставляет
    официальное строковое представление книги.
    """

    def __init__(self, name: str, author: str):
        """Инициализирует объект книги с заданным названием и автором.
        Аргументы:
        name -- название книги
        author -- автор книги
        """
        self._name = name
        self._author = author

    @property
    def name(self):
        """Возвращает название книги (только для чтения)."""
        return self._name

    @property
    def author(self):
        """Возвращает автора книги (только для чтения)."""
        return self._author

    def __str__(self):
        """Возвращает строковое представление книги с учетом ее типа.
        В зависимости от типа книги (PaperBook или AudioBook) добавляются дополнительные детали:
        количество страниц или продолжительность книги.
        """
        details = ""
        if isinstance(self, PaperBook):
            details = f". Страниц: {self.pages}"
        elif isinstance(self, AudioBook):
            details = f". Продолжительность: {self.duration} часов"
        return f"{self.__class__.__name__} {self.name}. Автор {self.author}{details}"

    def __repr__(self):
        """Возвращает официальное представление книги.
        Этот метод используется для отображения базовой информации о книге в виде строки.
        """
        return f"Book(name='{self.name}', author='{self.author}')"


class PaperBook(Book):
    """Класс для бумажной книги.
    Хранит информацию о бумажной книге, включая название, автора и количество страниц.
    """

    def __init__(self, name: str, author: str, pages: int):
        """Инициализирует объект бумажной книги.
        Аргументы:
        name -- название книги
        author -- автор книги
        pages -- количество страниц книги
        """
        super().__init__(name, author)
        self.pages = pages  # Используется setter для проверки

    @property
    def pages(self):
        """Возвращает количество страниц книги."""
        return self._pages

    @pages.setter
    def pages(self, value):
        """Устанавливает количество страниц книги с проверкой, что оно является положительным числом.
        Аргументы:
        value -- количество страниц
        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        self._pages = value

    def __repr__(self):
        """Возвращает официальное представление бумажной книги."""
        return f"PaperBook(name='{self.name}', author='{self.author}', pages={self.pages})"


class AudioBook(Book):
    """Класс для аудиокниги.
    Хранит информацию о аудиокниге, включая название, автора и продолжительность в часах.
    """

    def __init__(self, name: str, author: str, duration: float):
        """Инициализирует объект аудиокниги.

        Аргументы:
        name -- название книги
        author -- автор книги
        duration -- продолжительность книги в часах
        """
        super().__init__(name, author)
        self.duration = duration  # Используется setter для проверки

    @property
    def duration(self):
        """Возвращает продолжительность аудиокниги в часах."""
        return self._duration

    @duration.setter
    def duration(self, value):
        """Устанавливает продолжительность аудиокниги с проверкой, что она является положительным числом.
        Аргументы:
        value -- продолжительность в часах
        """
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = value

    def __repr__(self):
        """Возвращает официальное представление аудиокниги."""
        return f"AudioBook(name='{self.name}', author='{self.author}', duration={self.duration})"


# Пример использования
try:
    # Создаем экземпляры книг
    paper_book = PaperBook("Идиот", "Фёдор Достоевский", 640)
    audio_book = AudioBook("Песнь льда и огня", "Джордж Р. Р. Мартин", 768)

    # Печатаем информацию о книгах
    print(paper_book)  # Бумажная книга Идиот. Автор Фёдор Достоевский. Страниц: 640
    print(audio_book)  # Аудиокнига Песнь льда и огня. Автор Джордж Р. Р. Мартин. Продолжительность: 768 часов

    # Попытка установить некорректное количество страниц
    paper_book.pages = -5  # Ошибка: количество страниц должно быть положительным числом
except ValueError as e:
    print(e)
