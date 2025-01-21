# База данных книг в виде списка словарей
BOOKS_DATABASE = [
    {
        "id": 1,  # Уникальный идентификатор первой книги
        "name": "test_name_1",  # Название первой книги
        "pages": 200,  # Количество страниц в первой книге
    },
    {
        "id": 2,  # Уникальный идентификатор второй книги
        "name": "test_name_2",  # Название второй книги
        "pages": 400,  # Количество страниц во второй книге
    }
]



# TODO написать класс Book
# Определение класса Book для представления книги
class Book:
    """
    Класс для представления книги.

    Атрибуты:
        id (int): Уникальный идентификатор книги.
        name (str): Название книги.
        pages (int): Количество страниц в книге.
    """

    def __init__(self, id_, name, pages):
        """
        Инициализация объекта класса Book.

        Параметры:
            id_ (int): Уникальный идентификатор книги.
            name (str): Название книги.
            pages (int): Количество страниц в книге.
        """
        self.id = id_  # Присваиваем уникальный идентификатор книги
        self.name = name  # Присваиваем название книги
        self.pages = pages  # Присваиваем количество страниц книги

    def __str__(self):
        """
        Возвращает строковое представление объекта Book.

        Возвращает:
            str: Строка формата 'Книга "<название книги>"'.
        """
        return f'Книга "{self.name}"'  # Формируем строку с названием книги

    def __repr__(self):
        """
        Возвращает представление объекта Book для отладки.

        Возвращает:
            str: Строка формата 'Book(id_=<id>, name='<название>', pages=<количество страниц>)'.
        """
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"  # Формируем строку с полями книги


if __name__ == '__main__':
    # Инициализация списка объектов класса Book из базы данных
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"])  # Создание объекта Book из словаря
        for book_dict in BOOKS_DATABASE  # Перебор каждой книги в базе данных
    ]

    # Проверяем метод __str__ для каждого объекта Book
    for book in list_books:
        print(book)  # Выводим строковое представление книги

    # Проверяем метод __repr__ для списка объектов Book
    print(list_books)  # Выводим формальное представление списка книг
