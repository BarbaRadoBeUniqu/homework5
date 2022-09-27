


class Figure:
    unit = "cm"
    
    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass

class Circle(Figure):
    def __init__(self, radius):
        Figure.__init__(self)
        self.__radius = radius
    
    @property
    def radius(self):
        return self.__radius
    
    @radius.setter  
    def radius(self, value):
        self.__radius = value 

    def calculate_area(self):
        return 3.14 * (self.radius ** 2)

    def info(self):
        return f"Радиус круга = {self.radius} {self.unit}, площадь круга = {self.calculate_area()} {self.unit}"

class Triangle(Figure):
    def __init__(self, side_a, side_b):
        Figure.__init__(self)
        self.__side_a = side_a
        self.__side_b = side_b

    @property
    def side_a(self):
        return self.__side_a
    
    @side_a.setter
    def side_a(self, value):
        self.__side_a = value

    @property
    def side_b(self):
        return self.__side_b
    
    @side_b.setter
    def side_b(self, value):
        self.__side_b = value


    def calculate_area(self):
        return (self.side_a * self.side_b) / 2

    def info(self):
        return f"Сторона треугольника а = {self.side_a} {self.unit}, сторона треугольника б = {self.side_b} {self.unit} площадь треугольника = {self.calculate_area()} {self.unit}"


list_figure = []
Krug = Circle(5)
Krug1 = Circle(10)
list_figure.append(Krug.info())
list_figure.append(Krug1.info())

# print(Krug.calculate_area())
# print(Krug.info())


Treugolnik = Triangle(10, 10)
Treugolnik1 = Triangle(5, 5)
Treugolnik2 = Triangle(3, 6)
list_figure.append(Treugolnik.info())
list_figure.append(Treugolnik1.info())
list_figure.append(Treugolnik2.info())

# print(Treugolnik.calculate_area())
# print(Treugolnik.info())

for i in list_figure:
    print(i)