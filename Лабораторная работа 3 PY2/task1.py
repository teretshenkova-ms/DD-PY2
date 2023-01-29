class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = None
        self.set_pages(pages)

    def __str__(self):
        super().__str__()
        return f"Книга {self.name}. Автор {self.author}. Количество страниц {self._pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self._pages!r})"

    def get_pages(self) -> int:
        return self._pages

    def set_pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration
        self.set_duration(duration)

    def __str__(self):
        super().__str__()
        return f"Книга {self.name}. Автор {self.author}. Продолжительность {self._duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self._duration!r})"

    def get_duration(self) -> int:
        return self._duration

    def set_duration(self, new_duration: int) -> None:
        if not isinstance(new_duration, int):
            raise TypeError("Продолжительность должна быть типа int")
        if new_duration <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = new_duration


# paper = PaperBook("Physics", "Landau", 100)
# audio = AudioBook("Fairytale", "Charles Perrault", 180)
#
# print(paper)
# print(audio)
