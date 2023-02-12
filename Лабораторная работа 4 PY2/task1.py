class Quadrangle:
    """
    Класс Четырехугольник
    :param sides: четыре стороны произвольного четырехугольника
    """
    def __int__(self, sides):
        self.sides = [0 for i in range(4)]

    def set_sides(self):
        self.sides = [float(input("Введите сторону " + str(i+1) + " : ")) for i in range(4)]

    def __str__(self):
        return f" Четырехугольник со стронами {self.sides}"

    def __repr__(self):
        return f"{self.__class__.__name__}(sides={self.sides!r})"


class Trapeze(Quadrangle):
    """
    Класс Трапеция
    :param sides: четыре стороны трапеции (ввод в следующей последовательности:
    основание, основание, боковая сторона, боковая сторона
    :param square: площадь трапеции
    """
    def __int__(self, square):
        super().__init__(sides)
        self.square = square

    def set_sides(self):
        super().set_sides()


    def square_calc(self):
        #расчёт площади трапеции, если такая трапеция существует
        self.square = "число"
        return f"Площаль трапеции : {self.square}"

    def __str__(self):
        return f" Трапеция со стронами {self.sides}"

    def __repr__(self):
        return f"{self.__class__.__name__}(sides={self.sides!r})"



if __name__ == "__main__":
    quadrangle = Quadrangle()
    quadrangle.set_sides()
    print(quadrangle)
    print(repr(quadrangle))

    trapeze = Trapeze()
    trapeze.set_sides()
    print(trapeze.square_calc())
    print(trapeze)
    print(repr(trapeze))
