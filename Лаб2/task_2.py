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

# TODO написать класс Library
class Library:
    """
    Класс для представления библиотеки.
    Атрибуты:
        books (list): Список книг в библиотеке.
    """

    def __init__(self, books=None):
        """
        Инициализация библиотеки.
        Параметры:
            books (list, optional): Список книг для инициализации библиотеки. По умолчанию пустой список.
        """
        self.books = books if books is not None else []

    def get_next_book_id(self):
        """
        Получение следующего доступного идентификатора для книги.
        Возвращает:
            int: Следующий доступный идентификатор книги.
        """
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id):
        """
        Поиск индекса книги по её идентификатору.
        Параметры:
            book_id (int): Идентификатор книги.

        Возвращает:
            int: Индекс книги в списке.
        Исключения:
            ValueError: Если книга с заданным id не найдена.
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1

