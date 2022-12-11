import doctest


class Student:
    def __init__(self, FIO, group, email):
        """
        Создание и подготовка к работе объекта "Студент"
        :param FIO: ФИО студента
        :param group: Номер группы
        :param email: адрес эл. почты
        Примеры:
        >>> ivanov_ii = Student("Иванов Иван Иванович", "4941601/00001", "ivanov.ii4@edu.spbstu.ru")  # инициализация экземпляра класса
        """
        if not isinstance(FIO, str):
            raise TypeError("ФИО должно быть типа str")
        self.FIO = FIO
        if not isinstance(group, str):
            raise TypeError("Номер группы должен быть типа str")
        self.group = group
        if not isinstance(email, str):
            raise TypeError("Адрес эл. почты должен быть типа str")
        self.email = email

    def mark_as_present(self):
        ...
        """
        Функция которая отмечает студента присутствующим на паре
        :return: Присутствует ли студент на паре
        Примеры:
        >>> ivanov_ii = Student("Иванов Иван Иванович", "4941601/00001", "ivanov.ii4@edu.spbstu.ru")
        >>> ivanov_ii.mark_as_present()
        """

    def mark_as_absent(self):
        ...
        """
        Функция которая отмечает студента отсутствующим на паре
        :return: Отсутствует ли студент на паре
        Примеры:
        >>> ivanov_ii = Student("Иванов Иван Иванович", "4941601/00001", "ivanov.ii4@edu.spbstu.ru")
        >>> ivanov_ii.mark_as_absent()
        """


class Professor:
    def __init__(self, prof_FIO, prof_email):
        """
        Создание и подготовка к работе объекта "Профессор"
        :param prof_FIO: ФИО профессора
        :param prof_email: адрес эл. почты профессора
        Примеры:
        >>> rul_ni = Professor("Руль Николай Игоревич", "rul.ni@spbstu.ru")  # инициализация экземпляра класса
        """
        if not isinstance(prof_FIO, str):
            raise TypeError("ФИО должно быть типа str")
        self.prof_FIO = prof_FIO
        if not isinstance(prof_email, str):
            raise TypeError("Адрес эл. почты должен быть типа str")
        self.prof_email = prof_email

    def new_letter(self):
        ...
        """
        Функция, которая проверяет, получены ли новые письма с этой почты
        :return: есть ли письма с этого эл. адреса
        Примеры:
        >>> rul_ni = Professor("Руль Николай Игоревич", "rul.ni@spbstu.ru")
        >>> rul_ni.new_letter()
        """

    def generate_letter(self):
        ...
        """
        Функция, которая генерирует шаблон письма
        :return: шаблон письма
        Примеры:
        >>> rul_ni = Professor("Руль Николай Игоревич", "rul.ni@spbstu.ru")
        >>> rul_ni.generate_letter()
        """


class Schedule:
    def __init__(self, *subject):
        """
        Создание и подготовка к работе объекта "Расписание дня"
        :param subject: предмет, время, группа, профессор
        Примеры:
        >>> friday = Schedule("Физика", "12:00", "4941601/00001", "Руль Николай Игоревич")  # инициализация экземпляра класса
        """
        if len(subject) < 3:
            raise ValueError("Не хватает аргументов. Впишите  предмет, время, группу, профессора")
        self.subject = subject

    def change(self, subject, time, group, professor):
        ...
        """
        Функция, которая изменяет расписание
        :return: изменение расписания
        Примеры:
        >>> friday = Schedule("Физика", "12:00", "4941601/00001", "Руль Николай Игоревич")
        >>> friday.change()
        """
    def break_for_holiday(self):
        ...
        """
        Функция, которая отменяет все пары в праздничный деень
        :return: отмена пар
        Примеры:
        >>> friday = Schedule("Физика", "12:00", "4941601/00001", "Руль Николай Игоревич")
        >>> friday.break_for_holiday()
        """


if __name__ == "__main__":
    doctest.testmod()
