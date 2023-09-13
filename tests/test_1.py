import unittest

from my_shapes_lib.area_of_figures import ShapeFactory

class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        # Создаем круг с радиусом 5
        circle = ShapeFactory.create_circle(5)
        # Вычисляем площадь круга и проверяем, что она равна ожидаемому значению
        self.assertAlmostEqual(circle.area(), 78.54, places=2)

    def test_triangle_area(self):
        # Создаем треугольник с длинами сторон 3, 4 и 5
        triangle = ShapeFactory.create_triangle(3, 4, 5)
        # Вычисляем площадь треугольника и проверяем, что она равна ожидаемому значению
        self.assertAlmostEqual(triangle.area()[0], 6.0, places=2)

    def test_is_right_triangle(self):
        # Создаем треугольник с длинами сторон 3, 4 и 5
        triangle = ShapeFactory.create_triangle(3, 4, 5)
        # Проверяем, является ли треугольник прямоугольным
        self.assertTrue(triangle.area()[1])

