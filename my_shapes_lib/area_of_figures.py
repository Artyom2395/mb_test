import math

class ShapeFactory:
    @staticmethod
    def create_circle(radius):
        return Circle(radius)

    @staticmethod
    def create_triangle(side1, side2, side3):
        return Triangle(side1, side2, side3)

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        if self.radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        return math.pi * self.radius**2

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        if self.side1 <= 0 or self.side2 <= 0 or self.side3 <= 0:
            raise ValueError("Длины сторон должны быть положительными числами")

        # Проверяем, является ли треугольник прямоугольным
        sides = sorted([self.side1, self.side2, self.side3])
        if sides[0]**2 + sides[1]**2 == sides[2]**2:
            is_right_triangle = True
        else:
            is_right_triangle = False

        # Вычисляем полупериметр
        s = (self.side1 + self.side2 + self.side3) / 2

        # Вычисляем площадь по формуле Герона
        area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        return area, is_right_triangle

## Создаем круг с радиусом 5
#circle = ShapeFactory.create_circle(5)
## Вычисляем площадь круга
#circle_area = circle.area()
#print(f"Площадь круга: {circle_area:.2f}")
#
## Создаем треугольник с длинами сторон 3, 4 и 5
#triangle = ShapeFactory.create_triangle(3, 4, 5)
## Вычисляем площадь треугольника и проверяем, является ли он прямоугольным
#triangle_area, is_right_triangle = triangle.area()
#print(f"Площадь треугольника: {triangle_area:.2f}")
#if is_right_triangle:
#    print("Треугольник прямоугольный")
#else:
#    print("Треугольник не прямоугольный")
        